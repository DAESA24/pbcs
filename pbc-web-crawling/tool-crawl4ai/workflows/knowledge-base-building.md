---
workflow_id: knowledge-base-building
title: "Knowledge Base Building"
abstraction_level: low
status: stub
version: "0.1.0"
created: 2025-12-08
last_updated: 2025-12-08
validated_by: []
use_cases:
  - "Build reference collection on a topic"
  - "Curate learning resources"
  - "Create research corpus"
  - "Gather training data"
scripts_used:
  - url_to_markdown.py
  - batch_urls_to_markdown.py
  - deep_crawl_docs.py
estimated_duration: "Ongoing - incremental additions"
complexity: low
---

# Knowledge Base Building

- **Abstraction Level:** Low (decision tree)
- **Status:** Stub (not yet validated)
- **Last Updated:** 2025-12-08

## When to Use This Workflow

Use this workflow when you're building a collection of reference materials over time. This is appropriate for:

- Curating learning resources on a topic
- Building a personal knowledge base
- Gathering reference materials for a project
- Creating a corpus for RAG or training

**Key difference from other workflows:** This is incremental and ongoing, not a one-time research project.

## Decision Tree

### Step 1: Define Knowledge Base Structure

Before adding content, establish organization:

```
knowledge-base/
├── [topic-1]/
│   ├── articles/
│   ├── documentation/
│   └── tutorials/
├── [topic-2]/
│   └── ...
└── index.md
```

### Step 2: Choose Capture Method by Content Type

| Content Type | Script | Notes |
|--------------|--------|-------|
| Single article/page | `url_to_markdown.py` | Quick capture |
| Tutorial series | `batch_urls_to_markdown.py` | All parts at once |
| Full documentation | `deep_crawl_docs.py` | Comprehensive capture |
| Reference page | `url_to_markdown.py` | Single file |

### Step 3: Maintain Index

Keep an index file updated with what's been captured:

```markdown
# Knowledge Base Index

## Topic: [Topic Name]

### Articles
- [Title](path/to/file.md) - captured 2025-01-15

### Documentation
- [Product Docs](path/to/docs/) - 50 files, captured 2025-01-10
```

## Script Reference

| Script | When to Use | Key Parameters |
|--------|-------------|----------------|
| `url_to_markdown.py` | Single page capture | `[url] -o ./kb/topic/file.md` |
| `batch_urls_to_markdown.py` | Multiple related pages | `--urls [urls] -o ./kb/topic/` |
| `deep_crawl_docs.py` | Full site/section | `--max-depth 3 -o ./kb/topic/` |

## Common Pitfalls

- **No organization:** Dumping files without structure. Solution: Define structure first, organize as you capture.
- **Duplicate content:** Capturing same content twice. Solution: Check index before adding.
- **Stale content:** Old captures become outdated. Solution: Note capture date, re-crawl periodically.
- **Too much noise:** Capturing entire sites when you need specific pages. Solution: Be selective, use targeted URLs.

## Examples

### Example: Add Single Reference Article

```bash
PBC_VENV="C:/Users/drewa/pbcs/pbc-web-crawling/tool-crawl4ai/.venv/Scripts/python.exe"
PBC_SCRIPTS="C:/Users/drewa/pbcs/pbc-web-crawling/tool-crawl4ai/scripts"

"$PBC_VENV" "$PBC_SCRIPTS/url_to_markdown.py" \
    "https://example.com/great-article" \
    --output "./kb/topic/great-article.md"
```

### Example: Capture Tutorial Series

```bash
"$PBC_VENV" "$PBC_SCRIPTS/batch_urls_to_markdown.py" \
    --urls \
    "https://tutorial-site.com/part-1" \
    "https://tutorial-site.com/part-2" \
    "https://tutorial-site.com/part-3" \
    --output-dir "./kb/tutorials/series-name"
```

### Example: Add Product Documentation

```bash
"$PBC_VENV" "$PBC_SCRIPTS/deep_crawl_docs.py" \
    "https://docs.product.com" \
    --output-dir "./kb/products/product-name/docs" \
    --max-depth 4 \
    --max-pages 200
```

## Index Template

Maintain an index for your knowledge base:

```markdown
# Knowledge Base Index

Last Updated: 2025-01-15

## Topics

### [Topic 1]
- **Articles:** 5 files
- **Documentation:** 2 product doc sets
- **Tutorials:** 3 series

### [Topic 2]
- ...

## Recent Additions

| Date | Content | Location |
|------|---------|----------|
| 2025-01-15 | Great Article on X | kb/topic1/great-article.md |
| 2025-01-14 | Product Y Docs | kb/products/product-y/ |

## Capture Log

| Date | Source | Files | Notes |
|------|--------|-------|-------|
| 2025-01-15 | example.com | 1 | Single article |
| 2025-01-10 | docs.product.com | 150 | Full docs |
```

## Maintenance Tasks

### Periodic Review
- Check for outdated content (>6 months old)
- Re-crawl updated documentation
- Remove deprecated resources

### Quality Control
- Verify files aren't empty or error pages
- Check for duplicate captures
- Ensure consistent organization

## Related Documentation

- [Simple Crawling](../docs/02-crawl4ai-simple-crawling-2025-12-03.md)
- [Deep Crawling](../docs/07-crawl4ai-deep-crawling-2025-12-03.md)

---

- **Document Status:** Stub
- **Next Review:** After first validation
