---
workflow_id: competitive-analysis
title: "Competitive Analysis"
abstraction_level: low
status: stub
version: "0.1.0"
created: 2025-12-08
last_updated: 2025-12-08
validated_by: []
use_cases:
  - "Compare features across competing products"
  - "Analyze market positioning"
  - "Track competitor pricing and messaging"
  - "Identify differentiation opportunities"
scripts_used:
  - deep_crawl_docs.py
  - batch_urls_to_markdown.py
estimated_duration: "1-3 hours per competitor"
complexity: medium
---

# Competitive Analysis

- **Abstraction Level:** Low (decision tree)
- **Status:** Stub (not yet validated)
- **Last Updated:** 2025-12-08

## When to Use This Workflow

Use this workflow when you need to compare multiple companies or products to understand competitive positioning. This is appropriate for:

- Feature comparison across competitors
- Pricing analysis
- Market positioning research
- Identifying gaps and opportunities

## Decision Tree

### Step 1: Define Comparison Framework

Before crawling, establish what you're comparing:

- **Features:** Product capabilities, integrations, limitations
- **Pricing:** Tiers, pricing model, target customer size
- **Positioning:** Target market, messaging, value proposition
- **Technical:** Architecture, APIs, platform capabilities

### Step 2: Choose Sources Per Competitor

**For each competitor, prioritize:**

1. **Main website** (deep crawl) - Product messaging, features
2. **Pricing page** (single URL) - Pricing model
3. **Documentation** (deep crawl if available) - Technical capabilities
4. **Case studies/customers** (batch URLs) - Use cases, outcomes

### Step 3: Structure Output for Comparison

Create consistent directory structure per competitor:

```
research/competitive-analysis/
├── competitor-a/
│   ├── main-site/
│   ├── pricing/
│   └── docs/
├── competitor-b/
│   ├── main-site/
│   ├── pricing/
│   └── docs/
└── comparison-notes.md
```

## Script Reference

| Script | When to Use | Key Parameters |
|--------|-------------|----------------|
| `deep_crawl_docs.py` | Main site, documentation | `--max-depth 2 --max-pages 50` (per competitor) |
| `batch_urls_to_markdown.py` | Specific pages (pricing, features) | `--urls [pricing] [features]` |
| `url_to_markdown.py` | Single comparison page | `[url] -o pricing.md` |

## Common Pitfalls

- **Scope creep:** Crawling too deep per competitor. Solution: Limit to 50 pages per competitor.
- **Inconsistent structure:** Different output structures make comparison hard. Solution: Use consistent directory template.
- **Missing pricing:** Some competitors hide pricing. Solution: Note "Contact sales" and check review sites.
- **Outdated content:** Cached pages may be stale. Solution: Use `cache_mode=BYPASS`.

## Examples

### Example: Crawl Competitor Main Site

```bash
PBC_VENV="C:/Users/drewa/pbcs/pbc-web-crawling/.venv/Scripts/python.exe"
PBC_SCRIPTS="C:/Users/drewa/pbcs/pbc-web-crawling/scripts"

# Competitor A
"$PBC_VENV" "$PBC_SCRIPTS/deep_crawl_docs.py" \
    "https://competitor-a.com" \
    --output-dir "./research/competitive/competitor-a/main-site" \
    --max-depth 2 \
    --max-pages 50

# Competitor B
"$PBC_VENV" "$PBC_SCRIPTS/deep_crawl_docs.py" \
    "https://competitor-b.com" \
    --output-dir "./research/competitive/competitor-b/main-site" \
    --max-depth 2 \
    --max-pages 50
```

### Example: Batch Crawl Key Pages

```bash
"$PBC_VENV" "$PBC_SCRIPTS/batch_urls_to_markdown.py" \
    --urls \
    "https://competitor-a.com/pricing" \
    "https://competitor-a.com/features" \
    "https://competitor-a.com/enterprise" \
    --output-dir "./research/competitive/competitor-a/key-pages"
```

## Comparison Template

After crawling, create comparison notes:

```markdown
# Competitive Analysis: [Category]

## Feature Comparison

| Feature | Competitor A | Competitor B | Our Product |
|---------|--------------|--------------|-------------|
| [Feature 1] | Yes/No/Details | Yes/No/Details | Yes/No/Details |

## Pricing Comparison

| Tier | Competitor A | Competitor B | Our Product |
|------|--------------|--------------|-------------|
| Starter | $X/mo | $Y/mo | $Z/mo |

## Positioning

| Aspect | Competitor A | Competitor B |
|--------|--------------|--------------|
| Target Market | ... | ... |
| Key Message | ... | ... |
```

## Related Documentation

- [Deep Company Research](deep-company-research.md) - For deeper single-company analysis
- [Deep Crawling](../docs/07-crawl4ai-deep-crawling-2025-12-03.md)

---

- **Document Status:** Stub
- **Next Review:** After first validation
