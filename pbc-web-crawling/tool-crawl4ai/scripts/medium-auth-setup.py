"""
Medium Authentication Setup for Crawl4AI

This script creates a persistent browser session for Medium.
Run once to log in manually, then reuse the session for authenticated crawls.

Usage:
    Step 1: Run this script to open browser and log in manually
    Step 2: Use medium_authenticated_crawl() for subsequent crawls
"""

import asyncio
import os
from pathlib import Path

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

# Persistent browser data directory
MEDIUM_PROFILE_DIR = Path(__file__).parent.parent / "browser-profiles" / "medium"


async def setup_medium_session():
    """
    Opens a visible browser for manual Medium login.
    Session data is saved to MEDIUM_PROFILE_DIR for reuse.
    """
    # Ensure profile directory exists
    MEDIUM_PROFILE_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Browser profile will be saved to: {MEDIUM_PROFILE_DIR}")
    print("\n" + "="*60)
    print("INSTRUCTIONS:")
    print("1. A browser window will open to Medium's login page")
    print("2. Log in with your Medium account (Google, email, etc.)")
    print("3. Once logged in and you see your feed, press ENTER here")
    print("="*60 + "\n")

    browser_config = BrowserConfig(
        headless=False,  # Visible browser for manual login
        use_persistent_context=True,
        user_data_dir=str(MEDIUM_PROFILE_DIR),
        viewport_width=1280,
        viewport_height=800,
        # Stealth settings to evade Cloudflare detection
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        headers={"Accept-Language": "en-US,en;q=0.9"},
        extra_args=[
            "--disable-blink-features=AutomationControlled",
        ],
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Navigate to Medium login with stealth settings
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            page_timeout=120000,  # 2 min timeout for login
            magic=True,  # Auto-handle common bot detection patterns
            simulate_user=True,  # Simulate human behavior
            override_navigator=True,  # Override navigator properties to hide automation
        )

        result = await crawler.arun("https://medium.com/m/signin", config=config)

        if result.success:
            print("\nBrowser opened to Medium login page.")
            print("Please log in now...")

            # Wait for user to complete login
            input("\nPress ENTER after you've logged in and see your Medium feed...")

            # Verify login by checking for authenticated content
            verify_config = CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS,
                wait_for="css:nav",  # Wait for navigation to load
            )

            verify_result = await crawler.arun("https://medium.com/", config=verify_config)

            if verify_result.success:
                print("\n✅ Session saved successfully!")
                print(f"   Profile location: {MEDIUM_PROFILE_DIR}")
                print("\nYou can now use medium_authenticated_crawl() for paywall content.")
            else:
                print("\n⚠️ Could not verify login. Try running setup again.")
        else:
            print(f"\n❌ Failed to open Medium: {result.error_message}")


async def medium_authenticated_crawl(url: str) -> str:
    """
    Crawl a Medium article using the saved authenticated session.

    Args:
        url: Medium article URL to crawl

    Returns:
        Full markdown content of the article
    """
    if not MEDIUM_PROFILE_DIR.exists():
        raise RuntimeError(
            "Medium session not found. Run setup_medium_session() first."
        )

    browser_config = BrowserConfig(
        headless=True,  # Headless for automated crawling
        use_persistent_context=True,
        user_data_dir=str(MEDIUM_PROFILE_DIR),
    )

    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        remove_overlay_elements=True,
        page_timeout=60000,
        # Focus on article content
        css_selector="article",
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawler_config)

        if result.success:
            return result.markdown
        else:
            raise RuntimeError(f"Crawl failed: {result.error_message}")


async def test_authenticated_crawl():
    """Test the authenticated session with a sample Medium article."""
    # Test URL - a known paywalled article
    test_url = "https://medium.com/"

    print(f"Testing authenticated crawl of: {test_url}")

    try:
        content = await medium_authenticated_crawl(test_url)
        print(f"\n✅ Successfully crawled! Content length: {len(content)} characters")
        print("\nFirst 500 characters:")
        print("-" * 40)
        print(content[:500])
    except RuntimeError as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Test mode: verify authentication works
        asyncio.run(test_authenticated_crawl())
    else:
        # Setup mode: open browser for manual login
        asyncio.run(setup_medium_session())
