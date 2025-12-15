# Workflow Evolution System

A feedback loop mechanism for continuously improving workflow patterns based on real-world 1Password CLI usage.

- **Location:** `C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\workflow-evolution\`
- **Created:** 2025-12-15
- **Purpose:** Systematically capture learnings from projects and feed them back into workflow documents

## The Feedback Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     │
│   │   Phase 1    │    │   Phase 2    │    │   Phase 3    │     │
│   │   EXTRACT    │───▶│    STORE     │───▶│  INTEGRATE   │     │
│   │              │    │              │    │              │     │
│   └──────────────┘    └──────────────┘    └──────────────┘     │
│          │                                        │             │
│          │                                        │             │
│          ▼                                        ▼             │
│   ┌──────────────┐                       ┌──────────────┐      │
│   │   Project    │                       │   Workflow   │      │
│   │   Artifacts  │                       │   Documents  │      │
│   └──────────────┘                       └──────────────┘      │
│                                                  │              │
│                                                  │              │
│                              ┌───────────────────┘              │
│                              ▼                                  │
│                     ┌──────────────┐                           │
│                     │ Next Project │                           │
│                     │   Uses       │                           │
│                     │  Workflows   │                           │
│                     └──────────────┘                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Phase 1: Extract

After completing a project that used 1Password CLI:

1. Use the `extraction-template.md` to create a project-specific extraction plan
2. Analyze project artifacts (scripts, configurations, integrations)
3. Extract patterns, decisions, successes, and failures
4. Identify gaps in current workflows

**Input:** Project artifacts (scripts, config files, documentation)
**Output:** Structured extraction with recommended updates

### Phase 2: Store

Save the completed extraction for reference:

1. Place in `extractions/` directory
2. Use naming convention: `YYYY-MM-DD-project-name-extraction.md`
3. Include all analysis in YAML format
4. Mark status as `pending_integration`

**Input:** Completed extraction analysis
**Output:** Archived extraction record

### Phase 3: Integrate

Apply learnings to workflow documents:

1. Follow the `integration-guide.md` process
2. Update target workflow(s) based on findings
3. Update workflow status if appropriate (stub → draft → validated → mature)
4. Mark extraction as `integrated`

**Input:** Extraction with `pending_integration` status
**Output:** Updated workflow document(s)

## Directory Structure

```
workflow-evolution/
├── README.md                 # This file - explains the system
├── extraction-template.md    # Template for Phase 1 (copy and fill in)
├── integration-guide.md      # Guide for Phase 3 (reference during integration)
└── extractions/              # Phase 2 storage
    └── YYYY-MM-DD-project-name-extraction.md
```

## Quick Start

### After Completing a 1Password CLI Project

1. **Copy the template:**
   ```bash
   cp extraction-template.md extractions/YYYY-MM-DD-my-project-extraction.md
   ```

2. **Fill in project-specific values:**
   - Project name and description
   - Source document paths
   - Target workflow to update

3. **Execute the extraction phases** (Phases 0-2 in template)

4. **Review findings** with user if needed

5. **Integrate** using the integration guide (Phase 3)

### When to Run an Extraction

- After any project that used a workflow
- When you discover a pattern that should be documented
- When something fails and the failure should be captured
- When a workflow felt incomplete during use

## Workflow Maturity Progression

```
stub ──▶ draft ──▶ validated ──▶ mature
  │        │          │            │
  │        │          │            └─ 3+ successful uses
  │        │          └─ 1-2 successful uses
  │        └─ Initial content written
  └─ Placeholder only
```

Each extraction can advance a workflow's maturity:
- A "successful" extraction on a stub → promotes to draft
- A "successful" extraction on a draft → promotes to validated
- 3+ "successful" extractions on validated → promotes to mature

## Current Extractions

| Extraction | Project | Target Workflow | Status |
|------------|---------|-----------------|--------|
| (none yet) | - | - | - |

## Related Documentation

- [Workflows README](../workflows/README.md) - Index of all workflow patterns
- [PBC Tool Definition](../pbc-tool-definition.yaml) - Formal capability specification
- [CLAUDE.md](../CLAUDE.md) - Instructions for Claude

---

- **System Status:** Active
- **Created:** 2025-12-15
