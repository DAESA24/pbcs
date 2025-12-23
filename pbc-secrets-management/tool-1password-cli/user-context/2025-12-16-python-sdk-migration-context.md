# Context: Migrate op_credential_utils.py from CLI to Python SDK

- **Created:** 2025-12-16
- **Purpose:** Provide Claude Code with full context to migrate from 1Password CLI subprocess calls to the official 1Password Python SDK
- **Target Directory:** `C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\`
- **Blocking Project:** Google Calendar Skill (`C:\Users\drewa\work\dev\cc-skills-dev\calendar-skills-dev`)

---

## 1. What We Were Trying To Do

Build a Google Calendar skill for Claude Code that:
- Manages Drew's personal (Gmail) and work (Google Workspace) calendars
- Stores OAuth tokens securely in 1Password
- Retrieves credentials at runtime via `op_credential_utils.py`
- Never exposes credentials to Claude Code (security requirement)

The skill architecture:
```
calendar-skills-dev/
├── scripts/
│   ├── calendar_auth.py      # OAuth flow, uses op_credential_utils
│   ├── calendar_ops.py       # CRUD operations
│   └── calendar_cli.py       # CLI entry point
└── calendar/
    └── SKILL.md              # Claude Code skill definition
```

## 2. The Reason for the Objective

Drew wants to manage his calendars through natural language commands in Claude Code:
- "Add Noah's enrollment deadline to my personal calendar"
- "Do I have a conflict on Tuesday at 2pm?"
- "Move my 3pm meeting to 4pm on my work calendar"

This requires secure credential storage (1Password) with seamless authentication (biometrics/Windows Hello).

## 3. Description of This Project

**This directory (`tool-1password-cli`)** is a PBC (Packaged Business Capability) that provides:
- `scripts/op_credential_utils.py` - Python utility for 1Password CLI operations
- Functions: `get_credential()`, `get_field()`, `store_field()`, `check_signed_in()`, `create_oauth_client_item()`
- Used by other projects (like calendar-skills-dev) that need secure credential storage

**Current Implementation:** Uses `subprocess.run()` to call the `op` CLI binary.

## 4. The Problem We Ran Into During Testing

### Symptom

When running Python scripts that call `op_credential_utils.py` functions, we get:
```
Error: 1Password CLI not signed in. Run 'op signin' first.
```

This happens **immediately after** successfully running `op signin` in the same terminal, and even though `op whoami` confirms the user is signed in.

### Evidence from Testing

1. **Direct CLI works:** `op vault list` in PowerShell triggers 1Password desktop app auth prompt and succeeds
2. **Python subprocess fails:** Same command via `subprocess.run(["op", "vault", "list"])` fails with "not signed in"
3. **shell=True doesn't help:** Tried `subprocess.run("op vault list", shell=True)` - still fails
4. **Environment variable approach fails:** `Invoke-Expression $(op signin --account my)` returns null because desktop app integration doesn't output session tokens
5. **Disabling biometrics requires Secret Key:** Setting `OP_BIOMETRIC_UNLOCK_ENABLED=false` forces manual account setup with Secret Key - not acceptable for daily use

### User's Requirement

Drew requires biometrics/Windows Hello authentication for 1Password. Any solution that requires manual password or Secret Key entry is not acceptable for production use.

## 5. Validated Root Cause

### Confirmed via 1Password Documentation and GitHub Issues

**Source:** [1Password GitHub Issue #63](https://github.com/1Password/solutions/issues/63)

> "This error happens on Windows when 1Password CLI is integrated with 1Password for Windows. The desktop app integration does not seem to allow a subprocess to delegate sign in using the desktop app."

**Source:** [1Password Developer Docs - Desktop App Integration](https://developer.1password.com/docs/cli/app-integration/)

The 1Password desktop app integration uses a trust model that only recognizes certain parent processes. Python's `subprocess.run()` spawns child processes that:
1. Don't inherit the terminal context
2. Can't trigger the biometric authentication prompt
3. Are not recognized as "trusted" by the 1Password desktop app

### Why CLI Subprocess Cannot Work

The fundamental issue is architectural:
- 1Password desktop app integration relies on process trust chains
- Python subprocess creates a new process tree
- The new process tree is not recognized by 1Password desktop app
- No amount of `shell=True` or environment variable passing can fix this

## 6. Solution: Migrate to 1Password Python SDK

### Why the SDK Solves This

**Source:** [1Password SDK Desktop App Integration](https://developer.1password.com/docs/sdks/desktop-app-integrations/)

> "To use the desktop app integration with Python, you'll need Python version 3.10 or later. Your users can authorize your integration the same way they unlock their 1Password app, like with biometric unlock, their 1Password account password, or other supported methods."

The SDK has **native desktop app integration** that:
- Properly communicates with 1Password desktop app
- Triggers biometric prompts when needed
- Works from Python code without subprocess issues

### High-Level Migration Plan

#### Phase 1: Research & Setup
1. Read 1Password Python SDK documentation
2. Understand SDK authentication model
3. Create test script to verify SDK + biometrics works
4. Document any SDK limitations

#### Phase 2: Rewrite op_credential_utils.py
1. Replace `subprocess.run(["op", ...])` calls with SDK equivalents
2. Maintain the same public API (function signatures)
3. Keep security requirements (never print credentials)
4. Add SDK initialization/client management

#### Phase 3: Update Dependent Projects
1. Update calendar-skills-dev scripts if needed
2. Test end-to-end with biometric auth
3. Document any usage changes

#### Phase 4: Cleanup
1. Remove CLI subprocess code
2. Update documentation
3. Test on fresh terminal session

---

## 7. Dependencies and Files to Update

### Primary File to Rewrite

**File:** `C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\scripts\op_credential_utils.py`

**Current Functions (must maintain API compatibility):**
```python
def check_signed_in() -> bool
def get_credential(secret_ref: str) -> Optional[str]
def get_field(item: str, field: str, vault: Optional[str] = None) -> Optional[str]
def field_exists(item: str, field: str, vault: Optional[str] = None) -> bool
def store_field(item: str, field: str, value: str, vault: Optional[str] = None) -> bool
def create_oauth_client_item(credentials_file: str, item_title: str, vault: Optional[str] = None) -> bool
```

**Internal Helpers (can be rewritten):**
```python
def get_default_vault() -> str
def _handle_op_error(e: subprocess.CalledProcessError) -> None
def _parse_google_credentials(file_path: Path) -> dict
def _build_oauth_item_template(title: str, credentials: dict, vault: str) -> dict
def _secure_delete(file_path: Path) -> None
```

### Downstream Dependencies

**Calendar Skills Project:**
- `C:\Users\drewa\work\dev\cc-skills-dev\calendar-skills-dev\scripts\calendar_auth.py`
  - Imports: `get_credential`, `store_field`, `field_exists` from op_credential_utils
  - Uses: Token storage/retrieval for OAuth flow

**Import Statement in calendar_auth.py:**
```python
sys.path.insert(0, r"C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\scripts")
from op_credential_utils import get_credential, store_field, field_exists, check_signed_in
```

### Configuration Dependencies

**File:** `C:\Users\drewa\work\dev\cc-skills-dev\calendar-skills-dev\scripts\config.py`
```python
OP_UTILS_PATH = r"C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\scripts"
VAULT = "Credentials-Workflow Tools"
```

### New Dependencies to Add

**Python Package:** `onepassword-sdk` (or whatever the official package name is)
- Requires Python 3.10+
- Add to requirements.txt or pyproject.toml

---

## 8. Security Requirements (Must Preserve)

1. **Never print credentials** - All credential values must stay internal
2. **Never log credentials** - No debug logging of sensitive values
3. **Secure delete** - Source credential files must be securely deleted after import
4. **Vault isolation** - Support specifying vault for credential operations

---

## 9. Success Criteria

The migration is successful when:

1. **Biometric auth works:** Running `calendar_cli.py create personal '{...}'` triggers Windows Hello prompt (if not already authenticated)
2. **No subprocess calls:** `op_credential_utils.py` contains zero `subprocess.run()` calls to `op`
3. **API compatibility:** All existing function signatures work unchanged
4. **End-to-end test:** Can create a calendar event using the skill with biometric auth

---

## 10. Reference Links

- [1Password Python SDK Documentation](https://developer.1password.com/docs/sdks/)
- [1Password SDK Desktop App Integration](https://developer.1password.com/docs/sdks/desktop-app-integrations/)
- [GitHub Issue #63 - Python subprocess fails on Windows](https://github.com/1Password/solutions/issues/63)
- [1Password CLI App Integration (for reference)](https://developer.1password.com/docs/cli/app-integration/)

---

## 11. How to Use This Document

When starting a new Claude Code session in `C:\Users\drewa\pbcs\pbc-secrets-management\tool-1password-cli\`:

1. Read this document for full context
2. Research the 1Password Python SDK
3. Create a test script to verify SDK works with biometrics
4. Proceed with migration plan

The goal is seamless biometric authentication from Python code - no workarounds, no manual sign-in required.

---

- **Document Status:** Complete
- **Next Action:** Research 1Password Python SDK and verify biometric support
- **Blocked Project:** calendar-skills-dev (Phase 7 testing cannot proceed until this is resolved)
