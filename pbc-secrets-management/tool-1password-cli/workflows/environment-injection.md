---
workflow_id: environment-injection
title: "Environment Variable Injection with op run"
abstraction_level: low
status: stub
version: "0.1.0"
created: 2025-12-15
last_updated: 2025-12-15
validated_by: []
use_cases:
  - "Run scripts with secrets as environment variables"
  - "Replace .env files with secure references"
  - "Execute builds with injected credentials"
  - "Run Docker containers with secrets"
scripts_used: []
estimated_duration: "5-15 minutes setup"
complexity: low
---

# Environment Variable Injection with op run

- **Abstraction Level:** Low (decision tree)
- **Status:** Stub (not yet validated)
- **Last Updated:** 2025-12-15

## When to Use This Workflow

Use this workflow when you need to:

- Run scripts that expect credentials in environment variables
- Replace insecure `.env` files with 1Password references
- Execute commands with secrets without exposing them

## Decision Tree

### Step 1: Create .env.op Template

Create a template file with `op://` references instead of actual values:

```bash
# .env.op - Template with secret references
DATABASE_URL=op://Credentials-Dev Project/myapp-database/connection_string
API_KEY=op://Credentials-Dev Project/myapp-api/api_key
GITHUB_TOKEN=op://Credentials-Workflow Tools/github-pat/credential
```

### Step 2: Run Command with Injection

```bash
# Run any command with secrets injected
op run --env-file .env.op -- python script.py

# Run npm scripts
op run --env-file .env.op -- npm run build

# Run with inline secrets (single var)
op run --env "API_KEY=op://vault/item/field" -- curl https://api.example.com
```

### Step 3: Verify Setup

```bash
# Test that environment variables are available (without printing values!)
op run --env-file .env.op -- python -c "import os; print('DB URL set:', bool(os.getenv('DATABASE_URL')))"
```

## File Structure

```
project/
├── .env.op          # Template with op:// references (safe to commit)
├── .env             # NEVER commit - local overrides only
├── .gitignore       # Must include .env
└── script.py        # Uses os.getenv() normally
```

## Common Patterns

### Python Script Expecting Environment Variables

```python
import os

# Script doesn't know about 1Password - just reads env vars
db_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")

# Use credentials directly
# NEVER print(db_url) or similar
```

**Run with:**
```bash
op run --env-file .env.op -- python script.py
```

### Docker Container

```bash
# Pass secrets to container
op run --env-file .env.op -- docker run -e DATABASE_URL -e API_KEY myimage
```

### npm/Node Scripts

```bash
op run --env-file .env.op -- npm run start
```

## Common Pitfalls

- **Committing .env:** Always add `.env` to `.gitignore`. The `.env.op` template is safe to commit.
- **Missing op run:** If script runs without `op run`, env vars will literally be "op://..." strings.
- **Debug output:** Many frameworks log environment variables on startup. Check logs don't expose secrets.

## Security Checklist

- [ ] `.env` is in `.gitignore`
- [ ] `.env.op` contains only references, no actual secrets
- [ ] Scripts don't print environment variable values
- [ ] Logs are checked for credential leakage

## Related Documentation

- [op run Command](../docs/cli-commands-run.md)
- [Secrets in Environment Variables](../docs/secrets-environment-variables.md)
- [Secrets in Config Files](../docs/secrets-config-files.md)

---

- **Document Status:** Stub
- **Next Review:** After first validation
