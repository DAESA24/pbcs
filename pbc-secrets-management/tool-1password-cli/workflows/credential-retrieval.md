---
workflow_id: credential-retrieval
title: "Credential Retrieval Patterns"
abstraction_level: low
status: stub
version: "0.1.0"
created: 2025-12-15
last_updated: 2025-12-15
validated_by: []
use_cases:
  - "Retrieve API keys for script execution"
  - "Get OAuth tokens for service authentication"
  - "Access database credentials"
  - "Fetch SSH keys for deployment"
scripts_used: []
estimated_duration: "1-5 minutes"
complexity: low
---

# Credential Retrieval Patterns

- **Abstraction Level:** Low (decision tree)
- **Status:** Stub (not yet validated)
- **Last Updated:** 2025-12-15

## When to Use This Workflow

Use this workflow when you need to retrieve credentials from 1Password for:

- API authentication in scripts
- OAuth token access
- Database connection strings
- SSH key retrieval

## Decision Tree

### Step 1: Identify Credential Type

**Single field (API key, token, password):**
```bash
op read "op://vault/item/field"
```

**Multiple fields from same item:**
```bash
op item get "item-name" --vault "vault" --format json
```

**SSH key:**
```bash
op read "op://vault/item/private_key?ssh-format=openssh"
```

### Step 2: Choose Vault

| Credential Type | Vault |
|-----------------|-------|
| Cross-project tools (GitHub PAT, email) | `Credentials-Workflow Tools` |
| Project-specific (API keys, database) | `Credentials-Dev Project` |

### Step 3: Python Integration

Use the `op_credential_utils.py` module:

```python
import sys
sys.path.insert(0, r"C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\scripts")
from op_credential_utils import get_field, store_field, field_exists, check_signed_in

# Check auth status first
if not check_signed_in():
    print("1Password CLI not signed in. Run 'op signin' first.")
    sys.exit(1)

# Retrieve a credential (vault auto-detected based on working directory)
token = get_field("github-pat", "credential")

# Or specify vault explicitly
token = get_field("github-pat", "credential", vault="Credentials-Workflow Tools")

# Check if a field exists before retrieving
if field_exists("google-calendar-personal", "access-token"):
    token = get_field("google-calendar-personal", "access-token")

# Store a credential (after OAuth flow, for example)
store_field("google-calendar-personal", "access-token", new_token)

# Use credential directly in API calls - NEVER print it
response = api_call(token)
print("API call successful")
```

**Vault auto-detection:**

- `work/dev/*` → `Credentials-Dev Project`
- Otherwise → `Credentials-Workflow Tools`

## Common Pitfalls

- **Printing credentials:** Never `print()` or log credential values. Claude Code can see stdout.
- **Session expired:** If `op read` fails with "not signed in", run `op signin` first.
- **Wrong field name:** Check with `op item get "item" --vault "vault"` to see field names.
- **URL encoding:** If item/field names have spaces, the CLI handles this automatically.

## Security Checklist

- [ ] Credential value is NEVER printed to stdout
- [ ] Credential is used directly in the target operation
- [ ] Error messages don't expose credential values
- [ ] Scripts exit cleanly without leaking on exception

## Related Documentation

- [Secret References](../docs/secret-references.md)
- [CLI Read Command](../docs/cli-commands-read.md)
- [Best Practices](../docs/best-practices.md)

---

- **Document Status:** Stub
- **Next Review:** After first validation
