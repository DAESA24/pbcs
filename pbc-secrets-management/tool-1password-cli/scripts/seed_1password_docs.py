"""
URL Seeding Script for 1Password CLI Documentation

Type: Maintenance
    This is a maintenance script for the PBC itself. Use it to refresh the local
    documentation corpus after 1Password CLI tool upgrades or when checking for
    new/updated documentation pages.

Purpose:
    Discovers all CLI documentation URLs from developer.1password.com using
    Crawl4AI's AsyncUrlSeeder. Outputs a JSON file for review before crawling.
    Run this as the first step when refreshing documentation, then follow up
    with crawl_1password_docs.py to fetch the actual content.

Usage:
    python seed_1password_docs.py

Output:
    ../docs/_url_discovery.json
"""

import asyncio
import json
from datetime import datetime
from pathlib import Path

from crawl4ai import AsyncUrlSeeder, SeedingConfig


async def discover_1password_cli_docs():
    """
    Discover 1Password CLI documentation URLs using sitemap seeding.

    Returns list of URLs with metadata and relevance scores.
    """

    # Keywords for relevance scoring - focused on security and CLI usage
    query_terms = (
        "secret credential security template privilege environment "
        "inject safe mask never expose hide protect command reference "
        "vault item read run signin authentication"
    )

    config = SeedingConfig(
        source="sitemap",           # Start with sitemap (fastest, official)
        pattern="*/docs/cli/*",     # Filter to CLI docs only
        extract_head=True,          # Get title, description metadata
        query=query_terms,          # For BM25 relevance scoring
        scoring_method="bm25",      # Content-based scoring
        score_threshold=0.0,        # Get all URLs, we'll filter manually
        max_urls=500,               # Reasonable limit for docs site
        concurrency=10,             # Parallel metadata extraction
        live_check=False,           # Skip accessibility check for speed
        verbose=True
    )

    print(f"Starting URL discovery for developer.1password.com/docs/cli")
    print(f"Query terms: {query_terms[:50]}...")

    discovered_urls = []

    async with AsyncUrlSeeder() as seeder:
        urls = await seeder.urls("developer.1password.com", config)

        print(f"\nDiscovered {len(urls)} URLs")

        for url_data in urls:
            url = url_data.get('url', '')
            head_data = url_data.get('head_data', {})

            discovered_urls.append({
                'url': url,
                'title': head_data.get('title', 'No title'),
                'description': head_data.get('meta', {}).get('description', ''),
                'relevance_score': url_data.get('relevance_score', 0),
                'status': url_data.get('status', 'unknown')
            })

    # Sort by relevance score descending
    discovered_urls.sort(key=lambda x: x['relevance_score'], reverse=True)

    return discovered_urls


def save_discovery_results(urls: list, output_path: Path):
    """Save discovered URLs to JSON for review."""

    output = {
        'discovered_at': datetime.now().isoformat(),
        'source': 'developer.1password.com',
        'pattern': '*/docs/cli/*',
        'total_urls': len(urls),
        'urls': urls
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2), encoding='utf-8')

    print(f"\nSaved {len(urls)} URLs to {output_path}")


def print_summary(urls: list):
    """Print summary of discovered URLs."""

    print(f"\n{'='*60}")
    print("URL DISCOVERY SUMMARY")
    print(f"{'='*60}")
    print(f"Total URLs discovered: {len(urls)}")

    # Show top 10 by relevance
    print(f"\nTop 10 by relevance score:")
    for i, url_data in enumerate(urls[:10], 1):
        score = url_data['relevance_score']
        title = url_data['title'][:50]
        print(f"  {i:2d}. [{score:.3f}] {title}")

    # Show score distribution
    high_relevance = len([u for u in urls if u['relevance_score'] >= 0.5])
    medium_relevance = len([u for u in urls if 0.2 <= u['relevance_score'] < 0.5])
    low_relevance = len([u for u in urls if u['relevance_score'] < 0.2])

    print(f"\nRelevance distribution:")
    print(f"  High (>=0.5):   {high_relevance}")
    print(f"  Medium (0.2-0.5): {medium_relevance}")
    print(f"  Low (<0.2):     {low_relevance}")


async def main():
    # Output path relative to script location
    script_dir = Path(__file__).parent
    output_path = script_dir.parent / "docs" / "_url_discovery.json"

    # Discover URLs
    urls = await discover_1password_cli_docs()

    # Save results
    save_discovery_results(urls, output_path)

    # Print summary
    print_summary(urls)

    print(f"\n{'='*60}")
    print("NEXT STEPS")
    print(f"{'='*60}")
    print(f"1. Review: {output_path}")
    print(f"2. Run crawl script: python crawl_1password_docs.py")


if __name__ == "__main__":
    asyncio.run(main())
