# 1Password CLI PBC

Secure credential management for development workflows using 1Password CLI.

- **Status:** Experimental
- **Created:** 2025-12-15
- **Version:** 0.1.0
- **Role:** Credential management

## What This PBC Provides

- Secure secret retrieval via `op://` references
- Environment variable injection with `op run`
- Vault and item management patterns
- Python integration for credential access
- SSH key management

## Tool Inventory

### Global CLI Tool

| Tool | Command | Installed Via |
|------|---------|---------------|
| 1Password CLI | `op` | [1Password CLI installer](https://developer.1password.com/docs/cli/get-started/) |

**Prerequisites:**
- 1Password account
- 1Password CLI installed and authenticated
- Biometric unlock enabled (recommended)

## Quick Reference

### Essential Commands

```bash
# Read a secret value
op read "op://vault/item/field"

# List items in a vault
op item list --vault "Credentials-Workflow Tools"

# Inject secrets into a command's environment
op run --env-file .env.op -- python script.py

# Check authentication status
op whoami

# Sign in (if session expired)
op signin
```

### Secret Reference Syntax

Format: `op://vault/item/field`

```
op://Credentials-Workflow Tools/google-calendar-personal/token
op://Credentials-Dev Project/myapp-api/api_key
op://Credentials-Workflow Tools/github-pat/credential
```

## Vault Architecture

| Vault | Purpose | Example Items |
|-------|---------|---------------|
| **Credentials-Workflow Tools** | Personal tooling, cross-project | `google-calendar-personal`, `github-pat`, `email-automation` |
| **Credentials-Dev Project** | Project-specific secrets | `myapp-database`, `myapp-stripe`, `clientsite-hosting` |

### Naming Conventions

**Workflow Tools:** `{service}-{scope}` (e.g., `google-calendar-personal`)

**Dev Project:** `{project}-{service}` (e.g., `myapp-database`)

## Python Integration

Use the `op_credential_utils.py` module for credential retrieval in Python scripts:

```python
import sys
sys.path.insert(0, r"C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\scripts")
from op_credential_utils import get_field, store_field, field_exists, check_signed_in

# Check if signed in first
if not check_signed_in():
    print("Please run 'op signin' first")
    sys.exit(1)

# Retrieve a credential (vault auto-detected based on working directory)
token = get_field("google-calendar-personal", "access-token")

# Check if a field exists
if not field_exists("google-calendar-personal", "refresh-token"):
    print("No refresh token found - need to re-authenticate")

# Store a credential (item must already exist)
store_field("google-calendar-personal", "access-token", new_token)

# Use credential directly - NEVER print it
response = api_call(token)
print("API call successful")  # Only status messages
```

**Vault auto-detection:**

- Running from `work/dev/*` → uses `Credentials-Dev Project`
- Running from anywhere else → uses `Credentials-Workflow Tools`
- Override with explicit `vault=` parameter when needed

## Scripts

| Script | Status | Description |
|--------|--------|-------------|
| `op_credential_utils.py` | Active | Python utilities for credential retrieval and storage |
| `seed_1password_docs.py` | Active | Discover 1Password CLI documentation URLs |
| `crawl_1password_docs.py` | Active | Crawl and save docs as markdown with YAML front matter |

The documentation scripts use pbc-web-crawling/tool-crawl4ai's venv for Crawl4AI functionality.

## Workflows

See [workflows/README.md](workflows/README.md) for reusable patterns.

| Workflow | Status | Use Case |
|----------|--------|----------|
| [Credential Retrieval](workflows/credential-retrieval.md) | Stub | Patterns for getting secrets |
| [Environment Injection](workflows/environment-injection.md) | Stub | Using `op run` for env vars |
| [Project Setup](workflows/project-setup.md) | Stub | Setting up new projects with 1Password |

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| `not signed in` | Session expired | Run `op signin` |
| `item not found` | Wrong name/vault | Check with `op item list --vault "..."` |
| `vault not found` | Wrong vault name | Check with `op vault list` |
| `permission denied` | No access to vault | Check 1Password app permissions |

## Composability

This PBC provides **credential management** for any project:

```
Any PBC/Project ──► pbc-secrets-management ──► Secure credentials
```

Used by any project requiring secure credential access without exposing secrets.

## Related Documentation

- [1Password CLI Docs](https://developer.1password.com/docs/cli)
- [Secret Reference Syntax](https://developer.1password.com/docs/cli/secret-references)
- Local docs: `docs/` (59 crawled documentation pages)
