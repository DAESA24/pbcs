# User Requirements: 1Password Python SDK Migration

**Created:** 2025-12-16
**Status:** Draft
**Purpose:** Define user requirements and use cases that drive the SDK migration decision

---

## 1. User Context

| Attribute | Value |
|-----------|-------|
| **User** | Drew (solo developer) |
| **Platform** | Windows 11 |
| **Auth Preference** | Windows Hello (biometrics) |
| **Security Constraint** | Credentials must NEVER be visible to Claude Code |

---

## 2. Blocking Use Case: Google Calendar Skill

### 2.1 What It Is

A **global Claude Code skill** that enables calendar management via natural language from **any project directory** where Claude Code is working.

- **Skill Location:** `~/.claude/skills/calendar/SKILL.md` (global)
- **Scripts Location:** `C:\Users\drewa\work\dev\cc-skills-dev\calendar-skills-dev\scripts\`
- **Calendars:** Personal (Gmail) and Work (Google Workspace)

### 2.2 User Stories

**UC-1: Weekly Briefing**
> "What does my calendar look like this week?"
> "What are my commitments for the week, by day?"

- Read-only
- Both calendars
- Returns structured summary

**UC-2: Add All-Day Task/Event**
> "Add 'Call Jenna' to Wednesday"
> "Put 'Noah's enrollment deadline' on my personal calendar for Friday"

- Write operation (create event)
- All-day (no specific time)
- User specifies calendar or defaults to personal

**UC-3: Reschedule Event**
> "Move my 3pm meeting to 4pm on my work calendar"
> "Reschedule the dentist appointment to next Tuesday"

- Read + Write (find, then update)
- Must identify event first

**UC-4: Check Conflicts/Availability**
> "Do I have a conflict on Tuesday at 2pm?"
> "Am I free Thursday afternoon?"

- Read-only
- May check multiple calendars

---

## 3. Technical Architecture (Current)

```
User (via Claude Code)
    │
    ▼
calendar_cli.py (CLI entry point)
    │
    ▼
calendar_auth.py (OAuth flow)
    │
    ├─► get_credentials() ──► _get_stored_credentials()
    │                              │
    │                              ▼
    │                         op_credential_utils.py
    │                              │
    │                              ▼
    │                         subprocess.run(["op", ...])
    │                              │
    │                              ▼
    │                         1Password CLI ──► 1Password Desktop App
    │                                                    │
    │                                                    ▼
    │                                              Windows Hello
    │
    └─► _save_tokens() ──► store_field() ──► (same path)
