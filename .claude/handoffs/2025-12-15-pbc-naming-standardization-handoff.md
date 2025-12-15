---
handoff_id: 2025-12-15-pbc-naming-standardization-handoff
created: 2025-12-15 16:05
status: pickup_completed
workspace: C:\Users\drewa\pbcs
pickup_history:
  - date: 2025-12-15 17:00
    notes: "Executed all 7 phases: created backups, updated all path references in both PBCs, renamed directories (web-crawling-pbc → pbc-web-crawling, media-download-pbc → pbc-media-download), updated root docs, cross-PBC refs, youtube-audio-download skill, validated no remaining old refs, removed backups"
---

# PBC Naming Convention Standardization

- **Created:** 2025-12-15 16:05
- **Purpose:** Execute the plan to rename PBC directories to use consistent `pbc-` prefix naming convention
- **Status:** Pickup completed

## Primary Request and Intent

Drew noticed that PBC directory naming is inconsistent:
- `pbc-1password-cli` (correct - prefix)
- `web-crawling-pbc` (incorrect - suffix)
- `media-download-pbc` (incorrect - suffix)

He wants all PBCs to use the `pbc-` prefix convention. A detailed plan was created to safely rename the directories while updating all internal path references to avoid breaking dependencies.

## Key Technical Concepts

- **PBC Naming Convention:** `pbc-{capability-name}` (prefix, not suffix)
- **Path Reference Types:**
  - Windows backslash: `C:\Users\drewa\pbcs\web-crawling-pbc\`
  - Bash forward slash: `/c/Users/drewa/pbcs/media-download-pbc/`
  - Relative paths: `web-crawling-pbc/CLAUDE.md`
- **Dependencies span multiple locations:** pbcs/, .claude/skills/, root CLAUDE.md

## Files and Code Sections

### Detailed Execution Plan

**Location:** `C:\Users\drewa\.claude\plans\2025-12-15-pbc-naming-convention-standardization.md`

This plan contains all the specifics - READ IT FIRST before executing.

### Summary of Changes Required

**web-crawling-pbc → pbc-web-crawling (~19 path refs):**
- `CLAUDE.md` - Line 20
- `README.md` - Lines 35, 63-64, 128 (NOTE: currently incorrect, says `web-crawling` not `web-crawling-pbc`)
- `workflows/README.md` - Line 5
- `workflows/deep-company-research.md` - Lines 159, 162, 181-182
- `workflows/news-monitoring.md` - Lines 82-83
- `workflows/knowledge-base-building.md` - Lines 102-103
- `workflows/documentation-ingestion.md` - Lines 108-109
- `workflows/competitive-analysis.md` - Lines 94-95
- `workflow-evolution/README.md` - Line 5
- `workflow-evolution/extraction-template.md` - Lines 69, 75

**media-download-pbc → pbc-media-download (~10 path refs):**
- `CLAUDE.md` - Line 24
- `README.md` - Lines 73-74, 137
- `GLOBAL_CONFIG_SETUP.md` - Lines 17, 32
- `configs/audio-only.conf` - Line 20
- `configs/video-720p.conf` - Line 20
- `configs/video-1080p.conf` - Line 20
- `configs/metadata-only.conf` - Line 11

**Claude Skills (17 refs):**
- `C:\Users\drewa\.claude\skills\youtube-audio-download\SKILL.md` - Lines 10, 14, 17-18, 42-43, 60, 70-71, 82, 95-96, 105-106, 115-116, 135

**Root pbcs/ files:**
- `CLAUDE.md` - Lines 22-24, 64, 101
- `README.md` - Lines 22, 31, 56, 75

**Cross-PBC reference:**
- `media-download-pbc/pbc-definition.yaml` - Line 123 (references `web-crawling-pbc` as peer)

## Pending Tasks

- [x] Phase 1: Create backups of both PBC directories
- [x] Phase 2: Update web-crawling-pbc internal files, then rename directory
- [x] Phase 3: Update media-download-pbc internal files, then rename directory
- [x] Phase 4: Update root pbcs/CLAUDE.md and README.md
- [x] Phase 5: Update cross-PBC reference in pbc-definition.yaml
- [x] Phase 6: Update youtube-audio-download skill
- [x] Phase 7: Validate all changes and remove backups

## Current Work

All phases completed successfully. PBC directories have been renamed to use the `pbc-` prefix convention:
- `web-crawling-pbc` → `pbc-web-crawling`
- `media-download-pbc` → `pbc-media-download`

All path references updated across:
- PBC internal files (CLAUDE.md, README.md, workflows, configs)
- Root pbcs/CLAUDE.md and README.md
- pbc-1password-cli cross-references
- youtube-audio-download skill
- pbc-media-download/pbc-definition.yaml peer reference

Backups removed after validation confirmed no remaining old references in active PBC directories.

## Next Steps

~~1. Read the detailed plan~~ ✓
~~2. Close any VS Code windows~~ ✓
~~3. Execute the plan phases in order (1-7)~~ ✓
~~4. Use `replace_all` in Edit tool for efficient search/replace~~ ✓
~~5. Run validation grep commands to confirm no old references remain~~ ✓

**All tasks complete.** Final directory structure:
```
pbcs/
├── pbc-1password-cli/
├── pbc-media-download/
└── pbc-web-crawling/
```

## Important Context

- **Backup first:** Create backups before any changes (plan has exact commands)
- **Order matters:** Update internal files BEFORE renaming directories
- **Known bug to fix:** `web-crawling-pbc/README.md` has wrong paths (says `web-crawling` instead of `web-crawling-pbc`) - fix these to `pbc-web-crawling`
- **Rollback plan included:** If something breaks, plan has commands to restore from backups
- **Also completed this session:**
  - Converted 1Password CLI tool to PBC (done)
  - Created `C:\Users\drewa\Scripts\cleanup-reserved-files.ps1` with scheduled task for Windows reserved filename cleanup (daily at 2:30 AM)
