# 1Password CLI PBC - Claude Instructions

## When to Use This PBC

Use this PBC when the user needs to:

- Manage credentials securely using 1Password CLI
- Inject secrets into environment variables
- Use secret references (`op://` syntax)
- Integrate 1Password with Python scripts

## Security Model - CRITICAL

**Credentials must NEVER be visible to Claude Code.**

All scripts that retrieve credentials must:

1. Retrieve credentials silently (no stdout)
2. Use credentials directly in operations
3. Only output success/failure messages

```python
# CORRECT - Claude never sees the credential
token = get_credential("op://Credentials-Workflow Tools/google-calendar/token")
response = api_call(token)  # Use directly
print("API call successful")  # Only status messages

# WRONG - Never do this
token = get_credential(...)
print(f"Token: {token}")  # EXPOSES CREDENTIAL TO CLAUDE
```

## Quick Reference

**Read a secret:**

```bash
op read "op://vault/item/field"
```

**Inject secrets into command:**

```bash
op run --env-file .env.op -- python script.py
```

**Secret reference syntax:**

```text
op://vault/item/field
op://Credentials-Workflow Tools/github-pat/credential
```

## Documentation by Task

| Task | Read This First |
|------|-----------------|
| Using secret references | `docs/secret-references.md` |
| Security patterns | `docs/best-practices.md` |
| Reading secrets with CLI | `docs/cli-commands-read.md` |
| Environment injection (`op run`) | `docs/cli-commands-run.md` |
| SSH key management | `docs/ssh-keys.md` |
| Config file templates | `docs/secrets-config-files.md` |
| Script integration | `docs/secrets-scripts.md` |

## Vault Architecture

Drew uses two vaults:

| Vault | Purpose | Example Items |
|-------|---------|---------------|
| **Credentials-Workflow Tools** | Personal tooling, cross-project | `google-calendar-personal`, `github-pat` |
| **Credentials-Dev Project** | Project-specific secrets | `myapp-database`, `clientsite-stripe` |

## Scripts Inventory

Check `pbc-tool-definition.yaml` for available scripts:

| Script | Purpose |
|--------|---------|
| `op_credential_utils.py` | Python utilities for credential retrieval and storage |
| `seed_1password_docs.py` | Discover documentation URLs |
| `crawl_1password_docs.py` | Crawl and save docs as markdown |

The documentation scripts use pbc-web-crawling/tool-crawl4ai's venv for Crawl4AI.

## Python Integration Pattern

Use the `op_credential_utils.py` module for all credential operations:

```python
import sys
sys.path.insert(0, r"C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\scripts")
from op_credential_utils import get_field, store_field, field_exists, check_signed_in

# Retrieve a credential (vault auto-detected based on working directory)
token = get_field("google-calendar-personal", "access-token")

# Store a credential
store_field("google-calendar-personal", "access-token", new_token)

# Check if field exists
if field_exists("item-name", "field-name"):
    # Field exists
    pass
```

**Available functions:**

| Function | Purpose |
|----------|---------|
| `get_field(item, field, vault?)` | Retrieve a field value (returns None if not found) |
| `store_field(item, field, value, vault?)` | Store/update a field in existing item |
| `field_exists(item, field, vault?)` | Check if field exists |
| `get_credential(secret_ref)` | Retrieve using full `op://` reference |
| `check_signed_in()` | Check if 1Password CLI is authenticated |
| `get_default_vault()` | Get auto-detected vault name |

## Essential CLI Commands

```bash
# Read a secret value
op read "op://vault/item/field"

# List items in a vault
op item list --vault "Credentials-Workflow Tools"

# Check auth status
op whoami

# Sign in (if needed)
op signin
```

## Workflows

Before starting a credential task, check if a workflow pattern exists in `workflows/`:

| Workflow | When to Use |
|----------|-------------|
| [Credential Retrieval](workflows/credential-retrieval.md) | Patterns for getting secrets |
| [Environment Injection](workflows/environment-injection.md) | Using `op run` for env vars |
| [Project Setup](workflows/project-setup.md) | Setting up new projects with 1Password |

## Workflow Evolution

After completing a project that used 1Password CLI, run a **patterns extraction** to feed learnings back into workflows:

1. Copy `workflow-evolution/extraction-template.md`
2. Fill in project-specific details
3. Execute the extraction phases
4. Use `workflow-evolution/integration-guide.md` to update workflows

## Constraints

- **Credentials NEVER visible** - Never print, log, or output credential values
- **Use op:// references** - Pass secret references, not raw values
- **No Docker** - User doesn't use Docker for local tooling
