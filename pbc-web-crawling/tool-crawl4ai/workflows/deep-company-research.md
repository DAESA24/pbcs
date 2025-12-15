---
workflow_id: deep-company-research
title: "Deep Company Research"
abstraction_level: medium
status: draft
version: "0.1.0"
created: 2025-12-08
last_updated: 2025-12-08
validated_by:
  - project: "viktor-ai-research"
    date: 2025-12-08
    outcome: "successful"
    notes: "First validation - produced comprehensive research report answering critical business question about product positioning"
use_cases:
  - "Company due diligence"
  - "Partnership evaluation"
  - "Competitive positioning analysis"
  - "Vendor assessment"
  - "Investment research"
scripts_used:
  - deep_crawl_docs.py
  - batch_urls_to_markdown.py
  - url_to_markdown.py
estimated_duration: "4-8 hours (planning through final report)"
complexity: medium
---

# Deep Company Research

- **Abstraction Level:** Medium (workflow template)
- **Status:** Draft (validated by viktor-ai-research)
- **Last Updated:** 2025-12-08

## When to Use This Workflow

Use this workflow when you need to deeply research a company to answer a strategic business question. This is appropriate when:

- You have a specific critical question to answer (not just "learn about company X")
- Multiple source types are needed (website, docs, GitHub, company info)
- The answer requires synthesizing evidence across sources
- Output is a structured research report with strategic implications

**Not suitable for:** Quick lookups, single-page extraction, or monitoring ongoing news.

## Workflow Phases Overview

| Phase | Name | Purpose | Scripts Used | Execution Pattern |
|-------|------|---------|--------------|-------------------|
| 0 | Project Planning | Define objectives, identify critical question, inventory sources | None | Conversational |
| 1 | Crawl Architecture | Map sources to crawl strategies, design output structure | None | Conversational |
| 2 | Content Acquisition | Execute crawls autonomously to gather all content | deep_crawl_docs.py, batch_urls_to_markdown.py | Docs-as-code (autonomous bash) |
| 3 | Synthesis | Analyze content via parallel sub-agents | None | Sub-agents |
| 4 | Report Assembly | Compile agent outputs into final report | None | Conversational |

## Phase Details

### Phase 0: Project Planning

**Purpose:** Define the research scope and success criteria before any crawling begins.

**Inputs:**
- Business context (why is this research needed?)
- The strategic decision this research will inform

**Outputs:**
- Research project plan document
- Critical question clearly stated
- Research objectives prioritized (P1-P4 primary, S1-S5 secondary)
- Source inventory (primary vs secondary)

#### Steps

1. **Define the Critical Question**
   - What specific question must this research answer?
   - How will the answer inform business decisions?
   - Example: "Is [Company] an internal tool OR a client delivery platform?"

2. **List Research Objectives**
   - Primary (P1-P4): Must answer to address critical question
   - Secondary (S1-S5): Nice-to-have context

3. **Inventory Potential Sources**
   - Primary: Company website, documentation, GitHub
   - Secondary: Funding sources, news, third-party profiles

#### Validation

- [ ] Critical question is specific and answerable
- [ ] At least 3 primary sources identified
- [ ] Clear success criteria defined

---

### Phase 1: Crawl Architecture Design

**Purpose:** Map each source to the appropriate Crawl4AI script and parameters.

**Inputs:**
- Source inventory from Phase 0
- Available scripts in PBC

**Outputs:**
- Crawl architecture document with source-to-strategy mapping
- Output directory structure design
- Pre-flight validation checklist

#### Source-to-Strategy Mapping

| Source Type | Crawl Strategy | Script | Typical Parameters |
|-------------|----------------|--------|-------------------|
| Company main site | Deep BFS crawl | `deep_crawl_docs.py` | `--max-depth 3 --max-pages 100` |
| Documentation site | Deep crawl OR batch URLs | `deep_crawl_docs.py` or `batch_urls_to_markdown.py` | `--max-depth 4 --max-pages 200` |
| GitHub organization | Two-phase: org pages → repo crawls | `batch_urls_to_markdown.py` then `deep_crawl_docs.py` | Org: batch 3 URLs; Repos: `--max-depth 2 --max-pages 30` each |
| Company info pages | Batch or single URL | `batch_urls_to_markdown.py` | 5-10 URLs (/about, /team, /pricing, /careers) |
| News/articles | Batch URLs | `batch_urls_to_markdown.py` | Discovered article URLs |

#### Output Directory Structure Template

```
research/[company-name]/
├── primary/
│   ├── main-site/           # Deep crawl of main website
│   │   ├── customer-cases/  # Often richest source
│   │   └── screenshots/     # Manual captures if needed
│   ├── docs/                # Documentation site content
│   └── github/
│       ├── org/             # Organization overview pages
│       └── repos/           # Individual repository content
└── secondary/
    ├── funding/             # Company background
    └── news/                # Press coverage
```