```

### 3.1 Current 1Password Item Structure

**Item:** `google-calendar-personal` (in `Credentials-Workflow Tools` vault)

| Field | Type | Purpose |
|-------|------|---------|
| `client-id` | STRING | OAuth client ID from Google Cloud Console |
| `client-secret` | CONCEALED | OAuth client secret |
| `project-id` | STRING | Google Cloud project ID |
| `auth-uri` | STRING | OAuth authorization endpoint |
| `token-uri` | STRING | OAuth token endpoint |
| `access-token` | CONCEALED | Current access token (expires ~1 hour) |
| `refresh-token` | CONCEALED | Long-lived refresh token |
| `token-expiry` | STRING | ISO datetime when access token expires |

---

## 4. Credential Operations Required

Based on `op_credential_utils.py` and `calendar_auth.py`:

### 4.1 Read Operations

| Function | Usage in Calendar Skill | Frequency |
|----------|------------------------|-----------|
| `get_field(item, field, vault)` | Retrieve individual fields (client-id, access-token, etc.) | Every API call |
| `get_credential(op://ref)` | Alternative: full op:// reference | Not currently used |
| `field_exists(item, field, vault)` | Check if tokens exist | Startup check |
| `check_signed_in()` | Verify 1Password is authenticated | Before any operation |

**Hot Path:** `_get_stored_credentials()` calls `get_field()` **8 times** per authentication check.

### 4.2 Write Operations

| Function | Usage in Calendar Skill | Frequency |
|----------|------------------------|-----------|
| `store_field(item, field, value, vault)` | Save refreshed tokens | After each token refresh (~hourly) |

**Token Refresh Flow:**
1. Access token expires (1 hour lifetime)
2. `calendar_auth._refresh_token()` calls Google API
3. Google returns new access token (and sometimes new refresh token)
4. `_save_tokens()` writes 1-3 fields back to 1Password:
   - `access-token` (always)
   - `token-expiry` (always)
   - `refresh-token` (sometimes)

### 4.3 Create Operations

| Function | Usage | Frequency |
|----------|-------|-----------|
| `create_oauth_client_item()` | Initial setup: import credentials from Google Cloud Console JSON | One-time per calendar |

---

## 5. Derived Technical Requirements

| Requirement | Implication | Priority |
|-------------|-------------|----------|
| **R1: Biometric auth from Python** | SDK must trigger Windows Hello without manual `op signin` | **Critical** |
| **R2: Read individual fields** | SDK must support field-level reads (not just full item) | **Critical** |
| **R3: Update individual fields** | SDK must support field-level writes to existing items | **Critical** |
| **R4: Async-compatible** | Calendar skill is sync, but SDK is async—need to handle | Medium |
| **R5: Global skill (any cwd)** | Can't rely on cwd-based vault auto-detection | Medium |
| **R6: Create items with structure** | SDK must support creating items with custom fields | Low (one-time setup) |
| **R7: Credential secrecy** | Credentials must never appear in logs, stdout, or Claude Code context | **Critical** |

---

## 6. Invocation Context

### 6.1 How Scripts Are Called

1. **From Claude Code** (primary use case)
   - Claude Code invokes: `.venv\Scripts\python.exe scripts/calendar_cli.py ...`
   - Python subprocess spawns → calls `op_credential_utils.py` → spawns `op` CLI
   - **This is where it fails:** The nested subprocess doesn't inherit terminal trust

2. **From Terminal** (development/testing)
   - User runs: `python scripts/calendar_cli.py ...`
   - Works fine if user already ran `op signin` in that terminal session

### 6.2 The Fundamental Problem

```
Terminal Session
    │
    ├─► op signin ──► Windows Hello ──► Session established ✓
    │
    └─► python calendar_cli.py
            │
            └─► subprocess.run(["op", "read", ...])
                    │
                    └─► NEW PROCESS ──► "Not signed in" ✗
```

The `op` CLI's desktop app integration only trusts certain parent processes. Python's subprocess creates a new process tree that isn't recognized.

---

## 7. Success Criteria

The migration is successful when:

1. **SC-1:** Running `calendar_cli.py create personal '{...}'` from Claude Code triggers Windows Hello (if not already authenticated) and completes successfully

2. **SC-2:** Token refresh works: when access token expires, new token is fetched and stored without user intervention

3. **SC-3:** No `subprocess.run(["op", ...])` calls remain in `op_credential_utils.py`

4. **SC-4:** All existing function signatures work unchanged (API compatibility)

5. **SC-5:** Credentials never appear in stdout, logs, or error messages

---

## 8. Open Questions

1. **Q1:** Does the SDK support field-level reads, or only full item retrieval?
   - If only full item: how do we extract specific fields?

2. **Q2:** Does the SDK support field-level updates, or do we need to read-modify-write the entire item?
   - If read-modify-write: what's the concurrency story?

3. **Q3:** What happens when the 10-minute desktop auth window expires mid-session?
   - Does it prompt again, or fail silently?

4. **Q4:** Is the beta SDK stable enough for daily use?
   - What are the known issues?

---

## 9. Next Steps

1. Define specific information requirements based on these user requirements
2. Identify source URLs to crawl for SDK documentation
3. Execute structured crawl to capture clean documentation
4. Evaluate SDK capabilities against requirements
5. Make go/no-go decision
