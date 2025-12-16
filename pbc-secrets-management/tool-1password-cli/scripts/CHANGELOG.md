# Changelog

All notable changes to the 1Password CLI scripts will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-12-16

### Added

- **OAuth credential import functionality** (`op_credential_utils.py`)
  - `create_oauth_client_item()` function to import OAuth credentials from JSON files (e.g., Google Cloud Console)
  - `import-oauth` CLI command for command-line usage
  - `_secure_delete()` helper that overwrites files with random bytes before deletion
  - `_parse_google_credentials()` parser supporting Google's `installed` and `web` JSON formats
  - `_build_oauth_item_template()` builder for 1Password JSON templates
  - Pre-creates empty token fields (`access-token`, `refresh-token`, `token-expiry`) for OAuth flow

- **CLI entry point** (`op_credential_utils.py`)
  - Script can now be run directly: `python op_credential_utils.py import-oauth <file> <title> [--vault]`
  - Argparse-based CLI with help text and examples

- **New imports** (`op_credential_utils.py`)
  - `argparse`, `json`, `sys`, `pathlib.Path` added to support new functionality

### Security

- OAuth credentials are passed to 1Password CLI via stdin (never in command line arguments)
- Source JSON files are securely deleted after successful import (overwrite with random bytes + delete)
- If 1Password item creation fails, source file is preserved (not deleted)

## [1.0.0] - 2025-12-15

### Added

- Initial release of `op_credential_utils.py`
  - `get_default_vault()` - Auto-detect vault based on working directory
  - `check_signed_in()` - Verify 1Password CLI authentication
  - `get_credential()` - Retrieve credentials using `op://` secret references
  - `get_field()` - Retrieve specific fields from 1Password items
  - `field_exists()` - Check if a field exists in an item
  - `store_field()` - Store/update fields in existing 1Password items
  - `_handle_op_error()` - User-friendly error handling for CLI errors

- Initial release of `seed_1password_docs.py`
  - URL discovery for 1Password CLI documentation using Crawl4AI

- Initial release of `crawl_1password_docs.py`
  - Documentation crawler with YAML front matter generation
