"""
Batch SPA URL to Markdown converter using Crawl4AI.

Specialized script for crawling Single Page Applications (SPAs) that have
client-side routing issues, such as React/Vue apps where direct URL access
may render incorrect content.

Key features:
- Session-based navigation: initializes SPA router first, then navigates
- Uses js_only mode to navigate without full page reloads
- Custom JavaScript wait conditions that verify page-specific content
- Sequential processing to avoid SPA routing race conditions
- Longer delays and timeouts for React/Vue hydration
- Content validation to detect routing failures

Usage:
    python batch_spa_to_markdown.py --urls <url1> <url2> ... --output-dir <directory>
    python batch_spa_to_markdown.py <urls_file> --output-dir <directory>

Examples:
    # Notion API docs (known SPA routing issues)
    python batch_spa_to_markdown.py --urls https://developers.notion.com/reference/post-database-query -o ./output

    # Specify an init URL to bootstrap the SPA router
    python batch_spa_to_markdown.py urls.txt -o ./output --init-url https://developers.notion.com/reference/intro
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


# URL-to-expected-content mapping for SPA validation
# Maps URL path patterns to expected H1 text or content markers
SPA_CONTENT_VALIDATORS = {
    # Notion API database/data_source endpoints (known problematic pages)
    'post-database-query': ['query', 'database'],
    'query-a-data-source': ['query', 'data source'],
    'retrieve-a-data-source': ['retrieve', 'data source'],
    'retrieve-a-database': ['retrieve', 'database'],
    'create-a-data-source': ['create', 'data source'],
    # Add more patterns as needed
}


def slugify(text: str) -> str:
    """Convert text to a safe filename slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = text.strip('-')
    return text[:60] or 'untitled'


def get_filename_from_url(url: str) -> str:
    """Generate filename from URL path (not page title)."""
    parsed = urlparse(url)
    # Get last path segment
    path_parts = [p for p in parsed.path.strip('/').split('/') if p]
    if path_parts:
        return f"{path_parts[-1]}.md"
    return f"{slugify(parsed.netloc)}.md"


def get_content_validator_for_url(url: str) -> list[str] | None:
    """Get expected content keywords for a URL."""
    url_lower = url.lower()
    for pattern, keywords in SPA_CONTENT_VALIDATORS.items():
        if pattern in url_lower:
            return keywords
    return None


def build_spa_wait_condition(url: str) -> str:
    """
    Build a JavaScript wait condition that verifies the SPA has rendered
    the correct content for the requested URL.

    This is crucial for React/Vue SPAs where client-side routing may
    render the wrong page content when accessing URLs directly.
    """
    validators = get_content_validator_for_url(url)

    if validators:
        # Build condition that checks H1 contains expected keywords
        keyword_checks = ' && '.join([
            f"h1Text.includes('{kw}')" for kw in validators
        ])

        return f"""js:() => {{
            const h1 = document.querySelector('h1');
            if (!h1) return false;
            const h1Text = h1.textContent.toLowerCase();
            return {keyword_checks};
        }}"""

    # Default: wait for any H1 to appear
    return "js:() => document.querySelector('h1') !== null"


def validate_content(markdown: str, url: str) -> tuple[bool, str]:
    """
    Validate that crawled content matches expected content for the URL.
    Returns (is_valid, reason).
    """
    validators = get_content_validator_for_url(url)

    if not validators:
        return True, "No validation rules for this URL"

    markdown_lower = markdown.lower()
    missing = [kw for kw in validators if kw not in markdown_lower]

    if missing:
        return False, f"Missing expected content: {missing}"

    return True, "Content validated successfully"


async def initialize_spa_session(
    crawler,
    init_url: str,
    session_id: str
) -> bool:
    """
    Initialize the SPA by loading a known-working page first.
    This bootstraps the React/Vue router before navigating to target URLs.

    Returns True if initialization succeeded.
    """
    print(f"Initializing SPA session at: {init_url}", file=sys.stderr)

    init_config = CrawlerRunConfig(
        session_id=session_id,
        wait_until="networkidle",
        delay_before_return_html=3.0,
        cache_mode=CacheMode.BYPASS,
        magic=True
    )

    result = await crawler.arun(init_url, config=init_config)

    if result.success:
        title = result.metadata.get('title', 'Unknown')
        print(f"  SPA initialized: {title}", file=sys.stderr)
        return True
    else:
        print(f"  WARNING: SPA init failed: {result.error_message}", file=sys.stderr)
        return False


