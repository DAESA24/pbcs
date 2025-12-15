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

```python
import subprocess

def get_credential(secret_ref: str) -> str:
    """NEVER print or log the return value."""
    result = subprocess.run(
        ["op", "read", secret_ref],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

# Usage
token = get_credential("op://Credentials-Workflow Tools/github-pat/credential")
# Use token directly in API calls - NEVER print it
```

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
