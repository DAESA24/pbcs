---
workflow_id: news-monitoring
title: "News and Article Monitoring"
abstraction_level: low
status: stub
version: "0.1.0"
created: 2025-12-08
last_updated: 2025-12-08
validated_by: []
use_cases:
  - "Track news coverage of a topic or company"
  - "Capture articles for research"
  - "Build corpus of press coverage"
  - "Monitor industry developments"
scripts_used:
  - batch_urls_to_markdown.py
  - url_to_markdown.py
estimated_duration: "Variable - depends on article count"
complexity: low
---

# News and Article Monitoring

- **Abstraction Level:** Low (decision tree)
- **Status:** Stub (not yet validated)
- **Last Updated:** 2025-12-08

## When to Use This Workflow

Use this workflow when you need to capture news articles or blog posts about a topic. This is appropriate for:

- Tracking press coverage of a company or topic
- Building a research corpus of articles
- Capturing announcements and news
- Monitoring industry trends

**Not suitable for:** Ongoing automated monitoring (this is manual/batch capture).

## Decision Tree

### Step 1: Identify Article Sources

**Where to find articles:**

- Company press/news page
- Google News search results
- Industry publication archives
- Blog aggregators

### Step 2: Choose Capture Method

- **Single article:** Use `url_to_markdown.py`
- **Multiple articles (known URLs):** Use `batch_urls_to_markdown.py`
- **News section of a site:** Use `deep_crawl_docs.py` with URL pattern filter

### Step 3: Handle Paywalled Content

- **Soft paywall (limited free articles):** May work with crawler
- **Hard paywall:** Won't work - note as "paywalled" in research
- **Registration wall:** May need browser profile with cookies

## Script Reference

| Script | When to Use | Key Parameters |
|--------|-------------|----------------|
| `url_to_markdown.py` | Single article | `[url] -o article.md` |
| `batch_urls_to_markdown.py` | Multiple known URLs | `--urls [url1] [url2] -o ./articles` |
| `deep_crawl_docs.py` | News section crawl | `--pattern "*news*" --max-pages 50` |

## Common Pitfalls

- **Paywalls:** Many news sites block content. Solution: Note paywalled articles, try alternative sources.
- **Dynamic content:** Article text loaded via JavaScript. Solution: Default crawler uses browser, should work.
- **Ads and noise:** Articles have lots of ads/related content. Solution: Rely on `fit_markdown` output which filters noise.
- **Date extraction:** Hard to get article dates consistently. Solution: Include URL in output, dates often in URL.

## Examples

### Example: Capture Single Article

```bash
PBC_VENV="C:/Users/drewa/pbcs/web-crawling-pbc/.venv/Scripts/python.exe"
PBC_SCRIPTS="C:/Users/drewa/pbcs/web-crawling-pbc/scripts"

"$PBC_VENV" "$PBC_SCRIPTS/url_to_markdown.py" \
    "https://techcrunch.com/2025/01/15/company-raises-funding" \
    --output "./articles/company-funding-announcement.md"
```

### Example: Batch Capture Multiple Articles

```bash
"$PBC_VENV" "$PBC_SCRIPTS/batch_urls_to_markdown.py" \
    --urls \
    "https://news-site.com/article-1" \
    "https://news-site.com/article-2" \
    "https://other-site.com/article-3" \
    --output-dir "./articles/topic-coverage"
```

### Example: Crawl Company News Section

```bash
"$PBC_VENV" "$PBC_SCRIPTS/deep_crawl_docs.py" \
    "https://company.com/news" \
    --output-dir "./articles/company-news" \
    --max-depth 2 \
    --max-pages 50 \
    --pattern "*news*"
```

## Output Organization

Organize articles by source or date:

```
articles/
├── by-source/
│   ├── techcrunch/
│   ├── reuters/
│   └── company-blog/
└── by-topic/
    ├── funding/
    ├── product-launches/
    └── partnerships/
```

## Metadata Tracking

Consider creating an index file:

```markdown
# Article Index

| Date | Title | Source | File |
|------|-------|--------|------|
| 2025-01-15 | Company Raises $50M | TechCrunch | techcrunch/funding.md |
| 2025-01-10 | New Product Launch | Company Blog | company-blog/launch.md |
```

## Related Documentation

- [Simple Crawling](../docs/02-crawl4ai-simple-crawling-2025-12-03.md)
- [Multi-URL Crawling](../docs/06-crawl4ai-multi-url-crawling-2025-12-03.md)

---

- **Document Status:** Stub
- **Next Review:** After first validation
