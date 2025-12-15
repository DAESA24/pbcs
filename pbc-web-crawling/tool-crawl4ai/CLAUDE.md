# Web Crawling PBC - Claude Instructions

## When to Use This PBC

Use this PBC when the user needs to:
- Convert URLs to markdown
- Crawl documentation sites
- Extract structured data from web pages
- Replace WebFetch with something more capable

## Quick Reference

**Global CLI (simple tasks):**
```bash
crwl https://example.com -o markdown
```

**PBC venv (Python scripts):**
```bash
C:\Users\drewa\pbcs\pbc-web-crawling\tool-crawl4ai\.venv\Scripts\python.exe script.py
```

## Documentation by Task

| Task | Read This First |
|------|-----------------|
| Single URL to markdown | `docs/02-crawl4ai-simple-crawling-2025-12-03.md` |
| Configure browser/crawler options | `docs/03-crawl4ai-configuration-objects-2025-12-03.md` |
| Extract specific data (tables, lists) | `docs/05-crawl4a-data-extractions-no-llm-2025-12-03.md` |
| Bulk URL processing | `docs/06-crawl4ai-multi-url-crawling-2025-12-03.md` |
| Deep crawl a docs site | `docs/07-crawl4ai-deep-crawling-2025-12-03.md` |
| CLI options and flags | `docs/09-crawl4ai-cli-2025-12-03.md` |
| Fast static content (no JS) | `docs/10-crawl4ai-http-based-crawler-2025-12-03.md` |
| Bulk URL discovery (sitemaps, Common Crawl) | `docs/11-crawl4ai-url-seeder-2025-12-03.md` |
| Content filtering and relevance scoring | `docs/12-crawl4ai-advanced-filters-and-scores-2025-12-03.md` |

## Scripts Inventory

Check `pbc-definition.yaml` for available scripts and their status.
Prefer using existing scripts over writing new code.

## Workflows

Before starting a crawling task, check if a workflow pattern exists in `workflows/`:

| Workflow | When to Use |
|----------|-------------|
| [Deep Company Research](workflows/deep-company-research.md) | Multi-phase research on a company (planning → crawling → synthesis → report) |
| [Documentation Ingestion](workflows/documentation-ingestion.md) | Crawl docs for RAG pipeline |
| [Competitive Analysis](workflows/competitive-analysis.md) | Compare multiple companies/products |
| [News Monitoring](workflows/news-monitoring.md) | Track articles and news coverage |
| [Knowledge Base Building](workflows/knowledge-base-building.md) | Build reference collections over time |

Workflows provide:

- Decision trees for which scripts to use
- Phase-by-phase guidance for complex tasks
- Fallback strategies when things fail
- Lessons learned from past projects

See [workflows/README.md](workflows/README.md) for the full index and maturity levels.

## Workflow Evolution

After completing a project that used Crawl4AI, run a **patterns extraction** to feed learnings back into workflows:

1. Copy `workflow-evolution/extraction-template.md`
2. Fill in project-specific details
3. Execute the extraction phases
4. Use `workflow-evolution/integration-guide.md` to update workflows

This feedback loop helps workflows mature: stub → draft → validated → mature.

See [workflow-evolution/README.md](workflow-evolution/README.md) for the full system.

## Constraints

- **No Docker** - User doesn't use Docker for this
- **No LLM extraction** - Use CSS/XPath selectors instead
- **Ollama is for embeddings only** - Don't configure Crawl4AI to use Ollama for extraction
