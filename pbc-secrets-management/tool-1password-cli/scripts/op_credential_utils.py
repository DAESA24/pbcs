"""
1Password CLI credential utilities for Python scripts.

Type: Primary
    This is a primary script that directly uses the 1Password CLI for intended
    credential management use cases (retrieval, storage, authentication checks,
    and secure item creation from OAuth credential files).

Purpose:
    Provides a security-focused Python interface to the 1Password CLI. Use this
    module when your scripts need to:
    - Retrieve API tokens and credentials
    - Store OAuth tokens after authentication flows
    - Check authentication status
    - Import OAuth client credentials from JSON files (e.g., Google Cloud Console)

SECURITY: Functions in this module handle credentials securely:
    - NEVER print or log credential values
    - Use stdin piping for item creation (secrets never appear in command line)
    - Securely delete source files after import (overwrite + delete)

Usage:
    import sys
    sys.path.insert(0, r"C:\\Users\\drewa\\pbcs\\pbc-secrets-management\\tool-1password-cli\\scripts")
    from op_credential_utils import get_field, store_field, check_signed_in, create_oauth_client_item

Example - Retrieve credentials:
    token = get_field("google-calendar-personal", "access-token")
    response = api_call(token)  # Use directly - NEVER print
    print("API call successful")  # Only status messages

Example - Import OAuth credentials from Google:
    # After downloading credentials JSON from Google Cloud Console
    create_oauth_client_item(
        credentials_file="C:/Users/drewa/Downloads/credentials.json",
        item_title="google-calendar-personal",
        vault="Credentials-Workflow Tools"
    )
    # File is securely deleted after successful import

CLI Usage:
    python op_credential_utils.py import-oauth <credentials.json> <item-title> [--vault <vault>]
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional


# Vault configuration
VAULT_WORKFLOW_TOOLS = "Credentials-Workflow Tools"
VAULT_DEV_PROJECT = "Credentials-Dev Project"


def get_default_vault() -> str:
    """
    Auto-detect which vault to use based on current working directory.

    Returns:
        - "Credentials-Dev Project" if cwd contains "work/dev" or "work\\dev"
        - "Credentials-Workflow Tools" otherwise
    """
    cwd = os.getcwd().lower()

    if "work\\dev" in cwd or "work/dev" in cwd:
        return VAULT_DEV_PROJECT
    else:
        return VAULT_WORKFLOW_TOOLS


def check_signed_in() -> bool:
    """
    Check if 1Password CLI is authenticated.

    Returns:
        True if signed in, False otherwise
    """
    result = subprocess.run(
        ["op", "whoami"],
        capture_output=True,
        text=True
    )
    return result.returncode == 0


def _handle_op_error(e: subprocess.CalledProcessError) -> None:
    """
    Handle 1Password CLI errors with user-friendly messages.

    Raises:
        RuntimeError: With actionable error message
    """
    stderr = e.stderr.lower() if e.stderr else ""

    if "not signed in" in stderr or "session expired" in stderr:
        raise RuntimeError("1Password CLI not signed in. Run 'op signin' first.")
    elif "could not find item" in stderr or "item not found" in stderr:
        # Don't raise for missing items - let caller handle via None return
        return
    elif "could not find vault" in stderr or "vault not found" in stderr:
        raise RuntimeError(f"1Password vault not found. Check vault name and permissions.")
    elif "field not found" in stderr or "no field" in stderr:
        # Don't raise for missing fields - let caller handle via None return
        return
    else:
        # Re-raise with original error for unexpected issues
        raise RuntimeError(f"1Password CLI error: {e.stderr.strip() if e.stderr else 'Unknown error'}")


def get_credential(secret_ref: str) -> Optional[str]:
    """
    Retrieve a credential using a full op:// secret reference.

    Args:
        secret_ref: Full op:// reference (e.g., "op://vault/item/field")

    Returns:
        The credential value, or None if not found.
        NEVER print or log the return value.

    Raises:
        RuntimeError: If 1Password CLI is not signed in or other errors occur
    """
    try:
        result = subprocess.run(
            ["op", "read", secret_ref],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        _handle_op_error(e)
        return None


def get_field(item: str, field: str, vault: Optional[str] = None) -> Optional[str]:
    """
    Retrieve a field from a 1Password item.

    Args:
        item: Item name in 1Password
        field: Field name to retrieve
        vault: Vault name. If None, auto-detects based on working directory:
               - work/dev/* -> Credentials-Dev Project
               - Otherwise  -> Credentials-Workflow Tools

    Returns:
        The field value, or None if not found.
        NEVER print or log the return value.

    Raises:
        RuntimeError: If 1Password CLI is not signed in or other errors occur
    """
    if vault is None:
        vault = get_default_vault()

    return get_credential(f"op://{vault}/{item}/{field}")


def field_exists(item: str, field: str, vault: Optional[str] = None) -> bool:
    """
    Check if a field exists in a 1Password item.

    Args:
        item: Item name in 1Password
        field: Field name to check
        vault: Vault name. If None, auto-detects based on working directory.

    Returns:
        True if field exists, False otherwise
    """
    return get_field(item, field, vault) is not None


def store_field(item: str, field: str, value: str, vault: Optional[str] = None) -> bool:
    """
    Store or update a field in an existing 1Password item.

    Args:
        item: Item name in 1Password (must already exist)
        field: Field name to set
        value: Value to store (will not be printed - passed directly to op CLI)
        vault: Vault name. If None, auto-detects based on working directory.

    Returns:
        True on success

    Raises:
        RuntimeError: If item doesn't exist, not signed in, or other errors occur

    Note:
        The value parameter contains sensitive data. It is passed directly to
        the 1Password CLI and is never logged or printed.
    """
    if vault is None:
        vault = get_default_vault()

    try:
        subprocess.run(
            ["op", "item", "edit", item, f"{field}={value}", "--vault", vault],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        _handle_op_error(e)
        # If we get here, it's an unexpected error
        raise RuntimeError(f"Failed to store field '{field}' in item '{item}'")


# =============================================================================
# OAuth Client Credential Import Functions
# =============================================================================


def _secure_delete(file_path: Path) -> None:
    """
    Securely delete a file by overwriting contents before deletion.

    Overwrites the file with random bytes, flushes to disk, then deletes.
    This makes casual recovery much harder than a simple delete.

    Args:
        file_path: Path to the file to securely delete

    Note:
        This is not military-grade secure deletion, but is sufficient for
        preventing accidental exposure and casual recovery attempts.
    """
    try:
        size = file_path.stat().st_size
        with open(file_path, 'wb') as f:
            f.write(os.urandom(size))  # Overwrite with random bytes
            f.flush()
            os.fsync(f.fileno())  # Force write to disk
        file_path.unlink()  # Delete the file
    except OSError as e:
        raise RuntimeError(f"Failed to securely delete {file_path}: {e}")


def _parse_google_credentials(file_path: Path) -> dict:
    """
    Parse a Google OAuth client credentials JSON file.

    Google's format wraps credentials in an "installed" or "web" key:
    {
        "installed": {
            "client_id": "...",
            "client_secret": "...",
            "project_id": "...",
            ...
        }
    }

    Args:
        file_path: Path to the Google credentials JSON file

    Returns:
        Dict with keys: client_id, client_secret, project_id

    Raises:
        ValueError: If file format is not recognized
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Google uses "installed" for desktop apps, "web" for web apps
    if "installed" in data:
        creds = data["installed"]
    elif "web" in data:
        creds = data["web"]
    else:
        # Try flat structure (generic OAuth)
        creds = data

    required_fields = ["client_id", "client_secret"]
    for field in required_fields:
        if field not in creds:
            raise ValueError(
                f"Missing required field '{field}' in credentials file. "
                f"Expected Google OAuth client credentials JSON format."
            )

    return {
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
        "project_id": creds.get("project_id", ""),  # Optional
        "auth_uri": creds.get("auth_uri", ""),
        "token_uri": creds.get("token_uri", ""),
    }


def _build_oauth_item_template(
    title: str,
    credentials: dict,
    vault: str
) -> dict:
    """
    Build a 1Password item JSON template for OAuth client credentials.

    Creates an API Credential item with:
    - Client credentials (from the downloaded JSON)
    - Empty token fields (to be populated after OAuth flow)

    Args:
        title: Item title in 1Password
        credentials: Parsed credentials dict from _parse_google_credentials
        vault: Vault name

    Returns:
        Dict suitable for piping to `op item create -`
    """
    return {
        "title": title,
        "category": "API_CREDENTIAL",
        "vault": {"name": vault},
        "fields": [
            {
                "id": "client-id",
                "type": "STRING",
                "label": "client-id",
                "value": credentials["client_id"]
            },
            {
                "id": "client-secret",
                "type": "CONCEALED",
                "label": "client-secret",
                "value": credentials["client_secret"]
            },
            {
                "id": "project-id",
                "type": "STRING",
                "label": "project-id",
                "value": credentials["project_id"]
            },
            {
                "id": "auth-uri",
                "type": "STRING",
                "label": "auth-uri",
                "value": credentials["auth_uri"]
            },
            {
                "id": "token-uri",
                "type": "STRING",
                "label": "token-uri",
                "value": credentials["token_uri"]
            },
            # Pre-create empty fields for OAuth tokens (filled after auth flow)
            {
                "id": "access-token",
                "type": "CONCEALED",
                "label": "access-token",
                "value": ""
            },
            {
                "id": "refresh-token",
                "type": "CONCEALED",
                "label": "refresh-token",
                "value": ""
            },
            {
                "id": "token-expiry",
                "type": "STRING",
                "label": "token-expiry",
                "value": ""
            }
        ]
    }


def create_oauth_client_item(
    credentials_file: str,
    item_title: str,
    vault: Optional[str] = None
) -> bool:
    """
    Create a 1Password item from an OAuth client credentials JSON file.

    Reads the credentials file (e.g., from Google Cloud Console), creates
    a 1Password item with the client credentials and empty token fields,
    then securely deletes the source file.

    Args:
        credentials_file: Path to the OAuth credentials JSON file
        item_title: Title for the 1Password item (e.g., "google-calendar-personal")
        vault: Vault name. If None, auto-detects based on working directory.

    Returns:
        True on success

    Raises:
        FileNotFoundError: If credentials file doesn't exist
        ValueError: If credentials file format is invalid
        RuntimeError: If 1Password CLI errors occur

    Security:
        - Credentials are passed to op CLI via stdin (never in command args)
        - Source file is securely deleted after successful import
        - No credential values are printed or logged
    """
    file_path = Path(credentials_file)

    if not file_path.exists():
        raise FileNotFoundError(f"Credentials file not found: {credentials_file}")

    if vault is None:
        vault = get_default_vault()

    # Check 1Password is signed in before doing anything
    if not check_signed_in():
        raise RuntimeError("1Password CLI not signed in. Run 'op signin' first.")

    # Parse the credentials file
    credentials = _parse_google_credentials(file_path)

    # Build the 1Password item template
    template = _build_oauth_item_template(item_title, credentials, vault)

    # Create the item via stdin (secrets never appear in command line)
    try:
        result = subprocess.run(
            ["op", "item", "create", "-", "--format", "json"],
            input=json.dumps(template),
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        # Don't delete the file if creation failed
        _handle_op_error(e)
        raise RuntimeError(
            f"Failed to create 1Password item '{item_title}'. "
            f"Credentials file was NOT deleted."
        )

    # Success - now securely delete the source file
    _secure_delete(file_path)

    return True


# =============================================================================
# CLI Entry Point
# =============================================================================


def _cli_import_oauth(args) -> int:
    """Handle the import-oauth CLI command."""
    try:
        create_oauth_client_item(
            credentials_file=args.credentials_file,
            item_title=args.item_title,
            vault=args.vault
        )
        print(f"Created 1Password item: {args.item_title}")
        print(f"Credentials file securely deleted: {args.credentials_file}")
        return 0
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main():
    """CLI entry point for op_credential_utils."""
    parser = argparse.ArgumentParser(
        description="1Password CLI credential utilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Import Google OAuth credentials:
    python op_credential_utils.py import-oauth credentials.json google-calendar-personal

  Import with specific vault:
    python op_credential_utils.py import-oauth credentials.json google-calendar-work --vault "Credentials-Dev Project"
        """
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # import-oauth command
    import_parser = subparsers.add_parser(
        "import-oauth",
        help="Import OAuth client credentials from a JSON file into 1Password"
    )
    import_parser.add_argument(
        "credentials_file",
        help="Path to the OAuth credentials JSON file (e.g., from Google Cloud Console)"
    )
    import_parser.add_argument(
        "item_title",
        help="Title for the 1Password item (e.g., 'google-calendar-personal')"
    )
    import_parser.add_argument(
        "--vault",
        default=None,
        help="Vault name (default: auto-detect based on working directory)"
    )

    args = parser.parse_args()

    if args.command == "import-oauth":
        return _cli_import_oauth(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
