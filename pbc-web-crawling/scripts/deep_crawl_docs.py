"""
Deep crawl documentation sites using Crawl4AI.

Crawls nested documentation sites and saves pages as markdown files,
preserving site structure.

Usage:
    python deep_crawl_docs.py <root_url> --output-dir <directory> [options]

Examples:
    python deep_crawl_docs.py https://docs.example.com -o ./docs
    python deep_crawl_docs.py https://docs.example.com -o ./docs --max-depth 3 --max-pages 100
    python deep_crawl_docs.py https://pipeline.groupthought.com -o ./pipeline-docs --pattern "*docs*"
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy, BestFirstCrawlingStrategy
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter, DomainFilter
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy


def slugify(text: str) -> str:
    """Convert text to a safe filename slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = text.strip('-')
    return text[:60] or 'untitled'


def url_to_filepath(url: str, base_domain: str, output_dir: Path) -> Path:
    """Convert URL to a file path preserving site structure."""
    parsed = urlparse(url)
    path = parsed.path.strip('/')

    if not path:
        path = 'index'

    # Clean up path segments
    segments = [slugify(seg) for seg in path.split('/') if seg]

    if not segments:
        segments = ['index']

    # Add .md extension if not present
    if not segments[-1].endswith('.md'):
        segments[-1] = f"{segments[-1]}.md"

    return output_dir / '/'.join(segments)


async def deep_crawl_docs(
    root_url: str,
    output_dir: str,
    max_depth: int = 2,
    max_pages: int = 50,
    url_pattern: str | None = None,
    keywords: list[str] | None = None,
    use_best_first: bool = True
) -> dict:
    """
    Deep crawl a documentation site and save pages as markdown.

    Args:
        root_url: Starting URL for the crawl
        output_dir: Directory to save markdown files
        max_depth: Maximum crawl depth (default: 2)
        max_pages: Maximum pages to crawl (default: 50)
        url_pattern: Optional URL pattern filter (e.g., "*docs*")
        keywords: Optional keywords for relevance scoring
        use_best_first: Use BestFirst strategy (True) or BFS (False)

    Returns:
        Dict with crawl statistics
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Extract domain for filtering
    parsed_root = urlparse(root_url)
    base_domain = parsed_root.netloc

    # Build filter chain
    filters = [
        DomainFilter(allowed_domains=[base_domain])
    ]

    if url_pattern:
        filters.append(URLPatternFilter(patterns=[url_pattern]))

    filter_chain = FilterChain(filters)

    # Choose strategy
    if use_best_first and keywords:
        scorer = KeywordRelevanceScorer(keywords=keywords, weight=0.8)
        strategy = BestFirstCrawlingStrategy(
            max_depth=max_depth,
            max_pages=max_pages,
            include_external=False,
            filter_chain=filter_chain,
            url_scorer=scorer
        )
    else:
        strategy = BFSDeepCrawlStrategy(
            max_depth=max_depth,
            max_pages=max_pages,
            include_external=False,
            filter_chain=filter_chain
        )

    browser_config = BrowserConfig()

    run_config = CrawlerRunConfig(
        deep_crawl_strategy=strategy,
        scraping_strategy=LXMLWebScrapingStrategy(),
        word_count_threshold=10,
        exclude_external_links=True,
        remove_overlay_elements=True,
        excluded_tags=['nav', 'footer', 'header', 'aside'],
        cache_mode=CacheMode.BYPASS,
        stream=True,
        verbose=True
    )

    stats = {
        'pages_crawled': 0,
        'pages_saved': 0,
        'pages_failed': 0,
        'files': [],
        'errors': []
    }

    async with AsyncWebCrawler(config=browser_config) as crawler:
        async for result in await crawler.arun(root_url, config=run_config):
            stats['pages_crawled'] += 1
            depth = result.metadata.get('depth', 0)
            score = result.metadata.get('score', 0)

            if result.success:
                # Get markdown content
                markdown = result.markdown.fit_markdown or result.markdown.raw_markdown
                title = result.metadata.get('title', 'Untitled')

                # Build output with metadata
                output = f"# {title}\n\n"
                output += f"- **Source:** {result.url}\n"
                output += f"- **Depth:** {depth}\n"
                if score:
                    output += f"- **Relevance Score:** {score:.2f}\n"
                output += f"- **Status:** {result.status_code}\n\n"
                output += "---\n\n"
                output += markdown

                # Determine file path preserving structure
                filepath = url_to_filepath(result.url, base_domain, output_path)
                filepath.parent.mkdir(parents=True, exist_ok=True)

                # Avoid overwriting
                if filepath.exists():
                    stem = filepath.stem
                    filepath = filepath.parent / f"{stem}-{stats['pages_crawled']}.md"

                filepath.write_text(output, encoding='utf-8')

                stats['pages_saved'] += 1
                stats['files'].append(str(filepath))

                print(f"[{stats['pages_crawled']}/{max_pages}] Depth {depth} | Score {score:.2f} | Saved: {filepath.name}", file=sys.stderr)

            else:
                stats['pages_failed'] += 1
                stats['errors'].append({
                    'url': result.url,
                    'error': result.error_message,
                    'depth': depth
                })
                print(f"[{stats['pages_crawled']}/{max_pages}] Depth {depth} | Failed: {result.url}", file=sys.stderr)

    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Deep crawl documentation sites and save as markdown'
    )
    parser.add_argument(
        'root_url',
        help='Root URL to start crawling from'
    )
    parser.add_argument(
        '-o', '--output-dir',
        required=True,
        help='Output directory for markdown files'
    )
    parser.add_argument(
        '-d', '--max-depth',
        type=int,
        default=2,
        help='Maximum crawl depth (default: 2)'
    )
    parser.add_argument(
        '-p', '--max-pages',
        type=int,
        default=50,
        help='Maximum pages to crawl (default: 50)'
    )
    parser.add_argument(
        '--pattern',
        help='URL pattern filter (e.g., "*docs*", "*tutorial*")'
    )
    parser.add_argument(
        '-k', '--keywords',
        nargs='+',
        help='Keywords for relevance scoring (enables BestFirst strategy)'
    )
    parser.add_argument(
        '--bfs',
        action='store_true',
        help='Use BFS strategy instead of BestFirst'
    )

    args = parser.parse_args()

    print(f"Starting deep crawl of {args.root_url}", file=sys.stderr)
    print(f"Max depth: {args.max_depth}, Max pages: {args.max_pages}", file=sys.stderr)

    try:
        stats = asyncio.run(deep_crawl_docs(
            root_url=args.root_url,
            output_dir=args.output_dir,
            max_depth=args.max_depth,
            max_pages=args.max_pages,
            url_pattern=args.pattern,
            keywords=args.keywords,
            use_best_first=not args.bfs
        ))

        # Summary
        print(f"\n{'='*50}", file=sys.stderr)
        print(f"Crawl Complete", file=sys.stderr)
        print(f"{'='*50}", file=sys.stderr)
        print(f"Pages crawled: {stats['pages_crawled']}", file=sys.stderr)
        print(f"Pages saved: {stats['pages_saved']}", file=sys.stderr)
        print(f"Pages failed: {stats['pages_failed']}", file=sys.stderr)
        print(f"Output directory: {args.output_dir}", file=sys.stderr)

        if stats['errors']:
            print(f"\nFailed URLs:", file=sys.stderr)
            for error in stats['errors'][:10]:
                print(f"  Depth {error['depth']}: {error['url']}", file=sys.stderr)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
