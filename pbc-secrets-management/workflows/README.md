# 1Password CLI PBC - Workflows

Reusable workflow patterns for common 1Password CLI use cases.

- **Location:** `C:\Users\drewa\pbcs\pbc-secrets-management\workflows\`
- **Last Updated:** 2025-12-15

## Workflow Index

| Workflow | Abstraction | Status | Use Case |
|----------|-------------|--------|----------|
| [Credential Retrieval](credential-retrieval.md) | Low | Stub | Patterns for getting secrets securely |
| [Environment Injection](environment-injection.md) | Low | Stub | Using `op run` for env vars in scripts |
| [Project Setup](project-setup.md) | Low | Stub | Setting up new projects with 1Password |

## Abstraction Levels

- **Low (Decision Tree):** When to use which command, key parameters, common pitfalls
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
- [1Password CLI Docs](../docs/) - Reference documentation

---

- **Document Status:** Active
- **Created:** 2025-12-15
- **Next Review:** After next workflow validation
