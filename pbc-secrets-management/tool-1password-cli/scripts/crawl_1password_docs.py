"""
Crawl Script for 1Password CLI Documentation

Type: Maintenance
    This is a maintenance script for the PBC itself. Use it after running
    seed_1password_docs.py to fetch and store documentation locally. Typically
    run after 1Password CLI tool upgrades to refresh the local docs corpus.

Purpose:
    Reads URLs from discovery JSON and crawls each page, saving as markdown
    files with YAML front matter. The front matter includes category, keywords,
    and relevance tags useful for search and RAG indexing.

    Includes URL filtering to exclude individual shell plugin pages while
    keeping overview/security documentation.

Usage:
    python crawl_1password_docs.py [--input discovery.json] [--output-dir ../docs]

Output:
    ../docs/*.md files with YAML front matter
"""

import argparse
import asyncio
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy


def should_include_url(url: str) -> bool:
    """
    Filter URLs to exclude individual shell plugin pages.

    Keeps:
    - All non-shell-plugin CLI docs
    - Shell plugins overview and conceptual pages

    Excludes:
    - Individual shell plugin integration pages (AWS, GitHub, etc.)
    """
    if '/shell-plugins/' not in url:
        return True

    # Shell plugin pages to keep (overview, security, conceptual)
    keep_patterns = [
        '/shell-plugins/$',              # Overview (trailing slash or end)
        '/shell-plugins/security',       # Security model
        '/shell-plugins/environments',   # Multi-environment guide
        '/shell-plugins/multiple-accounts',  # Multi-account guide
        '/shell-plugins/contribute',     # Build your own
        '/shell-plugins/troubleshooting',
        '/shell-plugins/test',
        '/shell-plugins/uninstall',
        '/shell-plugins/nix',            # NixOS configuration
    ]

    # Check if URL matches any keep pattern
    for pattern in keep_patterns:
        if pattern.endswith('$'):
            # Exact match for overview page
            if url.rstrip('/').endswith('/shell-plugins'):
                return True
        elif pattern in url:
            return True

    return False


def slugify(text: str) -> str:
    """Convert text to a safe filename slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = text.strip('-')
    return text[:60] or 'untitled'


def url_to_filename(url: str) -> str:
    """
    Convert URL to semantic filename.

    Examples:
        /docs/cli/get-started -> get-started.md
        /docs/cli/reference/commands/read -> cli-commands-read.md
        /docs/cli/secret-references -> secret-references.md
        /docs/cli/shell-plugins/ -> shell-plugins-overview.md
    """
    parsed = urlparse(url)
    path = parsed.path.strip('/')

    # Remove common prefixes
    path = re.sub(r'^docs/cli/?', '', path)

    if not path:
        return 'cli-overview.md'

    # Handle nested paths
    segments = [s for s in path.split('/') if s]

    if len(segments) == 1:
        if segments[0] == 'shell-plugins':
            return 'shell-plugins-overview.md'
        return f"{slugify(segments[0])}.md"
    elif 'reference' in segments and 'commands' in segments:
        # Command reference pages: reference/commands/read -> cli-commands-read.md
        cmd_name = segments[-1]
        return f"cli-commands-{slugify(cmd_name)}.md"
    elif 'reference' in segments:
        # Other reference pages
        return f"cli-reference-{slugify(segments[-1])}.md"
    elif 'shell-plugins' in segments:
        # Shell plugin conceptual pages
        plugin_page = segments[-1]
        return f"shell-plugins-{slugify(plugin_page)}.md"
    else:
        # Join with hyphens for other nested paths
        return f"{slugify('-'.join(segments))}.md"


def categorize_url(url: str, title: str) -> str:
    """
    Determine category based on URL and title.

    Categories: commands, security, concepts, best-practices, integrations
    """
    url_lower = url.lower()
    title_lower = title.lower()

    if '/commands/' in url_lower or 'command' in title_lower:
        return 'commands'
    elif any(term in url_lower or term in title_lower for term in
             ['secret', 'security', 'credential', 'protect', 'privilege']):
        return 'security'
    elif any(term in url_lower for term in ['run', 'inject', 'environment', 'shell-plugins']):
        return 'integrations'
    elif any(term in url_lower for term in ['get-started', 'install', 'setup']):
        return 'concepts'
    elif any(term in title_lower for term in ['best practice', 'pattern']):
        return 'best-practices'
    else:
        return 'concepts'


def extract_keywords(content: str, title: str) -> list:
    """Extract relevant keywords from content."""
    keywords = []

    # Check for common 1Password CLI terms
    terms_to_check = [
        'op://', 'vault', 'item', 'field', 'secret reference',
        'op read', 'op run', 'op item', 'op vault', 'op signin',
        'environment variable', 'service account', 'template',
        'biometric', 'authentication', 'session', 'ssh', 'ssh key'
    ]

    content_lower = content.lower()
    for term in terms_to_check:
        if term.lower() in content_lower:
            keywords.append(term)

    return keywords[:10]  # Limit to 10 keywords


def extract_relevance(content: str, title: str) -> list:
    """Extract use cases / relevance tags."""
    relevance = []

    use_cases = [
        ('secret retrieval', ['op read', 'secret reference', 'retrieve']),
        ('environment variables', ['environment', 'env var', 'op run']),
        ('script integration', ['script', 'automat', 'ci/cd', 'pipeline']),
        ('authentication', ['signin', 'auth', 'biometric', 'session']),
        ('item management', ['create item', 'edit item', 'delete item']),
        ('vault management', ['vault', 'permission', 'access']),
        ('security patterns', ['secure', 'protect', 'never expose', 'mask']),
        ('ssh keys', ['ssh', 'ssh key', 'ssh-agent']),
    ]

    content_lower = content.lower()
    for use_case, triggers in use_cases:
        if any(trigger in content_lower for trigger in triggers):
            relevance.append(use_case)

    return relevance[:5]  # Limit to 5


def build_yaml_front_matter(
    title: str,
    source_url: str,
    category: str,
    relevance: list,
    keywords: list
) -> str:
    """Build YAML front matter string."""

    today = date.today().isoformat()

    # Escape quotes in title
    title_escaped = title.replace('"', '\\"')

    # Format lists for YAML
    relevance_yaml = '\n'.join(f'  - {r}' for r in relevance) if relevance else '  - general'
    keywords_yaml = '\n'.join(f'  - {k}' for k in keywords) if keywords else '  - 1password-cli'

    return f"""---
