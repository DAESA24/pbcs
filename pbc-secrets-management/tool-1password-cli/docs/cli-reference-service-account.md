---
title: "service-account | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/service-account/"
captured: 2025-12-15
category: concepts
relevance:
  - secret retrieval
  - vault management
keywords:
  - vault
  - item
  - service account
related: []
---

# service-account | 1Password CLI | 1Password Developer

On this page
# service-account
Manage service accounts.
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/service-account/#subcommands "Direct link to Subcommands")
  * [service-account create](https://developer.1password.com/docs/cli/reference/management-commands/service-account/#service-account-create): Create a service account
  * [service-account ratelimit](https://developer.1password.com/docs/cli/reference/management-commands/service-account/#service-account-ratelimit): Retrieve rate limit usage for a service account


## service-account create[​](https://developer.1password.com/docs/cli/reference/management-commands/service-account/#service-account-create "Direct link to service-account create")
Create a service account to gain programmatic access to your secrets using 1Password CLI.
op service-account create <serviceAccountName> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/service-account/#service-account-create-flags "Direct link to Flags")
--can-create-vaults Allow the service account to create new vaults.
--expires-in duration Set how long the service account is valid for in (s)econds,
(m)inutes, (h)ours, (d)ays, or (w)eeks.
--raw Only return the service account token.
--vault stringArray Give access to this vault with a set of permissions. Has
syntax <vault-name>:<permission>[,<permission>]
You can specify the vaults the service account can access, as well as the permissions it will have for each vault using the `--vault` flag. The syntax looks like this:
--vault <vault-name>:<permission>,<permission>
The permissions can be one of the following:
  * `read_items`
  * `write_items` (requires `read_items`)
  * `share_items` (requires `read_items`)


If no permissions are specified, it will default to `read_items`.
You can set an expiry to a service account using the `--expires-in` flag.
1Password CLI only returns the service account token once. Save the token in 1Password immediately to avoid losing it. Treat this token like a password, and don't store it in plaintext.
You can't grant a service account access to your built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/service-account/#service-account-create-examples "Direct link to Examples")
Create a new service account:
op service-account create my-service-account --vault Dev:read_items --vault Test:read_items,write_items
Create a service account with an expiry:
op service-account create my-service-account --expires-in=24h
Create a service account that can create new vaults:
op service-account create my-service-account --can-create-vaults
## service-account ratelimit[​](https://developer.1password.com/docs/cli/reference/management-commands/service-account/#service-account-ratelimit "Direct link to service-account ratelimit")
Retrieve hourly and daily rate limit usage for a service account.
op service-account ratelimit [{ <serviceAccountName> | <serviceAccountID> }] [flags]
### Was this page helpful?
YesNo