async def crawl_spa_url(
    crawler,
    url: str,
    output_dir: Path,
    delay: float,
    validate: bool,
    index: int,
    total: int,
    session_id: str,
    use_session_nav: bool = True
) -> dict:
    """
    Crawl a single SPA URL with session-based navigation and content validation.

    When use_session_nav is True, uses js_only mode to navigate the SPA
    without a full page reload, which avoids client-side routing issues.

    Returns dict with 'success', 'url', 'file' or 'error', 'validation'.
    """
    print(f"[{index}/{total}] Crawling: {url}", file=sys.stderr)

    if use_session_nav:
        # Session-based navigation: use JS to navigate within existing session
        config = CrawlerRunConfig(
            session_id=session_id,
            js_only=True,  # KEY: Don't reload page, navigate via JS
            js_code=f"window.location.href = '{url}';",

            # Content settings
            word_count_threshold=10,
            exclude_external_links=True,
            excluded_tags=['nav', 'footer', 'header', 'aside'],
            cache_mode=CacheMode.BYPASS,

            # Wait for content to render
            wait_until="networkidle",
            delay_before_return_html=delay,
            wait_for="js:() => document.querySelector('h1') !== null",
            wait_for_timeout=20000,

            # Page interaction
            page_timeout=60000,
        )
        print(f"  Mode: session-based navigation (js_only)", file=sys.stderr)
    else:
        # Direct URL access (fallback)
        wait_condition = build_spa_wait_condition(url)
        config = CrawlerRunConfig(
            session_id=session_id,

            # Content settings
            word_count_threshold=10,
            exclude_external_links=True,
            excluded_tags=['nav', 'footer', 'header', 'aside'],
            cache_mode=CacheMode.BYPASS,

            # SPA-specific settings
            wait_until="networkidle",
            scan_full_page=True,
            delay_before_return_html=delay,
            magic=True,

            # Custom wait condition for content verification
            wait_for=wait_condition,
            wait_for_timeout=30000,

            # Page interaction
            page_timeout=60000,
        )
        print(f"  Mode: direct URL access", file=sys.stderr)

    result = await crawler.arun(url=url, config=config)

    if not result.success:
        return {
            'success': False,
            'url': url,
            'error': result.error_message,
            'validation': None
        }

    # Get markdown content
    markdown = result.markdown.fit_markdown or result.markdown.raw_markdown
    title = result.metadata.get('title', 'Untitled')

    # Validate content if requested
    validation_result = None
    if validate:
        is_valid, reason = validate_content(markdown, url)
        validation_result = {'valid': is_valid, 'reason': reason}

        if not is_valid:
            print(f"  WARNING: Content validation failed - {reason}", file=sys.stderr)

    # Build output with metadata
    output = f"# {title}\n\n"
    output += f"- **Source:** {url}\n"
    output += f"- **Status:** {result.status_code}\n"
    if validation_result:
        status = "PASS" if validation_result['valid'] else "FAIL"
        output += f"- **Validation:** {status}\n"
    output += "\n---\n\n"
    output += markdown

    # Save to file (use URL-based filename, not title)
    filename = get_filename_from_url(url)
    filepath = output_dir / filename

    # Avoid overwriting
    if filepath.exists():
        stem = filepath.stem
        filepath = output_dir / f"{stem}-{index}.md"

    filepath.write_text(output, encoding='utf-8')

    print(f"  Saved: {filename} ({len(markdown)} chars)", file=sys.stderr)

    return {
        'success': True,
        'url': url,
        'file': str(filepath),
        'title': title,
        'validation': validation_result
    }


def derive_init_url(urls: list[str]) -> str | None:
    """
    Derive a suitable SPA initialization URL from the target URLs.
    Looks for a common base path and finds a likely "intro" or "index" page.
    """
    if not urls:
        return None

    # Parse first URL to get domain
    parsed = urlparse(urls[0])
    base = f"{parsed.scheme}://{parsed.netloc}"

    # Common patterns for SPA init pages
    path_parts = parsed.path.strip('/').split('/')

    if len(path_parts) >= 2:
        # Try to find intro/index page at same level
        parent_path = '/'.join(path_parts[:-1])
        candidates = [
            f"{base}/{parent_path}/intro",
            f"{base}/{parent_path}",
            f"{base}/{path_parts[0]}/intro",
            f"{base}/{path_parts[0]}",
        ]
        return candidates[0]

    return f"{base}/"


