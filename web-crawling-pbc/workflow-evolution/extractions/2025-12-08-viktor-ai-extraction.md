---
extraction_id: 2025-12-08-viktor-ai
project: "Viktor.ai Deep Company Research"
extraction_date: 2025-12-08
source_documents:
  - "viktor-ai-research-project-plan.md"
  - "viktor-ai-crawl-architecture.md"
  - "2025-12-08-viktor-ai-crawl-execution-plan.md"
  - "viktor-ai-synthesis-plan.md"
  - "viktor-ai-research-report.md"
source_location: "C:/Users/drewa/work/knowledge/hdr-consulting-opp-project/viktor-ai-research/"
target_workflow: "deep-company-research"
status: "integrated"
---

# Viktor.ai Research Project - Workflow Patterns Extraction

- **Project:** Viktor.ai Deep Company Research
- **Extraction Date:** 2025-12-08
- **Target Workflow:** deep-company-research.md
- **Outcome:** Successful - created initial MEDIUM-level workflow

## Context

This was the first project to use the web-crawling PBC for deep company research. The objective was to research Viktor.ai (a low-code engineering platform) to answer the question: "Is Viktor.ai a viable platform for building custom engineering applications for AEC industry clients?"

The project produced a comprehensive research report and informed the creation of the Deep Company Research workflow.

## Extraction Analysis

