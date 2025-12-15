---
title: "connect | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/connect/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - authentication
  - vault management
keywords:
  - vault
related: []
---

# connect | 1Password CLI | 1Password Developer

On this page
# connect
Manage Connect server instances and tokens in your 1Password account.
Looking up a Connect server by its [ID](https://developer.1password.com/docs/cli/reference#unique-identifiers-ids) is more efficient than using the Connect server's name.
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#subcommands "Direct link to Subcommands")
  * [connect group](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group): Manage group access to Secrets Automation
  * [connect server](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server): Manage Connect servers
  * [connect token](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token): Manage Connect server tokens
  * [connect vault](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault): Manage Connect server vault access


## connect group[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group "Direct link to connect group")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group-subcommands "Direct link to Subcommands")
  * [connect group grant](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group-grant): Grant a group access to manage Secrets Automation
  * [connect group revoke](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group-revoke): Revoke a group's access to manage Secrets Automation


## connect group grant[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group-grant "Direct link to connect group grant")
Grant a group access to manage Secrets Automation.
op connect group grant [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group-grant-flags "Direct link to Flags")
--all-servers Grant access to all current and future servers in the authenticated
account.
--group group The group to receive access.
--server server The server to grant access to.
If you don't specify a server, it adds the group to the list of Secrets Automation managers.
## connect group revoke[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group-revoke "Direct link to connect group revoke")
Revoke a group's access to manage Secrets Automation.
op connect group revoke [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-group-revoke-flags "Direct link to Flags")
  

--all-servers Revoke access to all current and future servers in the
authenticated account.
--group group The group to revoke access from.
--server server The server to revoke access to.
## connect server[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server "Direct link to connect server")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-subcommands "Direct link to Subcommands")
  * [connect server create](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-create): Set up a Connect server
  * [connect server delete](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-delete): Remove a Connect server
  * [connect server edit](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-edit): Rename a Connect server
  * [connect server get](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-get): Get a Connect server
  * [connect server list](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-list): List Connect servers


## connect server create[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-create "Direct link to connect server create")
Add a 1Password Connect server to your account and generate a credentials file for it. 1Password CLI saves the `1password-credentials.json` file in the current directory.
Note: You can't grant a Connect server access to your built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault.
op connect server create <name> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-create-flags "Direct link to Flags")
-f, --force Do not prompt for confirmation when overwriting credential files.
--vaults strings Grant the Connect server access to these vaults.
1Password CLI saves the `1password-credentials.json` file in the current directory.
## connect server delete[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-delete "Direct link to connect server delete")
Remove a Connect server. Specify the server by name or ID.
op connect server delete [{ <serverName> | <serverID> | - }] [flags]
The credentials file and all the tokens for the server will no longer be valid.
## connect server edit[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-edit "Direct link to connect server edit")
Rename a Connect server. Specify the server by name or ID.
op connect server edit { <serverName> | <serverID> } [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-edit-flags "Direct link to Flags")
--name name Change the server's name.
## connect server get[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-get "Direct link to connect server get")
Get details about a Connect server. Specify the server by name or ID.
op connect server get [{ <serverName> | <serverID> | - }] [flags]
## connect server list[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-server-list "Direct link to connect server list")
Get a list of Connect servers.
op connect server list [flags]
## connect token[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token "Direct link to connect token")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-subcommands "Direct link to Subcommands")
  * [connect token create](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-create): Issue a token for a 1Password Connect server
  * [connect token delete](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-delete): Revoke a token for a Connect server
  * [connect token edit](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-edit): Rename a Connect server token
  * [connect token list](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-list): Get a list of tokens


## connect token create[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-create "Direct link to connect token create")
Issue a new token for a Connect server.
op connect token create <tokenName> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-create-flags "Direct link to Flags")
--expires-in duration Set how long the Connect token is valid for in (s)econds,
(m)inutes, (h)ours, (d)ays, and/or (w)eeks.
--server string Issue a token for this server.
--vault stringArray Issue a token on these vaults.
Returns a token.
You can only provision Connect server tokens to vaults that the Connect server has access to. Use `op connect vault grant` to grant access to vaults.
Note: You can't grant a Connect server access to your built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault.
By default, the `--vaults` option grants the same permissions as the server. To further limit the permissions a token has to read-only or write-only, add a comma and `r` or `w` after the vault specification. For example:
op connect token create "Dev k8s token" --server Dev --vaults Kubernetes,r \
--expires-in=30d
op connect token create "Prod: Customer details" --server Prod --vault "Customers,w" \
--vault "Vendors,r"
## connect token delete[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-delete "Direct link to connect token delete")
Revoke a token for a Connect server.
op connect token delete [ <token> ] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-delete-flags "Direct link to Flags")
--server string Only look for tokens for this 1Password Connect server.
## connect token edit[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-edit "Direct link to connect token edit")
Rename a Connect server token.
op connect token edit <token> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-edit-flags "Direct link to Flags")
--name string Change the token's name.
--server string Only look for tokens for this 1Password Connect server.
## connect token list[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-list "Direct link to connect token list")
List tokens for Connect servers.
op connect token list [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-token-list-flags "Direct link to Flags")
--server server Only list tokens for this Connect server.
Returns both active and revoked tokens.
The `integrationId` is the ID for the Connect server the token belongs to.
## connect vault[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault "Direct link to connect vault")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault-subcommands "Direct link to Subcommands")
  * [connect vault grant](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault-grant): Grant a Connect server access to a vault
  * [connect vault revoke](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault-revoke): Revoke a Connect server's access to a vault


## connect vault grant[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault-grant "Direct link to connect vault grant")
Grant a Connect server access to a vault.
op connect vault grant [flags]
Note: You can't grant a Connect server access to your built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault.
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault-grant-flags "Direct link to Flags")
--server string The server to be granted access.
--vault string The vault to grant access to.
## connect vault revoke[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault-revoke "Direct link to connect vault revoke")
Revoke a Connect server's access to a vault.
op connect vault revoke [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/connect/#connect-vault-revoke-flags "Direct link to Flags")
--server server The server to revoke access from.
--vault vault The vault to revoke a server's access to.
### Was this page helpful?
YesNo