title: "{title_escaped}"
source_url: "{source_url}"
captured: {today}
category: {category}
relevance:
{relevance_yaml}
keywords:
{keywords_yaml}
related: []
---

"""


async def crawl_urls(urls: list, output_dir: Path, concurrent: int = 5):
    """
    Crawl URLs and save as markdown with YAML front matter.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    browser_config = BrowserConfig()

    run_config = CrawlerRunConfig(
        scraping_strategy=LXMLWebScrapingStrategy(),
        word_count_threshold=10,
        exclude_external_links=True,
        remove_overlay_elements=True,
        excluded_tags=['nav', 'footer', 'header', 'aside'],
        cache_mode=CacheMode.BYPASS,
        verbose=False
    )

    stats = {
        'crawled': 0,
        'saved': 0,
        'failed': 0,
        'skipped': 0,
        'files': []
    }

    # Extract just URLs for crawling
    url_list = [u['url'] for u in urls]
    url_metadata = {u['url']: u for u in urls}

    print(f"Crawling {len(url_list)} URLs...")

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun_many(url_list, config=run_config)

        for result in results:
            stats['crawled'] += 1

            if result.success:
                url = result.url
                meta = url_metadata.get(url, {})

                # Get content
                markdown = result.markdown.fit_markdown or result.markdown.raw_markdown
                title = result.metadata.get('title', meta.get('title', 'Untitled'))

                # Generate metadata
                category = categorize_url(url, title)
                keywords = extract_keywords(markdown, title)
                relevance = extract_relevance(markdown, title)

                # Build front matter
                front_matter = build_yaml_front_matter(
                    title=title,
                    source_url=url,
                    category=category,
                    relevance=relevance,
                    keywords=keywords
                )

                # Build full document
                doc_content = front_matter + f"# {title}\n\n{markdown}"

                # Generate filename
                filename = url_to_filename(url)
                filepath = output_dir / filename

                # Avoid overwriting
                if filepath.exists():
                    stem = filepath.stem
                    filepath = output_dir / f"{stem}-{stats['crawled']}.md"

                filepath.write_text(doc_content, encoding='utf-8')

                stats['saved'] += 1
                stats['files'].append(str(filepath.name))

                print(f"  [{stats['crawled']}/{len(url_list)}] Saved: {filepath.name}")

            else:
                stats['failed'] += 1
                print(f"  [{stats['crawled']}/{len(url_list)}] Failed: {result.url}")

    return stats


def main():
    parser = argparse.ArgumentParser(
        description='Crawl 1Password CLI documentation'
    )
    parser.add_argument(
        '--input',
        default='../docs/_url_discovery.json',
        help='Path to URL discovery JSON'
    )
    parser.add_argument(
        '--output-dir',
        default='../docs',
        help='Output directory for markdown files'
    )
    parser.add_argument(
        '--concurrent',
        type=int,
        default=5,
        help='Concurrent crawl workers'
    )
    parser.add_argument(
        '--no-filter',
        action='store_true',
        help='Disable URL filtering (crawl all URLs)'
    )

    args = parser.parse_args()

    # Resolve paths relative to script
    script_dir = Path(__file__).parent
    input_path = script_dir / args.input
    output_dir = script_dir / args.output_dir

    # Load discovery data
    if not input_path.exists():
        print(f"Error: Discovery file not found: {input_path}")
        print("Run seed_1password_docs.py first")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        discovery_data = json.load(f)

    urls = discovery_data.get('urls', [])
    total_discovered = len(urls)

    # Apply URL filtering unless disabled
    if not args.no_filter:
        urls = [u for u in urls if should_include_url(u['url'])]
        filtered_count = total_discovered - len(urls)
        print(f"Filtered {filtered_count} shell plugin URLs")
        print(f"Crawling {len(urls)} of {total_discovered} discovered URLs")

    if not urls:
        print("No URLs to crawl")
        return

    # Run crawl
    stats = asyncio.run(crawl_urls(urls, output_dir, args.concurrent))

    # Summary
    print(f"\n{'='*60}")
    print("CRAWL COMPLETE")
    print(f"{'='*60}")
    print(f"URLs crawled: {stats['crawled']}")
    print(f"Files saved: {stats['saved']}")
    print(f"Failed: {stats['failed']}")
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    main()
