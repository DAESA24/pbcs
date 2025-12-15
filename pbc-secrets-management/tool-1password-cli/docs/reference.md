---
title: "1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/"
captured: 2025-12-15
category: concepts
relevance:
  - secret retrieval
  - environment variables
  - script integration
  - authentication
  - vault management
keywords:
  - op://
  - vault
  - item
  - field
  - secret reference
  - op read
  - op run
  - op item
  - op vault
  - op signin
related: []
---

# 1Password Developer

On this page
# 1Password CLI reference
If you're new to 1Password CLI, [learn how to set it up and sign in to your account](https://developer.1password.com/docs/cli/get-started/).
## Command structure[​](https://developer.1password.com/docs/cli/reference/#command-structure "Direct link to Command structure")
op [command] <flags>
1Password CLI uses a noun-verb command structure that groups commands by topic rather than by operation.
The basic structure of a command starts with the 1Password program `op`, then the command name (noun), often followed by a subcommand (verb), then flags (which include additional information that gets passed to the command).
For example, to retrieve a list of all the items in your Private vault:
op item list --vault Private
To get a list of all global commands and flags, run the following: ​
op --help
## Command reference[​](https://developer.1password.com/docs/cli/reference/#command-reference "Direct link to Command reference")
  * [account](https://developer.1password.com/docs/cli/reference/management-commands/account): Manage your locally configured 1Password accounts
  * [completion](https://developer.1password.com/docs/cli/reference/commands/completion): Generate shell completion information
  * [connect](https://developer.1password.com/docs/cli/reference/management-commands/connect): Manage Connect server instances and tokens in your 1Password account
  * [document](https://developer.1password.com/docs/cli/reference/management-commands/document): Perform CRUD operations on Document items in your vaults
  * [events-api](https://developer.1password.com/docs/cli/reference/management-commands/events-api): Manage Events API integrations in your 1Password account
  * [group](https://developer.1password.com/docs/cli/reference/management-commands/group): Manage the groups in your 1Password account
  * [inject](https://developer.1password.com/docs/cli/reference/commands/inject): Inject secrets into a config file
  * [item](https://developer.1password.com/docs/cli/reference/management-commands/item): Perform CRUD operations on the 1Password items in your vaults
  * [plugin](https://developer.1password.com/docs/cli/reference/management-commands/plugin): Manage the shell plugins you use to authenticate third-party CLIs
  * [read](https://developer.1password.com/docs/cli/reference/commands/read): Read a secret reference
  * [run](https://developer.1password.com/docs/cli/reference/commands/run): Pass secrets as environment variables to a process
  * [service-account](https://developer.1password.com/docs/cli/reference/management-commands/service-account): Manage service accounts
  * [signin](https://developer.1password.com/docs/cli/reference/commands/signin): Sign in to a 1Password account
  * [signout](https://developer.1password.com/docs/cli/reference/commands/signout): Sign out of a 1Password account
  * [update](https://developer.1password.com/docs/cli/reference/commands/update): Check for and download updates
  * [user](https://developer.1password.com/docs/cli/reference/management-commands/user): Manage users within this 1Password account
  * [vault](https://developer.1password.com/docs/cli/reference/management-commands/vault): Manage permissions and perform CRUD operations on your 1Password vaults
  * [whoami](https://developer.1password.com/docs/cli/reference/commands/whoami): Get information about a signed-in account


## Global flags[​](https://developer.1password.com/docs/cli/reference/#global-flags "Direct link to Global flags")
--account string Select the account to execute the command by account shorthand, sign-in address, account ID, or user ID. For a list of available accounts, run 'op account list'. Can be set as the OP_ACCOUNT environment variable.
--cache Store and use cached information. Caching is enabled by default on UNIX-like systems. Caching is not available on Windows. Options: true, false. Can also be set with the OP_CACHE environment variable. (default true)
--config directory Use this configuration directory.
--debug Enable debug mode. Can also be enabled by setting the OP_DEBUG environment variable to true.
--encoding type Use this character encoding type. Default: UTF-8. Supported: SHIFT_JIS, gbk.
--format string Use this output format. Can be 'human-readable' or 'json'. Can be set as the OP_FORMAT environment variable. (default "human-readable")
-h, --help Get help for op.
--iso-timestamps Format timestamps according to ISO 8601 / RFC 3339. Can be set as the OP_ISO_TIMESTAMPS environment variable.
--no-color Print output without color.
--session token Authenticate with this session token. 1Password CLI outputs session tokens for successful `op signin` commands when 1Password app integration is not enabled.
## Unique identifiers (IDs)[​](https://developer.1password.com/docs/cli/reference/#unique-identifiers-ids "Direct link to Unique identifiers \(IDs\)")
When you retrieve information about an object using the `get` and `list` subcommands, you'll see a string of 26 numbers and letters that make up the object's unique identifier (ID).
You can use names or IDs in commands that take any [account](https://developer.1password.com/docs/cli/reference/management-commands/account#account-get), [user](https://developer.1password.com/docs/cli/reference/management-commands/user#user-get), [vault](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-get), or [item](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get) as an argument.
IDs are the most stable way to reference an item. An item's ID only changes when you move the item to a different vault. Commands provided with an ID are also faster and more efficient.
You can get information about an item, including the item's ID and the ID for the vault where it's stored, with [`op item get`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get).
op item get Netflix
See result...
ID: t2Vz6kMDjByzEAcq6peKnHL4k3
Title: Netflix
Vault: Private (sdfsdf7werjgdf8gdfgjdfgkj)
Created: 6 months ago
Updated: 1 month ago by Wendy Appleseed
Favorite: false
Version: 1
Category: LOGIN
To only fetch the item ID, use the same command with the format set to JSON, then use 
op item get Netflix --format json | jq .id
See result...
"t2Vz6kMDjByzEAcq6peKnHL4k3"
To get the IDs for all vaults in an account:
op vault list
See result...
ID NAME
cfqtakqiutfhiewomztljx4woy Development
rr3ggvrlr6opoete23q7c22ahi Personal
2gq6v6vzorl7jfxdurns4hl66e Work
## Shell completion[​](https://developer.1password.com/docs/cli/reference/#shell-completion "Direct link to Shell completion")
You can add shell completion so that 1Password CLI automatically completes your commands.
With shell completion enabled, start typing an `op` command, then press Tab to see the available commands and options.
  * Bash
  * Zsh
  * fish
  * PowerShell


To enable shell completion with Bash:
  1. Install the bash-completion package
  2. Add this line to your `.bashrc` file:
source <(op completion bash)


To enable shell completion with Zsh, add this line to your `.zshrc` file:
eval "$(op completion zsh)"; compdef _op op
To enable shell completion with fish, add this to your `.fish` file:
op completion fish | source
To enable shell completion with PowerShell, add this to your `.ps1` file:
op completion powershell | Out-String | Invoke-Expression
You'll need to enable script execution in PowerShell to start using shell completion. To do that, start a PowerShell window as an administrator and enter:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
## Cache item and vault information[​](https://developer.1password.com/docs/cli/reference/#cache-item-and-vault-information "Direct link to Cache item and vault information")
1Password CLI can use its daemon process to cache items, vault information, and the keys to access information in an account.
The daemon stores encrypted information in memory using the same encryption methods as on 1Password.com. It can read the information to pass to 1Password CLI, but can’t decrypt it.
On UNIX-like systems, caching between commands is enabled by default. This helps maximize performance and reduce the number of API calls.
If you use 1Password CLI in an environment where caching is not possible, you can turn it off by appending the `--cache=false` flag to your commands, or by setting the `OP_CACHE` environment variable to false.
Caching is not currently available on Windows.
## Alternative character encoding[​](https://developer.1password.com/docs/cli/reference/#alternative-character-encoding "Direct link to Alternative character encoding")
By default, 1Password CLI processes input and output with UTF-8 encoding. You can use an alternative character encoding with the `--encoding` option.
Supported alternative character encoding types:
  * `gbk`
  * `shift-jis`


## Parse JSON output with jq[​](https://developer.1password.com/docs/cli/reference/#parse-json-output-with-jq "Direct link to Parse JSON output with jq")
You can use the `--format` flag or the `OP_FORMAT` environment variable to set your 1Password CLI command output to `json`.
To parse JSON output, we recommend using the command-line tool 
For example, to use jq to retrieve a secret reference for the password saved on an item named `GitHub`:
op item get GitHub --format json --fields password | jq .reference
See result...
"op://development/GitHub/password"
## Beta builds[​](https://developer.1password.com/docs/cli/reference/#beta-builds "Direct link to Beta builds")
To download 1Password CLI beta builds, navigate to **Show betas**. On Linux, you can switch the channel from "stable" to "beta" when adding the 1Password repository in your package manager.
## Example commands[​](https://developer.1password.com/docs/cli/reference/#example-commands "Direct link to Example commands")
### Items[​](https://developer.1password.com/docs/cli/reference/#items "Direct link to Items")
To get information about an item:
op item get <item name>
You'll see the item's [ID](https://developer.1password.com/docs/cli/reference/#unique-identifiers-ids), title, vault, when it was created, when it was last modified, the item's version, if it's marked as a favorite, the type of item it is, and the item's fields.
If an item name includes spaces or special characters, enclose it in quotes. For example:
op item get "work email"
See result...
ID: a5w3is43ohs25qonzajrqaqx4q
Title: work email
Vault: Work (2gq6v6vzorl7jfxdurns4hl66e)
Created: 6 years ago
Updated: 9 months ago by Wendy Appleseed
Favorite: true
Version: 1
Category: LOGIN
Fields:
username: wendy.c.appleseed@agilebits.com
password: NLuXcEtg27JMjGmiBHXZMGCgce
URLs:
website: https://www.gmail.com (primary)
To use `op item get` to retrieve specific fields, include the `--fields` flag followed by a comma-separated list, with the prefix `label=` before each field name. For example, to only retrieve the username and password for the item `work email`:
op item get "work email" --fields label=username,label=password
See result...
wendy.c.appleseed@agilebits.com,NLuXcEtg27JMjGmiBHXZMGCgce
Learn more about working with [items](https://developer.1password.com/docs/cli/reference/management-commands/item/).
### Users and groups[​](https://developer.1password.com/docs/cli/reference/#users-and-groups "Direct link to Users and groups")
To get details about a user:
op user get "Wendy Appleseed"
See result...
ID: SPRXJFTDHTA2DDTPE5F7DA64RQ
Name: Wendy Appleseed
Email: wendy.c.appleseed@agilebits.com
State: ACTIVE
Type: MEMBER
Created: 6 years ago
Updated: 4 months ago
Last Authentication: 1 month ago
To list the users who belong to a group:
op group user list "Provision Managers"
See result...
ID NAME EMAIL STATE TYPE ROLE
7YEOODASGJE6VAEIOHYWGP33II Wendy Appleseed wendy.c.appleseed@agilebits.com ACTIVE MEMBER
UKCYFVOJSFEXLKKZREG7M2MZWM Johnny Appleseed johnny.appleseed@agilebits.com RECOVERY_STARTED MEMBER
Learn more about working with [users](https://developer.1password.com/docs/cli/reference/management-commands/user/) and [groups](https://developer.1password.com/docs/cli/reference/management-commands/group/).
### Vaults[​](https://developer.1password.com/docs/cli/reference/#vaults "Direct link to Vaults")
To create a new vault named `Test`:
op vault create Test
To get details about an existing vault:
op vault get Work
See result...
ID: jAeq2tfunmifZfG4WkuWvsaGGj
Name: Work
Type: USER_CREATED
Attribute version: 3
Content version: 241
Items: 25
Created: 1 year ago
Updated: 1 month ago
To list the vaults in an account:
op vault list
See result...
ID NAME
vw8qjYEvsdCcZoULJRCqopy7Rv Development
2RNjh43dpHB9sDqZXEHiiw7zTe Personal
cGxbZbV2pxKBmVJe9oWja4K8km Work
Learn more about working with [vaults](https://developer.1password.com/docs/cli/reference/management-commands/vault/).
### Secrets[​](https://developer.1password.com/docs/cli/reference/#secrets "Direct link to Secrets")
To insert a secret into an environment variable, config file, or script without putting the plaintext secret in code, use a [secret reference](https://developer.1password.com/docs/cli/secret-reference-syntax/) that specifies where the secret is stored in your 1Password account:
op://vault-name/item-name/[section-name/]field-name
Then, you can use [`op read`](https://developer.1password.com/docs/cli/reference/commands/read/), [`op run`](https://developer.1password.com/docs/cli/reference/commands/run/), or [`op inject`](https://developer.1password.com/docs/cli/reference/commands/inject/) to replace the secret reference with the actual secret at runtime.
To resolve a secret reference and confirm it outputs correctly:
op read "op://Work/work email/username"
See result...
wendy.c.appleseed@agilebits.com
Learn more about [loading secrets](https://developer.1password.com/docs/cli/secret-references/).
## Get help[​](https://developer.1password.com/docs/cli/reference/#get-help "Direct link to Get help")
For help with any command, use the `--help` option:
op <command> [subcommand] --help
### Was this page helpful?
YesNo
