---
guide_id: workflow-integration
version: "1.0.0"
created: 2025-12-15
purpose: "Guide for integrating extraction findings into workflow documents"
audience: "Claude (LLM executor)"
---

# Workflow Integration Guide

- **Version:** 1.0.0
- **Purpose:** Take completed extractions and update workflow documents
- **Primary Audience:** Claude (LLM executor)
- **Secondary Audience:** Drew Arnold (oversight)

## Overview

This guide covers Phase 3 of the workflow evolution process: taking a completed extraction and using it to improve workflow documents.

**Prerequisites:**
- A completed extraction in `workflow-evolution/extractions/`
- Extraction status is `pending_integration`
- Target workflow exists in `workflows/`

## Integration Process

### Step 1: Review the Extraction

Read the extraction file and identify:

1. **recommended_updates** - Explicit suggestions for changes
2. **workflow_gaps** - Missing guidance that should be added
3. **what_worked** - Patterns to emphasize or add
4. **what_failed** - Pitfalls to document

```yaml
# Key sections to review
recommended_updates:
  - section: "<workflow section>"
    change_type: "add | modify | emphasize"
    description: "<what to change>"

workflow_gaps:
  - gap: "<what's missing>"
    suggested_addition: "<what to add>"
    priority: "high | medium | low"
```

### Step 2: Determine Status Transition

Based on the extraction outcome, decide if the workflow status should change:

| Current Status | Extraction Outcome | New Status |
|---------------|-------------------|------------|
| stub | successful | draft |
| stub | partial | stub (add learnings) |
| draft | successful | validated |
| draft | partial | draft (add learnings) |
| validated | successful | validated (may → mature after 3+) |
| validated | failed | validated (add failure learnings) |

**Criteria for "mature" status:**
- 3+ successful validations
- Patterns have been refined based on multiple uses
- Common pitfalls are well documented

### Step 3: Update the Workflow Document

#### 3.1 Update YAML Front Matter

```yaml
# Update these fields
last_updated: "[today's date]"
version: "[bump if significant changes]"

# Add to validated_by array
validated_by:
  - project: "[project-name]"
    date: "[extraction-date]"
    outcome: "successful | partial | failed"
    notes: "[brief learning]"
```

#### 3.2 Apply recommended_updates

For each entry in `recommended_updates`:

**If change_type is "add":**
- Add new content to the specified section
- Follow existing formatting patterns

**If change_type is "modify":**
- Find the existing content
- Update based on the description
- Preserve what still works

**If change_type is "emphasize":**
- Make the pattern more prominent
- Add examples if helpful
- Consider moving to earlier position in section

#### 3.3 Address workflow_gaps

For each gap with priority "high" or "medium":
- Add the suggested content
- Place in appropriate section
- Mark with comment if uncertain about placement

Low priority gaps can be deferred or noted in a TODO comment.

#### 3.4 Update Lessons Learned

Add entries from `what_worked` and `what_failed`:

```markdown
## Lessons Learned

### What Works Well

- **[Pattern name]:** [Description of why it works]

### Common Pitfalls

- **[Pitfall]:** [What goes wrong and how to avoid it]
```

#### 3.5 Add Fallback Strategies

For any new entries in `fallback_strategies`:

```markdown
## Fallback Strategies

| Issue | Detection | Resolution |
|-------|-----------|------------|
| [issue] | [how to detect] | [what to do] |
```

### Step 4: Update the Extraction Record

After integration, update the extraction file:

```markdown
## Integration Status

- **Extracted:** [original date]
- **Integrated:** [today's date]
- **Changes Made:**
  - [List each change made to the workflow]
  - [Include section names and change types]
```

Change the front matter status:

```yaml
status: "integrated"
```

### Step 5: Verify Integration

Checklist:
- [ ] Workflow `last_updated` is today's date
- [ ] Workflow `validated_by` includes new entry
- [ ] All high/medium priority gaps addressed
- [ ] Extraction status changed to "integrated"
- [ ] Extraction lists changes made

---

## Quick Reference

### Files to Update

| File | What to Update |
|------|---------------|
| `workflows/[target].md` | Content, front matter, validated_by |
| `extractions/[extraction].md` | Integration status, changes made |
| `workflows/README.md` | Status column if status changed |

### Status Values

| Workflow Status | Meaning |
|----------------|---------|
| stub | Placeholder, not yet used |
| draft | Initial content, needs validation |
| validated | Used successfully in 1-2 projects |
| mature | 3+ successful uses, refined patterns |

| Extraction Status | Meaning |
|------------------|---------|
| pending_integration | Ready for integration |
| integrated | Changes applied to workflow |

---

- **Guide Status:** Active
- **Created:** 2025-12-15
