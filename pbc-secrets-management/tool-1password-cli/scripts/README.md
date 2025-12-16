# 1Password CLI Scripts

This directory contains Python scripts for working with the 1Password CLI (`op`) and crawling 1Password documentation.

## Scripts Overview

| Script | Type | Purpose |
|--------|------|---------|
| `op_credential_utils.py` | Primary | Python utilities for secure credential retrieval and storage |
| `seed_1password_docs.py` | Maintenance | Discover 1Password CLI documentation URLs for crawling |
| `crawl_1password_docs.py` | Maintenance | Crawl discovered URLs and save as markdown with metadata |

**Script Types:**

- **Primary**: Scripts that directly use the 1Password CLI for intended credential management use cases
- **Maintenance**: Scripts for maintaining the PBC itself (e.g., refreshing documentation after tool upgrades)

---

## op_credential_utils.py

**Purpose:** A security-focused Python module for retrieving, storing, and importing credentials via the 1Password CLI. Designed to prevent accidental credential exposure by never printing secrets.

### Key Features

- Auto-detects vault based on working directory
- Returns `None` for missing items/fields instead of raising errors
- User-friendly error messages for authentication issues
- Import OAuth credentials from JSON files (e.g., Google Cloud Console)
- Secure file deletion (overwrite + delete) after credential import
- CLI interface for common operations

### Use Cases

### 1. Importing OAuth credentials from Google Cloud Console

After downloading OAuth client credentials JSON from Google Cloud Console, securely import them into 1Password and delete the source file.

```bash
# CLI usage - imports credentials and securely deletes the JSON file
python op_credential_utils.py import-oauth "C:\Users\drewa\Downloads\credentials.json" "google-calendar-personal"

# With specific vault
python op_credential_utils.py import-oauth credentials.json "google-calendar-work" --vault "Credentials-Dev Project"
```

```python
# Python usage
from op_credential_utils import create_oauth_client_item

create_oauth_client_item(
    credentials_file="C:/Users/drewa/Downloads/credentials.json",
    item_title="google-calendar-personal",
    vault="Credentials-Workflow Tools"
)
# Credentials are now in 1Password, JSON file is securely deleted
```

The created 1Password item includes:

- `client-id`, `client-secret`, `project-id` (from the JSON file)
- `auth-uri`, `token-uri` (for OAuth flow configuration)
- Empty `access-token`, `refresh-token`, `token-expiry` fields (populated after OAuth flow)

### 2. Retrieving API tokens for script automation

When building a script that needs to call an external API, use `get_field()` to retrieve stored credentials without exposing them in logs.

```python
from op_credential_utils import get_field

# Retrieve token - vault auto-detected from working directory
api_token = get_field("slack-bot", "oauth-token")

# Use directly in API call - NEVER print the token
response = requests.post(url, headers={"Authorization": f"Bearer {api_token}"})
print("Message sent successfully")  # Only log status, not credentials
```

### 3. Checking authentication before running batch operations

Before starting a long-running process that needs 1Password access, verify the CLI is signed in to avoid mid-process failures.

```python
from op_credential_utils import check_signed_in, get_field

if not check_signed_in():
    print("Error: Run 'op signin' first")
    sys.exit(1)

# Now safe to run batch operations
for service in services:
    creds = get_field(service, "api-key")
    process_service(service, creds)
```

### 4. Storing OAuth refresh tokens after authentication flows

After completing an OAuth flow, securely store the refresh token back to 1Password for future use.

```python
from op_credential_utils import store_field

# After OAuth callback receives new tokens
store_field("google-calendar", "refresh-token", new_refresh_token)
store_field("google-calendar", "access-token", new_access_token)
print("Tokens updated successfully")  # Confirm without exposing values
```

---

## seed_1password_docs.py

**Purpose:** Discovers all 1Password CLI documentation URLs from developer.1password.com using Crawl4AI's sitemap seeding. Outputs a JSON file for review before crawling.

### Key Features
- Uses sitemap-based discovery for comprehensive coverage
- Applies BM25 relevance scoring based on security/CLI keywords
- Outputs metadata including titles and descriptions
- Filters to `/docs/cli/*` paths only

### Use Cases

**1. Initial documentation corpus setup**

When setting up a local copy of 1Password CLI docs for reference or RAG indexing, run this first to discover all available pages.

```bash
cd pbc-secrets-management/tool-1password-cli/scripts
python seed_1password_docs.py

# Review output
cat ../docs/_url_discovery.json
```

**2. Identifying high-relevance security documentation**

The script scores URLs by relevance to security terms. Review the output to prioritize which pages to crawl or read first.

```bash
python seed_1password_docs.py
# Check the summary output for "Top 10 by relevance score"
# High-scoring pages cover secrets, credentials, and security patterns
```

**3. Periodic documentation updates**

Re-run periodically to discover new documentation pages that have been added to the 1Password developer site.

```bash
# Compare new discovery with existing docs
python seed_1password_docs.py
diff ../docs/_url_discovery.json ../docs/_url_discovery_previous.json
```

---

## crawl_1password_docs.py

**Purpose:** Reads URLs from the discovery JSON and crawls each page, saving as markdown files with YAML front matter containing metadata for categorization and search.

### Key Features
- Intelligent URL filtering (excludes individual shell plugin pages, keeps overview docs)
- Auto-generates semantic filenames from URLs
- Adds YAML front matter with category, keywords, and relevance tags
- Supports concurrent crawling for performance

### Use Cases

**1. Building a local documentation reference**

After running the seeder, crawl all discovered URLs to create a local markdown copy of the documentation.

```bash
# First, seed the URLs
python seed_1password_docs.py

# Then crawl (filters out individual shell plugin pages by default)
python crawl_1password_docs.py

# Output is in ../docs/*.md with YAML front matter
```

**2. Creating a RAG-ready documentation corpus**

The YAML front matter includes category, keywords, and relevance tags that can be used for RAG chunk metadata.

```bash
python crawl_1password_docs.py --output-dir ../docs

# Each file includes front matter like:
# ---
# title: "Secret references"
# category: security
# relevance:
#   - secret retrieval
#   - environment variables
# keywords:
#   - op://
#   - secret reference
# ---
```

**3. Crawling everything without filtering**

If you need the complete documentation including all individual shell plugin integration pages, disable filtering.

```bash
python crawl_1password_docs.py --no-filter --output-dir ../docs/complete

# This includes pages like:
# - /docs/cli/shell-plugins/aws
# - /docs/cli/shell-plugins/github
# - etc.
```

---

## Dependencies

These scripts require:

- **1Password CLI** (`op`) - installed and signed in
- **Crawl4AI** - for `seed_1password_docs.py` and `crawl_1password_docs.py`
- **Python 3.10+**

Install Crawl4AI in the PBC venv:
```bash
cd pbc-web-crawling/tool-crawl4ai
.venv/Scripts/activate
pip install crawl4ai
```

## Security Notes

- `op_credential_utils.py` is designed to **never print credentials**
- Return values from `get_field()` and `get_credential()` should be used directly in operations
- Only log status messages, never credential values
- The module auto-detects vaults to reduce hardcoded configuration