```yaml
project_summary:
  name: "Viktor.ai Deep Company Research"
  workflow_validated: "deep-company-research"
  outcome: "successful"
  notes: "First validation - produced comprehensive research report answering critical business question"

phases_observed:
  - phase_number: 0
    name: "Project Planning"
    purpose: "Define research objectives and success criteria"
    inputs: ["Business question", "Initial company knowledge"]
    outputs: ["Research plan document", "Source identification"]
    scripts_used: []
    new_to_workflow: false

  - phase_number: 1
    name: "Crawl Architecture"
    purpose: "Design source categorization and crawl strategy"
    inputs: ["Research objectives", "Initial source URLs"]
    outputs: ["Categorized source list", "Per-source crawl parameters"]
    scripts_used: []
    new_to_workflow: false

  - phase_number: 2
    name: "Content Acquisition"
    purpose: "Execute crawls and capture content"
    inputs: ["Crawl architecture", "PBC scripts"]
    outputs: ["Markdown files organized by source"]
    scripts_used:
      - "deep_crawl_docs.py"
      - "batch_urls_to_markdown.py"
    new_to_workflow: false

  - phase_number: 3
    name: "Synthesis"
    purpose: "Analyze content and extract insights"
    inputs: ["Crawled content", "Research questions"]
    outputs: ["Analysis by category", "Answers to research questions"]
    scripts_used: []
    new_to_workflow: false

  - phase_number: 4
    name: "Report Assembly"
    purpose: "Compile findings into deliverable format"
    inputs: ["Synthesis outputs", "Original objectives"]
    outputs: ["Final research report"]
    scripts_used: []
    new_to_workflow: false

source_patterns:
  primary_sources:
    - type: "Main website"
      crawl_strategy: "Shallow depth, capture key pages"
      script: "deep_crawl_docs.py"
      params: "--max-depth 3 --max-pages 100"
      notes: "Good for marketing positioning, pricing, about pages"

    - type: "Documentation site"
      crawl_strategy: "Deep crawl following doc structure"
      script: "deep_crawl_docs.py"
      params: "--max-depth 4 --max-pages 200"
      notes: "Captures SDK reference, tutorials, architecture"

    - type: "GitHub organization"
      crawl_strategy: "Selective - readme and key repos"
      script: "batch_urls_to_markdown.py"
      params: "Manual URL list of repo pages"
      notes: "GitHub pages render well; capture examples, patterns"

  secondary_sources:
    - type: "Funding/news articles"
      crawl_strategy: "Individual page capture"
      script: "batch_urls_to_markdown.py"
      params: "Specific article URLs"
      notes: "External validation, funding history, press coverage"

decision_points:
  - decision: "When to use deep_crawl vs batch_urls"
    criteria: "Nested/linked content = deep_crawl; Curated URL list = batch_urls"
    documented_in_workflow: true

  - decision: "Primary vs secondary source classification"
    criteria: "Primary = official company-controlled; Secondary = external/third-party"
    documented_in_workflow: true

  - decision: "Crawl depth and page limits"
    criteria: "Based on site structure and content density; start conservative, increase if needed"
    documented_in_workflow: true

  - decision: "How to distribute synthesis work"
    criteria: "Parallel sub-agents for independent content categories; sequential for dependencies"
    documented_in_workflow: true

fallback_strategies:
  - issue: "Blocked or rate-limited requests"
    detection: "Empty or error responses"
    resolution: "Reduce concurrency, add delays, or use batch_urls for specific pages"
    new_to_workflow: false

  - issue: "JavaScript-rendered content not captured"
    detection: "Missing expected content in output"
    resolution: "Document limitation; consider alternative sources"
    new_to_workflow: false

  - issue: "Overwhelming content volume"
    detection: "Thousands of pages returned"
    resolution: "Reduce max-pages, increase depth selectivity, or target specific subsections"
    new_to_workflow: false

what_worked:
  - pattern: "LLM-executable execution plans with bash scripts"
    should_emphasize: true
    notes: "Plans that Claude can execute autonomously reduce back-and-forth"

  - pattern: "Sub-agent distribution for parallel analysis"
    should_emphasize: true
    notes: "Keeps main context clean; enables parallel processing of large content sets"

  - pattern: "YAML output format for sub-agent results"
    should_emphasize: true
    notes: "Structured output is easier to integrate than free-form text"

  - pattern: "Source-to-strategy mapping before execution"
    should_emphasize: true
    notes: "Planning crawl approach per source type prevents wasted effort"

  - pattern: "Pre-flight validation phase"
    should_emphasize: true
    notes: "Catching issues early (missing files, wrong paths) saves time"

what_failed:
  - issue: "Initial underestimation of documentation site depth"
    resolution: "Increased max-pages parameter mid-execution"
    add_to_pitfalls: true
    notes: "Docusaurus sites can be deeper than expected"

  - issue: "Windows path escaping with trailing backslashes"
    resolution: "Use forward slashes in bash commands"
    add_to_pitfalls: true
    notes: "Windows-specific issue with bash tool"

workflow_gaps:
  - gap: "No guidance on output organization structure"
    suggested_addition: "Add section on recommended directory structure for crawled content"
    priority: "medium"

  - gap: "No guidance on sub-agent prompt structure"
    suggested_addition: "Include template for synthesis sub-agent prompts"
    priority: "medium"

  - gap: "No guidance on what makes a good research question"
    suggested_addition: "Add section on formulating answerable research questions"
    priority: "low"

recommended_updates:
  - section: "Phase 2: Content Acquisition"
    change_type: "emphasize"
    description: "Stress the importance of source-to-strategy mapping before execution"

  - section: "Common Pitfalls"
    change_type: "add"
    description: "Add documentation site depth estimation; Windows path escaping"

  - section: "Output Structure"
    change_type: "add"
    description: "Add recommended directory structure for organizing crawled content"
```

## Integration Status

- **Extracted:** 2025-12-08
- **Integrated:** 2025-12-08
- **Changes Made:**
  - Created `deep-company-research.md` workflow (MEDIUM level)
  - Workflow status set to "draft" with Viktor.ai as first validation
  - Incorporated all 5 phases into workflow structure
  - Added fallback strategies table
  - Added lessons learned section

## Original Execution Context

This extraction was performed as part of the initial workflow patterns extraction effort. The Viktor.ai project documents were analyzed by a sub-agent, and the findings were used to create the first MEDIUM-level workflow in the web-crawling PBC.

### Execution Timeline

- **Project Execution:** 2025-12-08 (crawling and synthesis)
- **Patterns Extraction:** 2025-12-08
- **Workflow Creation:** 2025-12-08

### Files Produced by Original Project

The Viktor.ai research artifacts now reside at:
`C:/Users/drewa/work/knowledge/hdr-consulting-opp-project/viktor-ai-research/`

---

- **Document Status:** Integrated
- **Created:** 2025-12-08
- **Workflow Updated:** deep-company-research.md (draft status)
