---
template_id: workflow-patterns-extraction
template_version: "1.0.0"
created: 2025-12-08
purpose: "Template for extracting workflow patterns from completed Crawl4AI projects"
audience: "Claude (LLM executor)"
---

# Workflow Patterns Extraction Template

- **Template Version:** 1.0.0
- **Purpose:** Extract reusable workflow patterns from a completed Crawl4AI project
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
  description: "[Brief description of what was crawled and why]"
  completion_date: "[YYYY-MM-DD]"

source_documents:
  # List all project artifacts that document how Crawl4AI was used
  - "[Path to project plan or requirements]"
  - "[Path to crawl architecture/strategy doc]"
  - "[Path to execution plan if exists]"
  - "[Path to synthesis/analysis plan if exists]"
  - "[Path to final output/report]"

target_workflows:
  # Which workflow(s) should this extraction inform?
  primary: "[workflow-id]"  # e.g., deep-company-research
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
ls -la "C:/Users/drewa/pbcs/pbc-web-crawling/tool-crawl4ai/workflows/[primary-workflow].md"
```

### 0.3 Create Extraction Output File

```bash
touch "C:/Users/drewa/pbcs/pbc-web-crawling/tool-crawl4ai/workflow-evolution/extractions/[output-filename].md"
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

### 1. Workflow Phases
- What distinct phases did this project have?
- What was the purpose of each phase?
- What were the inputs and outputs of each phase?
- How does this compare to the current workflow phases?

### 2. Source Identification Pattern
- What source types were crawled?
- How were sources categorized (primary vs secondary)?
- How was the crawl strategy chosen for each source type?
- Any new source types not in current workflow?

### 3. Script Usage
- Which PBC scripts were used?
- What parameters were effective?
- Any parameter combinations that should be documented?

### 4. Decision Points
- What decisions had to be made during execution?
- What criteria were used for those decisions?
- Any new decision points to add to workflow?

### 5. Fallback Strategies
- What issues were encountered?
- How were they resolved?
- What fallbacks should be documented?

### 6. What Worked Well
- List patterns that contributed to success
- Note particularly effective approaches
- Identify what should be emphasized in workflow

### 7. What Failed or Required Workarounds
- List issues encountered
- Note the resolution for each
- Identify what could be anticipated in future

### 8. Workflow Gaps
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

phases_observed:
  - phase_number: 0
    name: "<name>"
    purpose: "<purpose>"
    inputs: ["<input1>"]
    outputs: ["<output1>"]
    scripts_used: ["<script.py>"]
    new_to_workflow: true | false

source_patterns:
  - type: "<source type>"
    crawl_strategy: "<strategy>"
    script: "<script.py>"
    params: "<effective params>"
    new_to_workflow: true | false

decision_points:
  - decision: "<description>"
    criteria: "<how to decide>"
    documented_in_workflow: true | false

fallback_strategies:
  - issue: "<issue>"
    detection: "<how detected>"
    resolution: "<what to do>"
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
- [ ] phases_observed section populated
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
- **Created:** 2025-12-08
- **Based On:** Viktor.ai research project extraction
