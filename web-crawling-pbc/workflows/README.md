# Web Crawling PBC - Workflows

Reusable workflow patterns for common Crawl4AI use cases.

- **Location:** `C:\Users\drewa\pbcs\web-crawling-pbc\workflows\`
- **Last Updated:** 2025-12-08

## Workflow Index

| Workflow | Abstraction | Status | Use Case |
|----------|-------------|--------|----------|
| [Deep Company Research](deep-company-research.md) | Medium | Draft | Research a company's products, positioning, technical architecture |
| [Documentation Ingestion](documentation-ingestion.md) | Low | Stub | Crawl documentation sites for RAG indexing |
| [Competitive Analysis](competitive-analysis.md) | Low | Stub | Compare multiple companies/products |
| [News Monitoring](news-monitoring.md) | Low | Stub | Track news and articles about topics |
| [Knowledge Base Building](knowledge-base-building.md) | Low | Stub | Build reference collections from web sources |

## Abstraction Levels

- **Low (Decision Tree):** When to use which script, key parameters, common pitfalls
- **Medium (Workflow Template):** Multi-phase patterns with decision points and validation
- **High (Execution Plan):** Full LLM-executable plans with bash scripts (future)

## Workflow Maturity

| Status | Description |
|--------|-------------|
| **Stub** | Placeholder with basic structure, not yet validated |
| **Draft** | Initial content, needs validation through real project |
| **Validated** | Used successfully in at least one project |
| **Mature** | Multiple successful uses, refined based on learnings |

## How Workflows Evolve

1. **Stub** - Created for hypothetical use case
2. **Draft** - Fleshed out with initial patterns
3. **Validated** - After first successful project use, update `validated_by` in front matter
4. **Mature** - After 3+ uses, patterns are reliable

### After Completing a Project

When you complete a project using a workflow:

1. Update the workflow's `validated_by` section in YAML front matter
2. Add any new learnings to "Lessons Learned" section
3. Update `last_updated` date
4. Consider bumping `version` if significant changes
5. If new fallback strategies discovered, add to "Fallback Strategies" table

### Promoting Workflow Status

| From | To | Criteria |
|------|----|----------|
| Stub | Draft | Initial patterns documented |
| Draft | Validated | 1 successful project use |
| Validated | Mature | 3+ successful uses, patterns refined |

## Related Documentation

- [PBC Definition](../pbc-definition.yaml) - Formal capability specification
- [CLAUDE.md](../CLAUDE.md) - Instructions for Claude
- [Scripts](../scripts/) - The actual crawling tools
- [Crawl4AI Docs](../docs/) - Reference documentation

---

- **Document Status:** Active
- **Created:** 2025-12-08
- **Next Review:** After next workflow validation
