# PBC Ecosystem - Claude Instructions

## What This Is

This is Drew Arnold's **Packaged Business Capabilities (PBCs)** monorepo - a collection of self-contained, composable capability packages designed explicitly for AI-assisted workflows.

**Key context:**
- Drew is an independent developer (not enterprise)
- The PBC concept is borrowed from enterprise composable architecture, simplified for solo use
- PBCs are designed to work WITH you (Claude) as a first-class interaction pattern
- Think of this as a "pick off the shelf" toolkit that you can invoke during sessions

## How to Navigate

**When a session starts in `pbcs/`:**

1. First understand what task the user needs
2. Use this table to identify which PBC to use:

| User needs to... | Use this PBC | Read first |
|------------------|--------------|------------|
| Convert URLs to markdown | web-crawling-pbc | `web-crawling-pbc/CLAUDE.md` |
| Crawl documentation sites | web-crawling-pbc | `web-crawling-pbc/CLAUDE.md` |
| Extract structured data from web | web-crawling-pbc | `web-crawling-pbc/CLAUDE.md` |
| Index content for RAG | rag-pipeline-pbc | (planned) |
| Transcribe audio/video | media-transcription-pbc | (planned) |

3. Once you identify the PBC, read its `CLAUDE.md` for specific instructions

**When referenced from another project:**

If a project's CLAUDE.md says "use the web-crawling PBC", come here and read the specific PBC's CLAUDE.md for instructions.

## PBC Invocation Pattern

Each PBC provides multiple access methods:

```
Global CLI (quick tasks)     → crwl, transcribe, etc.
PBC venv (Python scripts)    → {pbc}/.venv/Scripts/python.exe
pbc-definition.yaml          → Script inventory and capabilities
```

**Prefer existing scripts over writing new code.** Check `pbc-definition.yaml` first.

## Cross-PBC Constraints

These apply to ALL PBCs:

- **No Docker** - Drew doesn't use Docker for local tooling
- **No LLM extraction** - Use CSS/XPath selectors for web scraping, not LLM-based extraction
- **Ollama is for embeddings only** - Don't configure tools to use Ollama for text generation
- **uv is the Python package manager** - Use `uv pip`, `uv venv`, `uv tool`
- **Windows environment** - Paths use backslashes, scripts need Windows compatibility

## Composability

PBCs are designed to feed into each other:

```
web-crawling-pbc ──────┐
                       ├──► rag-pipeline-pbc ──► search/retrieval
media-transcription-pbc┘
```

When a task spans multiple PBCs:
1. Identify the pipeline flow
2. Execute each PBC's scripts in sequence
3. Pass outputs as inputs to the next stage

## Workflow Evolution

After completing a project that used PBCs, suggest running a **patterns extraction** to improve the workflows:

1. Each PBC has a `workflow-evolution/` directory
2. Use `extraction-template.md` to capture learnings
3. Feed insights back into workflow documents

This helps PBCs mature over time: stub → draft → validated → mature.

## When to Create a New PBC

If the user needs a capability that doesn't exist:

1. Check if an existing PBC can be extended first
2. If truly new, propose a PBC structure following the existing pattern:
   - `CLAUDE.md` - AI instructions
   - `README.md` - Human documentation
   - `pbc-definition.yaml` - Capability manifest
   - `scripts/` - Reusable scripts
   - `workflows/` - Task patterns
   - `docs/` - Tool documentation

## Individual PBC Instructions

For specific task guidance, read the PBC's own CLAUDE.md:

- [web-crawling-pbc/CLAUDE.md](web-crawling-pbc/CLAUDE.md) - Web scraping, URL to markdown, deep crawling
