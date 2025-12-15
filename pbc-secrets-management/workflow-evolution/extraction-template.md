---
template_id: workflow-patterns-extraction
template_version: "1.0.0"
created: 2025-12-15
purpose: "Template for extracting workflow patterns from completed 1Password CLI projects"
audience: "Claude (LLM executor)"
---

# Workflow Patterns Extraction Template

- **Template Version:** 1.0.0
- **Purpose:** Extract reusable workflow patterns from a completed 1Password CLI project
- **Primary Audience:** Claude (LLM executor)
- **Secondary Audience:** Drew Arnold (oversight)

## How to Use This Template

1. Copy this template to create a new extraction plan for your project
2. Fill in the `[PLACEHOLDER]` values with project-specific information
3. Execute the phases sequentially
4. Save the completed extraction to `workflow-evolution/extractions/`
5. Use the integration guide to update workflow documents

---

## Project-Specific Configuration

```yaml
# Fill these in before execution
project:
  name: "[PROJECT_NAME]"
  description: "[Brief description of how 1Password CLI was used]"
  completion_date: "[YYYY-MM-DD]"

source_documents:
  # List all project artifacts that document how 1Password CLI was used
  - "[Path to project code/scripts]"
  - "[Path to .env.op templates]"
  - "[Path to any integration documentation]"

target_workflows:
  # Which workflow(s) should this extraction inform?
  primary: "[workflow-id]"  # e.g., credential-retrieval
  secondary: []  # Optional: other workflows that might benefit

output_location: "workflow-evolution/extractions/[YYYY-MM-DD]-[project-name]-extraction.md"
```

---

## Phase 0: Pre-Flight Validation

**Autonomous:** YES

### 0.1 Verify Source Documents Exist

```bash
# Verify each source document exists
ls -la "[path-to-doc-1]"
ls -la "[path-to-doc-2]"
# ... repeat for all source documents
```

### 0.2 Verify Target Workflow Exists

```bash
ls -la "C:/Users/drewa/pbcs/pbc-secrets-management/workflows/[primary-workflow].md"
```

### 0.3 Create Extraction Output File

```bash
touch "C:/Users/drewa/pbcs/pbc-secrets-management/workflow-evolution/extractions/[output-filename].md"
```

---

## Phase 1: Analyze Project (Sub-Agent)

**Autonomous:** YES

### 1.1 Launch Analysis Sub-Agent

Use the Task tool with the following prompt. Customize the source document paths for your project.

**Sub-Agent Type:** `general-purpose`

**Sub-Agent Prompt Template:**

```
You are analyzing the [PROJECT_NAME] project to extract patterns for the "[TARGET_WORKFLOW]" workflow.

## Your Task

Read the following project documents and extract patterns that can improve the workflow:

1. [Source document 1 path]
2. [Source document 2 path]
[... add all source documents]

## Extraction Questions

### 1. Credential Access Patterns
- What types of credentials were accessed?
- How were secret references structured?
- What vault/item naming patterns were used?

### 2. Environment Injection Usage
- Was `op run` used for environment injection?
- How was the .env.op template structured?
- What worked well or failed?

### 3. Security Patterns
- How was credential exposure prevented?
- Were there any close calls or mistakes?
- What safety checks were effective?

### 4. Integration Patterns
- How was 1Password integrated with other tools?
- What Python patterns were used?
- Any shell script integrations?

### 5. What Worked Well
- List patterns that contributed to success
- Note particularly effective approaches
- Identify what should be emphasized in workflow

### 6. What Failed or Required Workarounds
- List issues encountered
- Note the resolution for each
- Identify what could be anticipated in future

### 7. Workflow Gaps
- What did you need that the workflow didn't provide?
- What guidance would have been helpful?
- What's missing from the current workflow?

## Output Format

Return your analysis in YAML:

```yaml
project_summary:
  name: "[project name]"
  workflow_validated: "[workflow-id]"
  outcome: "successful | partial | failed"

credential_patterns:
  - type: "<credential type>"
    vault: "<vault name>"
    access_method: "<op read | op run | Python subprocess>"
    new_to_workflow: true | false

security_observations:
  - pattern: "<security pattern>"
    effective: true | false
    notes: "<additional context>"

integration_patterns:
  - tool: "<tool integrated with>"
    method: "<how integrated>"
    new_to_workflow: true | false

what_worked:
  - pattern: "<description>"
    should_emphasize: true | false

what_failed:
  - issue: "<issue>"
    resolution: "<resolution>"
    add_to_pitfalls: true | false

workflow_gaps:
  - gap: "<what's missing>"
    suggested_addition: "<what to add>"
    priority: "high | medium | low"

recommended_updates:
  - section: "<workflow section>"
    change_type: "add | modify | emphasize"
    description: "<what to change>"
```

Read all documents thoroughly before responding.
```

### 1.2 Validate Sub-Agent Output

**Expected:** YAML-structured analysis

**Validation Criteria:**
- [ ] All source documents were analyzed
- [ ] credential_patterns section populated
- [ ] workflow_gaps identified (even if empty)
- [ ] recommended_updates provided

---

## Phase 2: Document Extraction Results

**Autonomous:** YES

### 2.1 Create Extraction Record

Save the sub-agent output to the extraction file with front matter:

```yaml
---
extraction_id: "[YYYY-MM-DD]-[project-name]"
project: "[PROJECT_NAME]"
extraction_date: "[YYYY-MM-DD]"
source_documents:
  - "[doc1]"
  - "[doc2]"
target_workflow: "[workflow-id]"
status: "pending_integration"
---
```

### 2.2 Append Analysis

Add the sub-agent's YAML analysis under the front matter.

### 2.3 Add Integration Tracking Section

```markdown
## Integration Status

- **Extracted:** [date]
- **Integrated:** pending
- **Changes Made:** (to be filled after integration)
```

---

## Phase 3: Integration Planning

**Autonomous:** NO - Requires review

At this point, the extraction is complete. The next step is integration, which is covered in `integration-guide.md`.

### 3.1 Review Extraction

Before integration:
- [ ] Review the extraction with the user
- [ ] Confirm recommended_updates make sense
- [ ] Prioritize which changes to make
- [ ] Decide if workflow status should change (stub → draft, draft → validated, etc.)

### 3.2 Hand Off to Integration

Use the integration guide to:
1. Update the target workflow document
2. Update the extraction's integration status
3. Update the workflow's `validated_by` section

---

## Execution Record Template

```yaml
execution_record:
  started: null
  completed: null
  executor: null
  outcome: null

  phases_completed:
    - phase: 0
      status: pending
      notes: ""
    - phase: 1
      status: pending
      notes: ""
    - phase: 2
      status: pending
      notes: ""
    - phase: 3
      status: pending
      notes: ""

  extraction_file: null
  integration_status: "pending"
```

---

- **Template Status:** Active
- **Created:** 2025-12-15
