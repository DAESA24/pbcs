---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git branch:*), Bash(git log:*), Bash(git diff:*)
description: PBC monorepo commit workflow - groups changes by PBC directory with conventional commits
---

# Commit PBC Command

Automates the Git commit workflow for the PBC monorepo: group changes by PBC directory, create conventional commits for each group, and push.

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status`
- Staged changes: !`git diff --staged`
- Unstaged changes: !`git diff`
- Recent commits: !`git log --oneline -5`

## Instructions

### Step 1: Group Changes by PBC

Analyze all changes and group them by directory:

| Group Type | Pattern | Scope |
|------------|---------|-------|
| Root files | `CLAUDE.md`, `README.md`, `.gitignore` | no scope or `(root)` |
| Infrastructure | `.claude/**` | `chore` type |
| PBC-specific | `pbc-*//**` | `(pbc-name)` e.g. `(pbc-web-crawling)` |
| Tool-specific | Single tool within PBC | `(tool-name)` e.g. `(tool-crawl4ai)` |

**Rules:**
- Each PBC gets ONE commit (all files under `pbc-foo/` go together)
- Root and infrastructure changes get separate commits from PBC changes
- Use tool-level scope only when changes are isolated to one tool

### Step 2: Create Commits

For each group, stage and commit with conventional message format:

| Type | When to Use |
|------|-------------|
| `feat` | New capability, script, or workflow |
| `fix` | Bug fix or correction |
| `docs` | Documentation changes only |
| `refactor` | Code restructuring without behavior change |
| `chore` | Maintenance, config, infrastructure |

Use HEREDOC format with standard footer:

```bash
git add <files>
git commit -m "$(cat <<'EOF'
<type>(<scope>): <description>

<body if multiple files or non-obvious changes>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"
```

**Message guidelines:**
- Imperative mood ("add", "update", "fix")
- Lowercase first letter, no period at end
- Body uses bullet points for multiple changes

### Step 3: Push Changes

1. Check current branch
2. If on `main`: push directly
3. If NOT on `main`: ask user which branch to push to

```bash
git push origin <branch>
```

### Step 4: Report Summary

After completion, report what was committed:

```text
✅ Committed and pushed to main:

1. docs(root): update routing table
   - 2 files changed

2. feat(pbc-web-crawling): add URL discovery script
   - 3 files changed
```

## Critical Requirements

- Review changes BEFORE committing (never commit blindly)
- Do NOT commit files containing secrets (.env, credentials, etc.)
- Confirm push target when not on main branch
- Keep commit messages concise - focus on "why" not "what"
