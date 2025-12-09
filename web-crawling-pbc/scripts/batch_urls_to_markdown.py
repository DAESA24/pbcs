"""
Batch URL to Markdown converter using Crawl4AI.

Converts multiple URLs to markdown files with concurrent processing.

Usage:
    python batch_urls_to_markdown.py <urls_file> --output-dir <directory>
    python batch_urls_to_markdown.py --urls <url1> <url2> ... --output-dir <directory>

Examples:
    python batch_urls_to_markdown.py urls.txt --output-dir ./output
    python batch_urls_to_markdown.py --urls https://a.com https://b.com -o ./output
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai import MemoryAdaptiveDispatcher, RateLimiter


def slugify(text: str) -> str:
    """Convert text to a safe filename slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = text.strip('-')
    return text[:60] or 'untitled'


def get_filename_from_result(result, index: int) -> str:
    """Generate a filename from crawl result."""
    title = result.metadata.get('title', '')
    if title:
        return f"{slugify(title)}.md"

    # Fall back to URL path
    parsed = urlparse(result.url)
    path_slug = slugify(parsed.path) or slugify(parsed.netloc)
    return f"{path_slug}-{index}.md"


async def batch_urls_to_markdown(
    urls: list[str],
    output_dir: str,
    max_concurrent: int = 5
) -> dict:
    """
    Convert multiple URLs to markdown files.

    Args:
        urls: List of URLs to crawl
        output_dir: Directory to save markdown files
        max_concurrent: Maximum concurrent crawls

    Returns:
        Dict with 'successful' and 'failed' lists
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    browser_config = BrowserConfig()

    run_config = CrawlerRunConfig(
        word_count_threshold=10,
        exclude_external_links=True,
        remove_overlay_elements=True,
        excluded_tags=['nav', 'footer', 'header', 'aside'],
        cache_mode=CacheMode.BYPASS,
        stream=True
    )

    rate_limiter = RateLimiter(
        base_delay=(0.5, 1.5),
        max_delay=30.0,
        max_retries=2
    )

    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=80.0,
        max_session_permit=max_concurrent,
        rate_limiter=rate_limiter
    )

    results = {'successful': [], 'failed': []}

    async with AsyncWebCrawler(config=browser_config) as crawler:
        index = 0
        async for result in await crawler.arun_many(
            urls=urls,
            config=run_config,
            dispatcher=dispatcher
        ):
            index += 1

            if result.success:
                # Get markdown content
                markdown = result.markdown.fit_markdown or result.markdown.raw_markdown
                title = result.metadata.get('title', 'Untitled')

                # Build output with metadata
                output = f"# {title}\n\n"
                output += f"- **Source:** {result.url}\n"
                output += f"- **Status:** {result.status_code}\n\n"
                output += "---\n\n"
                output += markdown

                # Save to file
                filename = get_filename_from_result(result, index)
                filepath = output_path / filename

                # Avoid overwriting
                if filepath.exists():
                    stem = filepath.stem
                    filepath = output_path / f"{stem}-{index}.md"

                filepath.write_text(output, encoding='utf-8')

                results['successful'].append({
                    'url': result.url,
                    'file': str(filepath),
                    'title': title
                })
                print(f"[{index}/{len(urls)}] Saved: {filename}", file=sys.stderr)

            else:
                results['failed'].append({
                    'url': result.url,
                    'error': result.error_message
                })
                print(f"[{index}/{len(urls)}] Failed: {result.url} - {result.error_message}", file=sys.stderr)

    return results


def load_urls_from_file(filepath: str) -> list[str]:
    """Load URLs from a text file (one per line)."""
    urls = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                urls.append(line)
    return urls


def main():
    parser = argparse.ArgumentParser(
        description='Convert multiple URLs to markdown files using Crawl4AI'
    )
    parser.add_argument(
        'urls_file',
        nargs='?',
        help='Text file containing URLs (one per line)'
    )
    parser.add_argument(
        '--urls',
        nargs='+',
        help='URLs to convert (alternative to file)'
    )
    parser.add_argument(
        '-o', '--output-dir',
        required=True,
        help='Output directory for markdown files'
    )
    parser.add_argument(
        '-c', '--concurrent',
        type=int,
        default=5,
        help='Maximum concurrent crawls (default: 5)'
    )

    args = parser.parse_args()

    # Get URLs from file or command line
    if args.urls_file:
        urls = load_urls_from_file(args.urls_file)
    elif args.urls:
        urls = args.urls
    else:
        parser.error('Either urls_file or --urls is required')

    if not urls:
        print("No URLs provided", file=sys.stderr)
        sys.exit(1)

    print(f"Processing {len(urls)} URLs...", file=sys.stderr)

    try:
        results = asyncio.run(batch_urls_to_markdown(
            urls=urls,
            output_dir=args.output_dir,
            max_concurrent=args.concurrent
        ))

        # Summary
        print(f"\nCompleted: {len(results['successful'])} successful, {len(results['failed'])} failed", file=sys.stderr)

        if results['failed']:
            print("\nFailed URLs:", file=sys.stderr)
            for failure in results['failed']:
                print(f"  {failure['url']}: {failure['error']}", file=sys.stderr)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