#### Validation

- [ ] Every source has a script assignment
- [ ] Parameters appropriate for expected site size
- [ ] Output directory structure designed

---

### Phase 2: Content Acquisition (Autonomous Execution)

**Purpose:** Execute all crawls via autonomous bash scripts.

**Inputs:**
- Crawl architecture document
- Pre-flight validation requirements

**Outputs:**
- Markdown files organized by source type
- Execution log with file counts
- Issue resolution notes

#### Pre-Flight Validation Checklist

```bash
# 1. Verify PBC venv accessible
ls "C:\Users\drewa\pbcs\pbc-web-crawling\tool-crawl4ai\.venv\Scripts\python.exe"

# 2. Verify scripts exist
ls "C:\Users\drewa\pbcs\pbc-web-crawling\tool-crawl4ai\scripts\"

# 3. Check target URLs reachable
curl -I https://[company].com

# 4. Create output directories
mkdir -p research/[company]/primary/{main-site,docs,github/{org,repos}}
mkdir -p research/[company]/secondary/{funding,news}
```

#### Execution Script Structure

Each phase should be a self-contained bash block:

```bash
# === PHASE: [Source Name] ===
echo "Starting [source] crawl..."

# Define paths
PBC_VENV="C:/Users/drewa/pbcs/pbc-web-crawling/tool-crawl4ai/.venv/Scripts/python.exe"
PBC_SCRIPTS="C:/Users/drewa/pbcs/pbc-web-crawling/tool-crawl4ai/scripts"
OUTPUT_DIR="[absolute path to output]"

# Execute crawl
"$PBC_VENV" "$PBC_SCRIPTS/[script].py" [params] --output-dir "$OUTPUT_DIR"

# Validate
echo "Files created:"
ls "$OUTPUT_DIR" | wc -l
```

#### Conditional Execution Logic

For optional sources, use conditional logic:

```bash
# Check if docs URL exists in crawled content
DOCS_URL=$(grep -r "docs\." research/[company]/primary/main-site/ | head -1)

if [ -n "$DOCS_URL" ]; then
    echo "Docs URL found, crawling documentation..."
    # Execute docs crawl
else
    echo "No docs URL found, skipping documentation crawl"
fi
```

#### File Count Validation

After all crawls complete:

```bash
echo "=== Content Acquisition Summary ==="
echo "Main site: $(find research/[company]/primary/main-site -name '*.md' | wc -l) files"
echo "Docs: $(find research/[company]/primary/docs -name '*.md' | wc -l) files"
echo "GitHub: $(find research/[company]/primary/github -name '*.md' | wc -l) files"
echo "Secondary: $(find research/[company]/secondary -name '*.md' | wc -l) files"
echo "TOTAL: $(find research/[company] -name '*.md' | wc -l) files"
```

**Success Threshold:** >= 10 total files before proceeding to synthesis

#### Validation

- [ ] Pre-flight checks passed
- [ ] All phases executed (or gracefully skipped)
- [ ] File count >= 10
- [ ] No critical errors in execution log

---

### Phase 3: Synthesis via Sub-Agents

**Purpose:** Analyze crawled content to answer research objectives.

**Inputs:**
- All crawled markdown files
- Research objectives from Phase 0
- Critical question to answer

**Outputs:**
- Analysis sections by topic
- Evidence-based answer to critical question
- Strategic implications

#### Agent Distribution Pattern

| Agent | Input Content | Analysis Task | Output Section |
|-------|---------------|---------------|----------------|
| Agent 1 | main-site/*.md (non-customer-cases) | Product positioning, features, messaging | Product Analysis |
| Agent 2 | main-site/customer-cases/**/*.md | Use cases, industries, outcomes | Use Cases & Industries |
| Agent 3 | github/repos/*.md + docs/*.md | Technical architecture, integrations | Technical Architecture |
| Agent 4 | secondary/**/*.md + screenshots/ | Company background, pricing, team | Company & Pricing |
| Agent 5 | All agent outputs | Cross-reference → answer critical question | Strategic Implications |

**Execution Order:**
- Agents 1-4: Run in parallel (no dependencies)
- Agent 5: Run after 1-4 complete (requires their outputs)

#### Agent Output Format Template

Each agent should return:

```markdown
## [Section Name]

### Key Findings

- [Finding 1 with source citation]
- [Finding 2 with source citation]

### Evidence Table

| Finding | Evidence | Source File |
|---------|----------|-------------|
| [finding] | [quote or description] | [filename.md] |

### Summary

[2-3 sentences linking findings to research objectives]
```

