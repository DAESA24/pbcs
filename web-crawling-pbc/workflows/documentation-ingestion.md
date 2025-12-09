---
workflow_id: documentation-ingestion
title: "Documentation Ingestion for RAG"
abstraction_level: low
status: stub
version: "0.1.0"
created: 2025-12-08
last_updated: 2025-12-08
validated_by: []
use_cases:
  - "Ingest product documentation for semantic search"
  - "Build knowledge base from technical docs"
  - "Feed documentation into rag-pipeline PBC"
  - "Create local offline copy of documentation"
scripts_used:
  - deep_crawl_docs.py
  - batch_urls_to_markdown.py
estimated_duration: "30 min - 2 hours depending on site size"
complexity: low
---

# Documentation Ingestion for RAG

- **Abstraction Level:** Low (decision tree)
- **Status:** Stub (not yet validated)
- **Last Updated:** 2025-12-08

## When to Use This Workflow

Use this workflow when you need to crawl a documentation site and convert it to markdown for:

- Feeding into a RAG pipeline for semantic search
- Building a local knowledge base
- Creating offline documentation copies
- Preparing training data

## Decision Tree

### Step 1: Identify Documentation Site Type

**Check the URL structure and technology:**

- **If Docusaurus/GitBook/SPA (client-side routing):**
  - Detection: URLs like `/docs/intro`, content loads dynamically
  - Use: `batch_urls_to_markdown.py` with extracted doc URLs
  - Why: Deep crawl won't discover client-side routes

- **If traditional server-rendered docs:**
  - Detection: Each page has unique server path, links in HTML
  - Use: `deep_crawl_docs.py`
  - Params: `--max-depth 4 --max-pages 200`

- **If single-page reference (API docs, README):**
  - Use: `url_to_markdown.py`
  - Single file output

### Step 2: Choose Crawl Parameters

**For deep_crawl_docs.py:**

| Site Size | max-depth | max-pages | Notes |
|-----------|-----------|-----------|-------|
| Small (<50 pages) | 3 | 100 | Quick crawl |
| Medium (50-200 pages) | 4 | 300 | Standard docs |
| Large (200+ pages) | 5 | 500 | May need multiple runs |

**For batch_urls_to_markdown.py:**

1. Extract doc URLs from sitemap or main page links
2. Create URL list file or pass directly
3. Set `--concurrent 5` (default)

### Step 3: Handle Common Patterns

**Docusaurus Detection:**
```bash
# Check if site uses Docusaurus
curl -s https://docs.example.com | grep -i "docusaurus"
```

**Sitemap Extraction:**
```bash
# Try common sitemap locations
curl -s https://docs.example.com/sitemap.xml
curl -s https://docs.example.com/sitemap-0.xml
```

## Script Reference

| Script | When to Use | Key Parameters |
|--------|-------------|----------------|
| `deep_crawl_docs.py` | Traditional server-rendered docs | `--max-depth 4 --max-pages 200` |
| `batch_urls_to_markdown.py` | SPA docs, known URL list | `--urls [list] -o ./output` |
| `url_to_markdown.py` | Single page/README | `[url] -o file.md` |

## Common Pitfalls

- **SPA/Docusaurus sites:** Deep crawl returns few files despite large docs. Solution: Extract URLs from sitemap or main page, use batch crawl.
- **Rate limiting:** Some doc sites rate limit. Solution: Reduce `--concurrent` to 2-3.
- **Versioned docs:** May crawl old versions. Solution: Add version to URL pattern filter.
- **Large sites timeout:** Solution: Run in phases by section, or increase `--max-pages`.

## Examples

### Example: Traditional Documentation Site

```bash
PBC_VENV="C:/Users/drewa/pbcs/web-crawling-pbc/.venv/Scripts/python.exe"
PBC_SCRIPTS="C:/Users/drewa/pbcs/web-crawling-pbc/scripts"

"$PBC_VENV" "$PBC_SCRIPTS/deep_crawl_docs.py" \
    "https://docs.example.com" \
    --output-dir "./docs-output" \
    --max-depth 4 \
    --max-pages 200
```

### Example: Docusaurus Site (Batch Approach)

```bash
# First, extract URLs from sitemap
curl -s https://docs.example.com/sitemap.xml | grep -oP '(?<=<loc>)[^<]+' > urls.txt

# Then batch crawl
"$PBC_VENV" "$PBC_SCRIPTS/batch_urls_to_markdown.py" \
    urls.txt \
    --output-dir "./docs-output"
```

### Example: Single API Reference

```bash
"$PBC_VENV" "$PBC_SCRIPTS/url_to_markdown.py" \
    "https://api.example.com/reference" \
    --output api-reference.md
```

## Output Structure

```
docs-output/
├── index.md
├── getting-started.md
├── api/
│   ├── overview.md
│   └── endpoints.md
└── guides/
    ├── tutorial-1.md
    └── tutorial-2.md
```

## Related Documentation

- [Deep Crawling](../docs/07-crawl4ai-deep-crawling-2025-12-03.md)
- [Multi-URL Crawling](../docs/06-crawl4ai-multi-url-crawling-2025-12-03.md)

---

- **Document Status:** Stub
- **Next Review:** After first validation