async def batch_spa_to_markdown(
    urls: list[str],
    output_dir: str,
    init_url: str = None,
    delay: float = 3.0,
    validate: bool = True,
    inter_request_delay: float = 2.0
) -> dict:
    """
    Convert multiple SPA URLs to markdown files using session-based navigation.

    Initializes the SPA router first by loading an init_url, then navigates
    to each target URL using js_only mode to avoid routing issues.

    Args:
        urls: List of URLs to crawl
        output_dir: Directory to save markdown files
        init_url: URL to load first to initialize SPA router (auto-derived if None)
        delay: Delay before capturing content (default: 3.0s for SPAs)
        validate: Enable content validation
        inter_request_delay: Delay between requests (default: 2.0s)

    Returns:
        Dict with 'successful', 'failed', and 'validation_failures' lists
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Derive init URL if not provided
    if not init_url:
        init_url = derive_init_url(urls)
        print(f"Auto-derived init URL: {init_url}", file=sys.stderr)

    browser_config = BrowserConfig(
        headless=True,
        verbose=False
    )

    results = {
        'successful': [],
        'failed': [],
        'validation_failures': []
    }

    session_id = "spa_batch_session"

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Initialize SPA session first
        if init_url:
            init_success = await initialize_spa_session(crawler, init_url, session_id)
            if not init_success:
                print("WARNING: SPA initialization failed, falling back to direct access", file=sys.stderr)

        # Crawl each URL using session navigation
        for index, url in enumerate(urls, 1):
            try:
                result = await crawl_spa_url(
                    crawler=crawler,
                    url=url,
                    output_dir=output_path,
                    delay=delay,
                    validate=validate,
                    index=index,
                    total=len(urls),
                    session_id=session_id,
                    use_session_nav=True  # Use session-based navigation
                )

                if result['success']:
                    results['successful'].append(result)

                    # Track validation failures separately
                    if result.get('validation') and not result['validation']['valid']:
                        results['validation_failures'].append(result)
                else:
                    results['failed'].append(result)

            except Exception as e:
                results['failed'].append({
                    'success': False,
                    'url': url,
                    'error': str(e),
                    'validation': None
                })
                print(f"  ERROR: {e}", file=sys.stderr)

            # Delay between requests to let SPA state settle
            if index < len(urls):
                await asyncio.sleep(inter_request_delay)

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
        description='Convert SPA URLs to markdown with session-based navigation (Crawl4AI)'
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
        '--init-url',
        help='URL to load first to initialize SPA router (auto-derived if not provided)'
    )
    parser.add_argument(
        '--delay',
        type=float,
        default=3.0,
        help='Delay before capturing content (default: 3.0s for SPAs)'
    )
    parser.add_argument(
        '--inter-delay',
        type=float,
        default=2.0,
        help='Delay between requests (default: 2.0s)'
    )
    parser.add_argument(
        '--validate-content',
        action='store_true',
        default=True,
        help='Enable content validation (default: True)'
    )
    parser.add_argument(
        '--no-validate',
        action='store_true',
        help='Disable content validation'
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

    validate = not args.no_validate

    print(f"SPA Batch Crawler (Session-Based Navigation)", file=sys.stderr)
    print(f"  URLs: {len(urls)}", file=sys.stderr)
    print(f"  Init URL: {args.init_url or '(auto-derived)'}", file=sys.stderr)
    print(f"  Delay: {args.delay}s", file=sys.stderr)
    print(f"  Inter-request delay: {args.inter_delay}s", file=sys.stderr)
    print(f"  Content validation: {validate}", file=sys.stderr)
    print(f"  Output: {args.output_dir}", file=sys.stderr)
    print("", file=sys.stderr)

    try:
        results = asyncio.run(batch_spa_to_markdown(
            urls=urls,
            output_dir=args.output_dir,
            init_url=args.init_url,
            delay=args.delay,
            validate=validate,
            inter_request_delay=args.inter_delay
        ))

        # Summary
        print("", file=sys.stderr)
        print(f"Results:", file=sys.stderr)
        print(f"  Successful: {len(results['successful'])}", file=sys.stderr)
        print(f"  Failed: {len(results['failed'])}", file=sys.stderr)

        if validate:
            print(f"  Validation failures: {len(results['validation_failures'])}", file=sys.stderr)

        if results['failed']:
            print("\nFailed URLs:", file=sys.stderr)
            for failure in results['failed']:
                print(f"  {failure['url']}: {failure['error']}", file=sys.stderr)

        if results['validation_failures']:
            print("\nValidation failures (content may be wrong):", file=sys.stderr)
            for failure in results['validation_failures']:
                reason = failure['validation']['reason']
                print(f"  {failure['url']}: {reason}", file=sys.stderr)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
