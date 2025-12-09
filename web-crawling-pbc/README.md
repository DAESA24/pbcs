# Web Crawling PBC

Content acquisition from web sources - URLs to markdown and structured data.

- **Status:** Experimental
- **Created:** 2025-12-04
- **Version:** 0.1.0
- **Role:** Content acquisition (feeds into rag-pipeline)

## What This PBC Provides

- Single URL to clean markdown conversion
- Deep crawling of documentation sites
- Structured data extraction via CSS/XPath selectors
- JavaScript-rendered page support (unlike basic fetch tools)

## Tool Inventory

### Global CLI Tool

| Tool | Location | Command | Installed Via |
|------|----------|---------|---------------|
| Crawl4AI CLI | `C:\Users\drewa\.local\bin\crwl.exe` | `crwl` | `uv tool install crawl4ai` |

**Use cases for CLI:**
- Quick one-off URL to markdown: `crwl https://example.com -o markdown`
- Claudesidian inbox processing
- Replacing WebFetch in workflows
- Any time you need fast, ad-hoc web content extraction

### PBC Virtual Environment

| Tool | Location | Purpose |
|------|----------|---------|
| crawl4ai (Python) | `C:\Users\drewa\pbcs\web-crawling\.venv\` | Python scripting with full API access |

**Use cases for venv:**
- Reusable scripts in `scripts/` directory
- Deep crawling with custom strategies
- Batch processing multiple URLs
- Structured extraction with selectors
- Integration with other PBCs

## Quick Reference

### CLI Examples

```bash
# Single URL to markdown (stdout)
crwl https://example.com -o markdown

# Save to file
crwl https://example.com -o markdown > article.md

# With browser (for JS-rendered pages)
crwl https://spa-site.com -o markdown --browser
```

### Python Script Invocation

```bash
# Run a script from this PBC (from any directory)
C:\Users\drewa\pbcs\web-crawling\.venv\Scripts\python.exe ^
    C:\Users\drewa\pbcs\web-crawling\scripts\deep_crawl_docs.py ^
    --url https://docs.example.com ^
    --output .\output\
```

## Scripts

| Script | Status | Description |
|--------|--------|-------------|
| `url_to_markdown.py` | Active | Single URL to clean markdown |
| `batch_urls_to_markdown.py` | Active | Multiple URLs to markdown files |
| `deep_crawl_docs.py` | Active | Crawl nested documentation sites |

See [pbc-definition.yaml](pbc-definition.yaml) for detailed script specifications.

## Workflows

Reusable patterns for common crawling use cases. See [workflows/README.md](workflows/README.md) for the full index.

| Workflow | Abstraction | Status | Use Case |
|----------|-------------|--------|----------|
| [Deep Company Research](workflows/deep-company-research.md) | Medium | Draft | Multi-phase company research |
| [Documentation Ingestion](workflows/documentation-ingestion.md) | Low | Stub | Crawl docs for RAG |
| [Competitive Analysis](workflows/competitive-analysis.md) | Low | Stub | Compare competitors |
| [News Monitoring](workflows/news-monitoring.md) | Low | Stub | Track news coverage |
| [Knowledge Base Building](workflows/knowledge-base-building.md) | Low | Stub | Build reference collections |

### Workflow Evolution

After using Crawl4AI in a project, run a patterns extraction to feed learnings back into workflows. See [workflow-evolution/README.md](workflow-evolution/README.md).

```
workflow-evolution/
├── README.md                 # How the feedback loop works
├── extraction-template.md    # Template for extracting patterns
├── integration-guide.md      # How to update workflows
└── extractions/              # Completed extraction records
```

## Composability

This PBC is a **content acquisition** capability:

```
web-crawling ──────┐
                   ├──► rag-pipeline (indexing, semantic search)
media-transcription┘
```

- **Feeds into:** rag-pipeline (extracted text for indexing)
- **Peer capability:** media-transcription (both acquire content for RAG)

## Installation

### 1. Global CLI (for quick commands)

```bash
uv tool install crawl4ai
crawl4ai-setup  # installs browser dependencies
```

### 2. PBC Virtual Environment (for scripting)

```bash
cd C:\Users\drewa\pbcs\web-crawling
uv venv
uv pip install crawl4ai
```

## Related Documentation

- [Crawl4AI Docs](https://docs.crawl4ai.com/)
- Local docs: `c:\Users\drewa\work\dev\local-infrastrructure-projects\crawl4ai-implementation-project\crawl4ai-docs\`
