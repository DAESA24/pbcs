---
name: pbc-git-commit
description: Automates Git commit workflow for Drew's PBC monorepo. This skill should be used when the user requests to commit and push changes in the pbcs directory with phrases like "commit these changes", "push to main", "stage and commit", "review changes and commit", or "group commits by PBC". Groups unstaged changes by PBC directory, creates conventional commit messages for each group, and pushes to main.
---

# PBC Git Commit

Automates the complete Git workflow for Drew's PBC (Packaged Business Capabilities) monorepo: review unstaged changes, group them by PBC directory, generate conventional commit messages for each group, and push to main.

## When to Use This Skill

Use this skill when in the `pbcs/` directory and the user requests:

- "Commit these changes"
- "Push to main"
- "Stage and commit"
- "Review changes and commit"
- "Group commits by PBC"
- Any commit-related request while working in the PBC monorepo

## Directory Context

**Target Repository:** `C:\Users\drewa\pbcs` (PBC monorepo)

This skill is specific to the PBC monorepo structure where multiple PBCs live as subdirectories:

```text
pbcs/
├── pbc-web-crawling/
│   └── tool-crawl4ai/
├── pbc-media-ingestion/
│   └── tool-yt-dlp/
├── pbc-secrets-management/
│   └── tool-1password-cli/
└── (root files: CLAUDE.md, README.md)
```

## Automated Workflow

Execute this workflow without permission prompts. Drew explicitly wants this automated.

### Step 1: Review Changes

Run these commands in parallel to understand what changed:

```bash
git status
git diff
git diff --cached  # if there are staged changes
git log -5 --oneline  # recent commit style reference
```

### Step 2: Group Changes into Logical Commits

Analyze the changed files and group them into logical commits. There are three types of groups:

#### Group Type 1: Root-Level Changes

Files directly in `pbcs/` root that are NOT inside any `pbc-*/` subdirectory:

- `CLAUDE.md` - Root AI instructions
- `README.md` - Root documentation
- `.gitignore` - Git configuration
- Any other root-level files

**These get their own commit** with no scope or `(root)` scope.

#### Group Type 2: PBC-Specific Changes

Files inside any `pbc-*/` directory (including all nested tool directories):

- `pbc-web-crawling/**` → One commit for all changes in this PBC
- `pbc-media-ingestion/**` → One commit for all changes in this PBC
- `pbc-secrets-management/**` → One commit for all changes in this PBC

**Each PBC gets its own commit** with the PBC name as scope.

#### Group Type 3: Infrastructure/Shared Changes

Files in shared directories like `.claude/`:

- `.claude/handoffs/` - Session handoffs
- `.claude/settings/` - Configuration

**These get their own commit** with `chore` type.

#### Example Grouping

```text
Changed files:
  CLAUDE.md                                    → Group: root
  README.md                                    → Group: root
  pbc-web-crawling/tool-crawl4ai/CLAUDE.md    → Group: pbc-web-crawling
  pbc-web-crawling/tool-crawl4ai/README.md    → Group: pbc-web-crawling
  pbc-media-ingestion/tool-yt-dlp/CLAUDE.md    → Group: pbc-media-ingestion
  .claude/handoffs/some-file.md               → Group: .claude (infrastructure)

Result: 4 commits (in this order)
  1. root changes (CLAUDE.md, README.md)
  2. .claude infrastructure changes
  3. pbc-media-ingestion changes
  4. pbc-web-crawling changes
```

### Step 3: Generate Conventional Commit Messages

For each group, create a conventional commit message following this format:

```text
<type>(<scope>): <description>

<body with details>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <model> <noreply@anthropic.com>
```

**Commit Types:**

| Type | When to Use |
|------|-------------|
| `feat` | New capability, script, or workflow |
| `fix` | Bug fix or correction |
| `docs` | Documentation changes only |
| `refactor` | Code restructuring without behavior change |
| `chore` | Maintenance, config, infrastructure |
| `style` | Formatting, whitespace, linting |

**Scope Rules:**

- Root changes: No scope or `(root)`
- PBC changes: Use PBC name, e.g., `(pbc-web-crawling)`
- Tool-specific: Can use tool name if only one tool changed, e.g., `(tool-crawl4ai)`

**Description Guidelines:**

- Imperative mood ("add", "update", "fix", not "added", "updated", "fixed")
- Lowercase first letter
- No period at end
- Concise but descriptive (50-72 chars)

See `references/conventional-commits.md` for detailed examples.

### Step 4: Execute Commits Sequentially

For each group, stage and commit:

```bash
# Stage files for this group
git add <file1> <file2> ...

# Commit with generated message (use heredoc for multi-line)
git commit -m "$(cat <<'EOF'
<type>(<scope>): <description>

<body>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <model> <noreply@anthropic.com>
EOF
)"
```

**Important:** Commit groups in logical order:

1. Infrastructure/root changes first
2. Then individual PBCs alphabetically

### Step 5: Push to Main

After all commits are created:

```bash
git push origin main
```

### Step 6: Confirm Completion

Report summary:

```text
✅ Committed and pushed to main:

1. docs(root): update documentation for new structure
   - 2 files changed

2. refactor(pbc-web-crawling): update tool definition schema
   - 5 files changed

3. refactor(pbc-media-ingestion): update tool definition schema
   - 3 files changed
```

## Edge Cases

### Nothing to Commit

If `git status` shows no changes:

- Report: "No changes to commit. Working directory is clean."
- Do not attempt commit/push

### Not on Main Branch

If not on main:

- **Stop** and report the current branch
- Ask if user wants to switch to main or cancel

### Single PBC Change

If all changes are within one PBC:

- Create a single commit with that PBC as scope
- No need for multiple commits

### Mixed Root + PBC Changes

Always separate root-level changes from PBC-specific changes into different commits.

## Resources

### references/

- `conventional-commits.md` - Detailed conventional commit format with PBC-specific examples

## Key Principles

1. **Three Group Types** - Root files, PBC directories, and infrastructure each get separate commits
2. **One Commit Per PBC** - All changes within a PBC directory go in one commit
3. **Root Changes Are First-Class** - Root-level files (CLAUDE.md, README.md) get their own commit, not lumped with PBCs
4. **Conventional Commits** - Follow the standard format with type and scope
5. **Logical Order** - Root first, then infrastructure, then PBCs alphabetically
6. **No Permission Prompts** - Execute automatically when invoked
7. **Clear Summaries** - Report what was committed after completion
