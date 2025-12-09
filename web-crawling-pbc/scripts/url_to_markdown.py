"""
URL to Markdown converter using Crawl4AI.

Converts a single URL to clean markdown output.

Usage:
    python url_to_markdown.py <url> [--output <file>]

Examples:
    python url_to_markdown.py https://example.com
    python url_to_markdown.py https://example.com --output article.md
    python url_to_markdown.py https://example.com -o -  # stdout
"""

import argparse
import asyncio
import sys
from pathlib import Path

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


async def url_to_markdown(url: str, output_path: str | None = None) -> str:
    """
    Convert a URL to clean markdown.

    Args:
        url: The URL to crawl
        output_path: Optional file path to save output (None = return string)

    Returns:
        The markdown content as a string
    """
    browser_config = BrowserConfig()

    run_config = CrawlerRunConfig(
        word_count_threshold=10,
        exclude_external_links=True,
        remove_overlay_elements=True,
        excluded_tags=['nav', 'footer', 'header', 'aside'],
        cache_mode=CacheMode.BYPASS
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=run_config)

        if not result.success:
            raise RuntimeError(f"Crawl failed: {result.error_message}")

        # Get the filtered markdown (cleaner) or fall back to raw
        markdown = result.markdown.fit_markdown or result.markdown.raw_markdown

        # Add metadata header
        title = result.metadata.get('title', 'Untitled')
        output = f"# {title}\n\n"
        output += f"- **Source:** {url}\n"
        output += f"- **Status:** {result.status_code}\n\n"
        output += "---\n\n"
        output += markdown

        if output_path and output_path != '-':
            Path(output_path).write_text(output, encoding='utf-8')
            print(f"Saved to: {output_path}", file=sys.stderr)

        return output


def main():
    parser = argparse.ArgumentParser(
        description='Convert a URL to clean markdown using Crawl4AI'
    )
    parser.add_argument('url', help='URL to convert')
    parser.add_argument(
        '-o', '--output',
        help='Output file path (use - for stdout, omit to print to stdout)',
        default='-'
    )

    args = parser.parse_args()

    try:
        result = asyncio.run(url_to_markdown(args.url, args.output))

        if args.output == '-':
            print(result)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
