# Conventional Commits for PBC Monorepo

Reference documentation for commit message formatting in the PBC monorepo.

## Format

```text
<type>(<scope>): <description>

[optional body]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <model> <noreply@anthropic.com>
```

## Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature or capability | Adding a new script, workflow, or tool |
| `fix` | Bug fix | Correcting broken paths, typos that cause errors |
| `docs` | Documentation only | README updates, CLAUDE.md changes, comment fixes |
| `refactor` | Code restructuring | Renaming files, reorganizing directories, schema changes |
| `chore` | Maintenance tasks | Dependency updates, config changes, cleanup |
| `style` | Formatting changes | Whitespace, linting fixes, markdown formatting |
| `test` | Test-related changes | Adding or updating tests |
| `perf` | Performance improvements | Optimizing scripts |

## Scopes for PBC Monorepo

### Root-Level Scope

For changes to files in the repository root (`pbcs/`):

```text
docs: update root documentation
chore: add gitignore entries
```

Or explicitly:

```text
docs(root): update navigation table in CLAUDE.md
```

### PBC-Level Scope

For changes within a specific PBC directory:

```text
refactor(pbc-web-crawling): restructure tool definitions
docs(pbc-media-download): update README with new paths
feat(pbc-secrets-management): add credential retrieval workflow
```

### Tool-Level Scope

When changes are specific to a single tool within a PBC:

```text
feat(tool-crawl4ai): add deep crawl script
fix(tool-yt-dlp): correct config preset paths
docs(tool-1password-cli): update security model section
```

## Real Examples from This Repository

### Documentation Updates

```text
docs: update root documentation for tool subdirectory structure

Update CLAUDE.md and README.md to reflect new multi-tool architecture:
- Update routing table to point to {pbc}/tool-{toolname}/CLAUDE.md paths
- Update venv path pattern to {pbc}/{tool}/.venv/Scripts/python.exe
- Update architecture diagram to show tool subdirectory structure

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### Refactoring

```text
refactor(pbc-web-crawling): move tool content to tool-crawl4ai/ subdirectory

Restructure pbc-web-crawling to support multi-tool architecture:
- Move all Crawl4AI-specific content to tool-crawl4ai/ subdirectory
- Create PBC-level CLAUDE.md and README.md as domain routers
- Update all internal path references for new structure

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### New Features

```text
feat(pbc-secrets-management): add secrets management PBC

Add new PBC for credential management using 1Password CLI:
- Create pbc-definition.yaml with tool specifications
- Add CLAUDE.md with security model and usage patterns
- Include workflow stubs for common credential tasks
- Crawl and store 1Password CLI documentation

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### Chore/Maintenance

```text
chore: add Claude Code configuration

Add .claude directory with project-specific settings and handoff documents.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

## Body Guidelines

### When to Include a Body

- Multiple files changed (list key changes)
- Non-obvious changes (explain the "why")
- Breaking changes (describe impact)
- Related changes grouped together

### Body Structure

Use bullet points for clarity:

```text
refactor(pbc-media-download): update tool definition schema

- Rename pbc-definition.yaml to pbc-tool-definition.yaml
- Add tool_name, tool_id, parent_pbc fields
- Update all internal references to new filename
- Flatten nested tools section (file IS the tool now)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### When Body Can Be Omitted

For simple, self-explanatory changes:

```text
fix(tool-crawl4ai): correct typo in workflow path

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

## Footer (Required)

Always include the Claude Code attribution:

```text
🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <model> <noreply@anthropic.com>
```

Replace `<model>` with the actual model name (e.g., `Opus 4.5`, `Sonnet 3.5`).

## Common Patterns

### Schema/Structure Changes

```text
refactor(pbc-*): rename pbc-definition.yaml to pbc-tool-definition.yaml
```

### Cross-Cutting Documentation

```text
docs: update all CLAUDE.md files for new tool definition schema
```

### Single File Fix

```text
fix(tool-yt-dlp): correct venv path in CLAUDE.md
```

### New Workflow Addition

```text
feat(tool-crawl4ai): add competitive analysis workflow

Add new workflow pattern for comparing multiple companies/products:
- Create workflows/competitive-analysis.md
- Update workflows/README.md index
- Reference in pbc-tool-definition.yaml

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```