#### Agent 5 (Cross-Reference) Output Format

```markdown
## Strategic Implications

### Verdict: [Answer to Critical Question]

**Confidence Level:** High | Medium | Low

### Supporting Evidence

| Evidence Type | Finding | Source |
|---------------|---------|--------|
| [type] | [finding] | [agent/source] |

### Counter-Evidence Considered

[Any evidence that contradicts the verdict, and why it was weighted lower]

### Implications for [Business Context]

- [Implication 1]
- [Implication 2]

### Recommended Talking Points

- [Point 1]
- [Point 2]
```

#### Validation

- [ ] All 4 content agents completed
- [ ] Agent 5 provided clear verdict with confidence level
- [ ] Evidence table populated with source citations

---

### Phase 4: Report Assembly

**Purpose:** Compile all outputs into the final research report.

**Inputs:**
- All agent analysis outputs
- Content inventory from Phase 2

**Outputs:**
- Final research report document
- Executive summary
- Appendix with source index

#### Report Structure Template

```markdown
# [Company Name] Research Report

- **Date:** [YYYY-MM-DD]
- **Critical Question:** [The question this research answers]
- **Verdict:** [One-line answer]

## Executive Summary

[3-5 bullet points summarizing key findings and strategic implications]

## Company Overview

[From Agent 4 - background, funding, team size, HQ location]

## Product Analysis

[From Agent 1 - what they offer, positioning, target market]

## Use Cases & Industries

[From Agent 2 - detailed examples, outcomes, customer profiles]

## Pricing Model

[From Agent 4 - pricing tiers, target company size]

## Technical Architecture

[From Agent 3 - platform capabilities, integrations, SDK patterns]

## Strategic Implications

[From Agent 5 - THE KEY SECTION - verdict with evidence]

## Appendix

### Content Inventory

| Source Type | File Count | Location |
|-------------|------------|----------|
| Main Site | [n] | research/[company]/primary/main-site/ |
| Docs | [n] | research/[company]/primary/docs/ |
| GitHub | [n] | research/[company]/primary/github/ |
| Secondary | [n] | research/[company]/secondary/ |

### Sources Consulted

[List of key URLs crawled]
```

#### Validation

- [ ] All sections populated
- [ ] Executive summary captures key points
- [ ] Strategic implications clearly answer critical question
- [ ] Appendix includes content inventory

---

## Fallback Strategies

| Issue | Detection | Resolution |
|-------|-----------|------------|
| Docusaurus/SPA docs site blocks deep crawl | Low file count from docs crawl despite large visible site | Extract specific doc URLs from main site links, use `batch_urls_to_markdown.py` |
| Crunchbase/LinkedIn blocked (403/999) | curl pre-check or crawl returns error | Use company's own /about, /team, /pricing, /careers pages |
| Assumed GitHub repos don't exist | 404 on curl pre-check | Discover actual repos from org page grep, crawl those instead |
| Key product features not in text | Synthesis reveals understanding gaps | Manual screenshot capture of key UI pages |
| Deep crawl returns mostly boilerplate | Many files but low unique content | Adjust excluded_tags, use content filters, or switch to targeted batch URLs |

## Lessons Learned

### From viktor-ai-research (2025-12-08)

**What worked well:**
- Customer case studies were richest source (60+ detailed examples vs 18 limited doc pages)
- Two-phase GitHub strategy (org overview first, then targeted repo crawls) discovered actual repos
- Conditional execution logic prevented blocking on optional sources
- Fallback from Crunchbase to company's own /about pages worked seamlessly
- File count validation provided immediate feedback on crawl success
- Parallel sub-agents for synthesis had no resource contention issues

**What required workarounds:**
- Docusaurus documentation site blocked deep crawling → switched to batch URLs
- Crunchbase/LinkedIn returned 403/999 → used company's own pages
- Initial synthesis plan overestimated docs value, underestimated customer cases

**Recommendations:**
- After Phase 2, review file counts by source type and adjust agent assignments based on actual content richness
- Detect Docusaurus/SPA patterns in pre-flight; default to batch strategy with URL extraction step
- Prioritize company's own pages over third-party aggregators for company info
- Plan for screenshot phase when visual evidence is critical to research question

## Related Documentation

- [PBC Scripts](../scripts/) - The crawling tools
- [Deep Crawling Docs](../docs/07-crawl4ai-deep-crawling-2025-12-03.md) - BFS/BestFirst strategies
- [Batch URL Docs](../docs/06-crawl4ai-multi-url-crawling-2025-12-03.md) - Concurrent URL processing

---

- **Document Status:** Draft (validated by 1 project)
- **Validated By:** viktor-ai-research (2025-12-08, successful)
- **Next Review:** After next company research project
