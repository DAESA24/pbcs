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
| [pbc-web-crawling](pbc-web-crawling/) | URL to markdown, deep crawling, structured extraction | Experimental |
| [pbc-media-download](pbc-media-download/) | Video/audio downloads, metadata extraction | Experimental |
| [pbc-secrets-management](pbc-secrets-management/) | Credential management, secret references | Experimental |
| pbc-rag-pipeline | Indexing, semantic search, vector storage | Planned |
| pbc-media-transcription | Audio/video to text | Planned |

## Architecture

PBCs are designed to compose into pipelines:

```
pbc-web-crawling ──────┐
                       ├──► pbc-rag-pipeline (indexing, semantic search)
pbc-media-transcription┘
```

Each PBC has:

```text
pbc-{domain}/
├── CLAUDE.md                   # PBC-level routing
├── README.md                   # PBC-level overview
└── tool-{toolname}/            # Tool-specific subdirectory
    ├── CLAUDE.md               # Tool-specific AI instructions
    ├── README.md               # Tool-specific documentation
    ├── pbc-tool-definition.yaml  # Tool manifest
    ├── scripts/
    ├── workflows/
    ├── docs/
    └── .venv/
```

## Using a PBC

### For AI Agents (Claude, Gemini)

Point the agent to the PBC's `CLAUDE.md` for instructions:

```
Read C:\Users\drewa\pbcs\pbc-web-crawling\tool-crawl4ai\CLAUDE.md and help me crawl this documentation site.
```

### For Humans

1. Check the PBC's `README.md` for overview and quick start
2. Review `pbc-tool-definition.yaml` for available scripts and capabilities
3. Use scripts directly or follow workflows for complex tasks

## Contributing

Each PBC evolves through use. After completing a project:

1. Run a **patterns extraction** using the PBC's workflow-evolution system
2. Update workflows and documentation with learnings
3. Scripts mature: stub → active → validated

## Related Projects

- [web-crawling-pbc-implementation-project](https://github.com/DAESA24/web-crawling-pbc-implementation-project) - Implementation docs and setup history for pbc-web-crawling
