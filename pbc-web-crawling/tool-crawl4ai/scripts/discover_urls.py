"""
URL Discovery using Crawl4AI's URL Seeder.

Discovers URLs from sitemaps and/or Common Crawl before crawling.
Use this to find all relevant pages on a documentation site, then
pipe the output to batch_urls_to_markdown.py for conversion.

Usage:
    python discover_urls.py <domain> [options]

Examples:
    # Discover all docs pages from sitemap
    python discover_urls.py developers.notion.com --pattern "*/docs/*"

    # Discover with relevance scoring
    python discover_urls.py docs.python.org --query "async await tutorial" --threshold 0.3

    # Output to file for batch processing
    python discover_urls.py example.com --pattern "*/blog/*" -o urls.txt

    # Use Common Crawl for comprehensive discovery
    python discover_urls.py example.com --source cc --max-urls 1000
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

from crawl4ai import AsyncUrlSeeder, SeedingConfig


async def discover_urls(
    domain: str,
    source: str = "sitemap",
    pattern: str = "*",
    query: str = None,
    score_threshold: float = 0.0,
    max_urls: int = 500,
    extract_metadata: bool = False,
    live_check: bool = False,
    verbose: bool = False
) -> list[dict]:
    """
    Discover URLs from a domain using sitemap and/or Common Crawl.

    Args:
        domain: Domain to discover URLs from (e.g., "docs.example.com")
        source: Data source - "sitemap", "cc", or "sitemap+cc"
        pattern: URL pattern filter (e.g., "*/docs/*", "*.html")
        query: Search query for BM25 relevance scoring
        score_threshold: Minimum relevance score (0.0-1.0)
        max_urls: Maximum URLs to return
        extract_metadata: Extract <head> metadata (slower but more info)
        live_check: Verify URLs are accessible (slower)
        verbose: Print progress messages

    Returns:
        List of URL dictionaries with 'url', 'status', and optionally 'relevance_score'
    """
    config_kwargs = {
        "source": source,
        "pattern": pattern,
        "max_urls": max_urls,
        "extract_head": extract_metadata,
        "live_check": live_check,
        "verbose": verbose,
        "filter_nonsense_urls": True
    }

    # Add relevance scoring if query provided
    if query:
        config_kwargs["query"] = query
        config_kwargs["scoring_method"] = "bm25"
        if score_threshold > 0:
            config_kwargs["score_threshold"] = score_threshold

    config = SeedingConfig(**config_kwargs)

    async with AsyncUrlSeeder() as seeder:
        if verbose:
            print(f"Discovering URLs from {domain}...", file=sys.stderr)
            print(f"  Source: {source}", file=sys.stderr)
            print(f"  Pattern: {pattern}", file=sys.stderr)
            if query:
                print(f"  Query: {query}", file=sys.stderr)

        urls = await seeder.urls(domain, config)

        if verbose:
            print(f"  Found: {len(urls)} URLs", file=sys.stderr)

        return urls


def format_output(urls: list[dict], output_format: str, include_metadata: bool) -> str:
    """Format URLs for output."""
    if output_format == "json":
        return json.dumps(urls, indent=2)

    elif output_format == "urls":
        # Plain URL list (one per line) - for piping to batch script
        return "\n".join(url["url"] for url in urls)

    elif output_format == "table":
        # Human-readable table format
        lines = []
        lines.append(f"{'#':>4}  {'Score':>6}  URL")
        lines.append("-" * 80)

        for i, url in enumerate(urls, 1):
            score = url.get("relevance_score", "-")
            if isinstance(score, float):
                score = f"{score:.3f}"
            lines.append(f"{i:4d}  {score:>6}  {url['url']}")

        return "\n".join(lines)

    else:
        return "\n".join(url["url"] for url in urls)


def main():
    parser = argparse.ArgumentParser(
        description="Discover URLs from a domain using sitemap and/or Common Crawl",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Discover docs pages from sitemap
  python discover_urls.py developers.notion.com --pattern "*/docs/*"

  # Find tutorials with relevance scoring
  python discover_urls.py docs.python.org --query "async tutorial" --threshold 0.3

  # Save to file for batch processing
  python discover_urls.py example.com -o urls.txt

  # Pipe to batch converter
  python discover_urls.py example.com --format urls | xargs python batch_urls_to_markdown.py --urls
"""
    )

    parser.add_argument(
        "domain",
        help="Domain to discover URLs from (e.g., 'docs.example.com')"
    )

    parser.add_argument(
        "--source", "-s",
        choices=["sitemap", "cc", "sitemap+cc"],
        default="sitemap",
        help="Data source: sitemap (fast), cc (Common Crawl, comprehensive), sitemap+cc (both)"
    )

    parser.add_argument(
        "--pattern", "-p",
        default="*",
        help="URL pattern filter (e.g., '*/docs/*', '*.html')"
    )

    parser.add_argument(
        "--query", "-q",
        help="Search query for BM25 relevance scoring"
    )

    parser.add_argument(
        "--threshold", "-t",
        type=float,
        default=0.0,
        help="Minimum relevance score threshold (0.0-1.0)"
    )

    parser.add_argument(
        "--max-urls", "-m",
        type=int,
        default=500,
        help="Maximum URLs to return (default: 500)"
    )

    parser.add_argument(
        "--metadata",
        action="store_true",
        help="Extract <head> metadata (slower but provides titles/descriptions)"
    )

    parser.add_argument(
        "--live-check",
        action="store_true",
        help="Verify URLs are accessible (slower)"
    )

    parser.add_argument(
        "--format", "-f",
        choices=["urls", "json", "table"],
        default="table",
        help="Output format: urls (plain list), json (full data), table (human-readable)"
    )

    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: stdout)"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print progress to stderr"
    )

    args = parser.parse_args()

    try:
        urls = asyncio.run(discover_urls(
            domain=args.domain,
            source=args.source,
            pattern=args.pattern,
            query=args.query,
            score_threshold=args.threshold,
            max_urls=args.max_urls,
            extract_metadata=args.metadata,
            live_check=args.live_check,
            verbose=args.verbose
        ))

        if not urls:
            print("No URLs found matching criteria", file=sys.stderr)
            sys.exit(1)

        output = format_output(urls, args.format, args.metadata)

        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
            print(f"Saved {len(urls)} URLs to {args.output}", file=sys.stderr)
        else:
            print(output)

        # Summary to stderr
        if args.verbose or args.format == "table":
            print(f"\nTotal: {len(urls)} URLs discovered", file=sys.stderr)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
