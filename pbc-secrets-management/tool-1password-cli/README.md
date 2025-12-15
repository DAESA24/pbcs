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

```python
import subprocess

def get_credential(secret_ref: str) -> str:
    """
    Retrieve a credential from 1Password.

    Args:
        secret_ref: Secret reference in format op://vault/item/field

    Returns:
        The credential value (NEVER print or log this)
    """
    result = subprocess.run(
        ["op", "read", secret_ref],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

# Usage
token = get_credential("op://Credentials-Workflow Tools/github-pat/credential")
# Use token directly - never print it
```

## Scripts

| Script | Status | Description |
|--------|--------|-------------|
| `seed_1password_docs.py` | Active | Discover 1Password CLI documentation URLs |
| `crawl_1password_docs.py` | Active | Crawl and save docs as markdown with YAML front matter |

These scripts use pbc-web-crawling/tool-crawl4ai's venv for Crawl4AI functionality.

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
