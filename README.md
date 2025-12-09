# Packaged Business Capabilities (PBCs)

A collection of self-contained, composable capability packages designed for AI-assisted workflows.

- **Author:** Drew Arnold
- **Status:** Active development
- **Philosophy:** Pick off the shelf, compose as needed

## What is a PBC?

A Packaged Business Capability (PBC) is a self-contained unit that:

- **Solves a specific problem** - Content acquisition, data processing, etc.
- **Includes everything needed** - Scripts, documentation, workflows, tool configuration
- **Works with AI agents** - Claude, Gemini, or other LLM-powered tools can invoke them
- **Composes with other PBCs** - Designed to work together in pipelines

## PBC Catalog

| PBC | Purpose | Status |
|-----|---------|--------|
| [web-crawling-pbc](web-crawling-pbc/) | URL to markdown, deep crawling, structured extraction | Experimental |
| rag-pipeline-pbc | Indexing, semantic search, vector storage | Planned |
| media-transcription-pbc | Audio/video to text | Planned |

## Architecture

PBCs are designed to compose into pipelines:

```
web-crawling-pbc ──────┐
                       ├──► rag-pipeline-pbc (indexing, semantic search)
media-transcription-pbc┘
```

Each PBC has:

```
{pbc-name}/
├── CLAUDE.md              # AI agent instructions
├── README.md              # Human documentation
├── pbc-definition.yaml    # Capability manifest
├── scripts/               # Reusable scripts
├── workflows/             # Task patterns and guides
├── docs/                  # Tool documentation
└── .venv/                 # Python environment (gitignored)
```

## Using a PBC

### For AI Agents (Claude, Gemini)

Point the agent to the PBC's `CLAUDE.md` for instructions:

```
Read C:\Users\drewa\pbcs\web-crawling-pbc\CLAUDE.md and help me crawl this documentation site.
```

### For Humans

1. Check the PBC's `README.md` for overview and quick start
2. Review `pbc-definition.yaml` for available scripts and capabilities
3. Use scripts directly or follow workflows for complex tasks

## Contributing

Each PBC evolves through use. After completing a project:

1. Run a **patterns extraction** using the PBC's workflow-evolution system
2. Update workflows and documentation with learnings
3. Scripts mature: stub → active → validated

## Related Projects

- [crawl4ai-implementation-project](https://github.com/DAESA24/crawl4ai-implementation-project) - Implementation docs and setup history for web-crawling-pbc
