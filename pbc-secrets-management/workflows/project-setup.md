---
workflow_id: project-setup
title: "Setting Up New Projects with 1Password"
abstraction_level: low
status: stub
version: "0.1.0"
created: 2025-12-15
last_updated: 2025-12-15
validated_by: []
use_cases:
  - "Initialize credential management for new project"
  - "Create vault items for project secrets"
  - "Set up .env.op templates"
  - "Establish secure credential patterns"
scripts_used: []
estimated_duration: "15-30 minutes"
complexity: low
---

# Setting Up New Projects with 1Password

- **Abstraction Level:** Low (decision tree)
- **Status:** Stub (not yet validated)
- **Last Updated:** 2025-12-15

## When to Use This Workflow

Use this workflow when starting a new project that needs:

- API credentials
- Database connections
- OAuth tokens
- Any secret management

## Decision Tree

### Step 1: Identify Required Credentials

List all credentials the project needs:

| Credential | Purpose | Vault |
|------------|---------|-------|
| Database URL | PostgreSQL connection | Credentials-Dev Project |
| API Key | Third-party service | Credentials-Dev Project |
| OAuth Token | Authentication | Credentials-Workflow Tools (if shared) |

### Step 2: Create Vault Items

```bash
# Create a new credential item
op item create --category="API Credential" \
  --title="myproject-database" \
  --vault="Credentials-Dev Project" \
  "connection_string=postgresql://user:pass@host:5432/db"

# Create with generated password
op item create --category=Login \
  --title="myproject-admin" \
  --vault="Credentials-Dev Project" \
  --generate-password \
  "username=admin"
```

### Step 3: Create .env.op Template

```bash
# .env.op - Template with secret references
DATABASE_URL=op://Credentials-Dev Project/myproject-database/connection_string
API_KEY=op://Credentials-Dev Project/myproject-api/api_key
```

### Step 4: Update .gitignore

```gitignore
# Secrets
.env
.env.local
*.pem
*.key

# Safe to commit
# .env.op  (this is just references)
```

### Step 5: Document in Project README

Add to project documentation:

```markdown
## Credentials

This project uses 1Password CLI for secret management.

### Setup
1. Ensure `op` CLI is installed and authenticated
2. Run commands with: `op run --env-file .env.op -- [command]`

### Required Credentials
- `myproject-database` in Credentials-Dev Project vault
- `myproject-api` in Credentials-Dev Project vault
```

## Naming Convention

Follow the PBC naming patterns:

**Credentials-Dev Project:** `{project}-{service}`
- `myproject-database`
- `myproject-stripe`
- `myproject-aws`

**Credentials-Workflow Tools:** `{service}-{scope}`
- `github-pat` (shared across projects)
- `email-automation`

## Verification Checklist

```bash
# 1. Verify items exist
op item list --vault "Credentials-Dev Project" | grep myproject

# 2. Test secret retrieval
op read "op://Credentials-Dev Project/myproject-database/connection_string" > /dev/null && echo "OK"

# 3. Test env injection
op run --env-file .env.op -- python -c "import os; print('Configured:', bool(os.getenv('DATABASE_URL')))"
```

## Common Pitfalls

- **Wrong vault:** Project-specific credentials go in `Credentials-Dev Project`, not workflow tools.
- **Inconsistent naming:** Use `{project}-{service}` pattern consistently.
- **Missing .gitignore:** Always exclude `.env` files.
- **Hardcoded fallbacks:** Don't add fallback values that expose test credentials.

## Security Checklist

- [ ] All credentials stored in 1Password (not in code/config)
- [ ] `.env.op` template created with references
- [ ] `.env` excluded from git
- [ ] Project README documents credential setup
- [ ] No test/default credentials in code

## Related Documentation

- [Creating Items](../docs/cli-commands-item.md)
- [Best Practices](../docs/best-practices.md)
- [Secret References](../docs/secret-references.md)

---

- **Document Status:** Stub
- **Next Review:** After first validation
