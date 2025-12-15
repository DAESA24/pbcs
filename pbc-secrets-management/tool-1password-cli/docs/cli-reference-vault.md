---
title: "vault | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/vault/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - vault management
keywords:
  - vault
  - item
  - op vault
related: []
---

# vault | 1Password CLI | 1Password Developer

On this page
# vault
Manage permissions and perform CRUD operations on your 1Password vaults.
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#subcommands "Direct link to Subcommands")
  * [vault create](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-create): Create a new vault
  * [vault delete](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-delete): Remove a vault
  * [vault edit](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-edit): Edit a vault's name, description, icon, or Travel Mode status
  * [vault get](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-get): Get details about a vault
  * [vault group](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group): Manage group vault access
  * [vault list](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-list): List all vaults in the account
  * [vault user](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user): Manage user vault access


## vault create[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-create "Direct link to vault create")
Create a new vault
op vault create <name> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-create-flags "Direct link to Flags")
--allow-admins-to-manage true|false Set whether administrators can manage the vault.
If not provided, the default policy for the account applies.
--description description Set the vault's description.
--icon string Set the vault icon.
Valid icon keywords are: airplane, application, art-supplies, bankers-box, brown-briefcase, brown-gate, buildings, cabin, castle, circle-of-dots, coffee, color-wheel, curtained-window, document, doughnut, fence, galaxy, gears, globe, green-backpack, green-gem, handshake, heart-with-monitor, house, id-card, jet, large-ship, luggage, plant, porthole, puzzle, rainbow, record, round-door, sandals, scales, screwdriver, shop, tall-window, treasure-chest, vault-door, vehicle, wallet, wrench
## vault delete[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-delete "Direct link to vault delete")
Remove a vault. Specify the vault to delete by name or ID.
op vault delete [{ <vaultName> | <vaultID> | - }] [flags]
A vault may be specified by name or ID.
## vault edit[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-edit "Direct link to vault edit")
Edit a vault's name, description, icon, or Travel Mode status. Specify the vault by name or ID.
op vault edit [{ <vaultName> | <vaultID> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-edit-flags "Direct link to Flags")
--description description Change the vault's description.
--icon icon Change the vault's icon.
--name name Change the vault's name.
--travel-mode on|off Turn Travel Mode on or off for the vault. Only vaults
with Travel Mode enabled are accessible while a user has Travel Mode turned on. (default off)
A vault may be specified by name or ID.
Valid icon keywords are: airplane, application, art-supplies, bankers-box, brown-briefcase, brown-gate, buildings, cabin, castle, circle-of-dots, coffee, color-wheel, curtained-window, document, doughnut, fence, galaxy, gears, globe, green-backpack, green-gem, handshake, heart-with-monitor, house, id-card, jet, large-ship, luggage, plant, porthole, puzzle, rainbow, record, round-door, sandals, scales, screwdriver, shop, tall-window, treasure-chest, vault-door, vehicle, wallet, wrench
## vault get[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-get "Direct link to vault get")
Get details about a vault. Specify the vault by name or ID.
op vault get [{ <vaultName> | <vaultID> | - }] [flags]
A vault may be specified by name or ID.
#### Use standard input to specify objects[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#use-standard-input-to-specify-objects "Direct link to Use standard input to specify objects")
If you enter a hyphen (`-`) instead of a single object for this command, the tool will read object specifiers from standard input (stdin). Separate each specifier with a new line. For more information about how to specify objects, run `op help`.
You can also pass the command a list or array of JSON objects. The tool will get an item for any object that has an ID, ignoring line breaks. This is useful for passing information from one `op` command to another.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-get-examples "Direct link to Examples")
Get details for all vaults:
op vault list --format=json | op vault get -
Get details for the vaults that a group has access to:
op vault list --group security --format=json | op vault get -
## vault group[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group "Direct link to vault group")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-subcommands "Direct link to Subcommands")
  * [vault group grant](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-grant): Grant a group permissions to a vault
  * [vault group list](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-list): List all the groups that have access to the given vault
  * [vault group revoke](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-revoke): Revoke a portion or the entire access of a group to a vault


## vault group grant[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-grant "Direct link to vault group grant")
Grant a group permissions in a vault.
op vault group grant [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-grant-flags "Direct link to Flags")
--group group The group to receive access.
--no-input input Do not prompt for input on interactive terminal.
--permissions permissions The permissions to grant to the group.
--vault vault The vault to grant group permissions to.
Permissions are specified in a comma separated list such as:
view_items,view_and_copy_passwords,edit_items
1Password Teams includes three permissions:
allow_viewing, allow_editing, allow_managing
1Password Business includes the permissions above as well as more granular options:
allow_viewing
view_items, view_and_copy_passwords, view_item_history
allow_editing
create_items, edit_items, archive_items, delete_items, import_items,
export_items, copy_and_share_items, print_items
allow_managing
manage_vault
When granting or revoking permissions, some permissions require dependent permissions to be granted or revoked alongside them.
[Learn more about managing vault permissions.](https://developer.1password.com/docs/cli/vault-permissions/)
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-grant-examples "Direct link to Examples")
Grant a group certain permissions in a vault with a business account:
op vault group grant --vault VAULT --group GROUP \
--permissions view_items,create_items,allow_viewing
op vault group grant --vault VAULT --group GROUP \
--permissions allow_viewing,export_items
Grant a group certain permissions in a vault with a team account:
op vault group grant --vault VAULT --group GROUP \
--permissions allow_viewing,allow_editing
## vault group list[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-list "Direct link to vault group list")
List all the groups that have access to the given vault.
op vault group list [{ <vault> | - }] [flags]
## vault group revoke[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-revoke "Direct link to vault group revoke")
Revoke a group's permissions in a vault, in part or in full.
op vault group revoke [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-revoke-flags "Direct link to Flags")
--group group The group to revoke access from.
--no-input input Do not prompt for input on interactive terminal.
--permissions permissions The permissions to revoke from the group.
--vault vault The vault to revoke access to.
Not specifying any permissions revokes the group's access to the vault.
Removing all existing permissions also revokes the group’s access to the vault.
Permissions are specified in a comma separated list such as:
view_items,view_and_copy_passwords,edit_items
1Password Teams includes three permissions:
allow_viewing, allow_editing, allow_managing
1Password Business includes the permissions above as well as more granular options:
allow_viewing
view_items, view_and_copy_passwords, view_item_history
allow_editing
create_items, edit_items, archive_items, delete_items, import_items,
export_items, copy_and_share_items, print_items
allow_managing
manage_vault
When granting or revoking permissions, some permissions require dependent permissions to be granted or revoked alongside them.
[Learn more about managing vault permissions.](https://developer.1password.com/docs/cli/vault-permissions/)
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-group-revoke-examples "Direct link to Examples")
Remove a group from a vault:
op vault group revoke --vault VAULT --group GROUP
Revoke certain permissions from a group in a vault with a business account:
op vault group revoke --vault VAULT --group GROUP \
--permissions view_items,create_items,allow_editing
Revoke certain permissions from a group in a vault with a team account:
op vault group revoke --vault VAULT --group GROUP \
--permissions allow_viewing,allow_editing
## vault list[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-list "Direct link to vault list")
List vaults.
op vault list [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-list-flags "Direct link to Flags")
--group string List vaults a group has access to.
--permission permissions List only vaults that the specified user/group has this permission for.
--user string List vaults that a given user has access to.
By default, returns all vaults the current user has read access to.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-list-examples "Direct link to Examples")
Get details for all vaults:
op vault list --format=json | op vault get -
Get details for vaults that a group has access to:
op vault list --group Security --format=json | op vault get -
Get details for vaults that a user has access to:
op vault list --user wendy_appleseed@1password.com --format=json | op vault get -
Only list vaults for which the user/group has a specific set of permissions:
op vault list --user wendy_appleseed@1password.com --permission manage_vault
## vault user[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user "Direct link to vault user")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-subcommands "Direct link to Subcommands")
  * [vault user grant](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-grant): Grant a user access to a vault
  * [vault user list](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-list): List all users with access to the vault and their permissions
  * [vault user revoke](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-revoke): Revoke a portion or the entire access of a user to a vault


## vault user grant[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-grant "Direct link to vault user grant")
Grant a user permissions in a vault.
op vault user grant [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-grant-flags "Direct link to Flags")
--no-input input Do not prompt for input on interactive terminal.
--permissions permissions The permissions to grant to the user.
--user user The user to receive access.
--vault vault The vault to grant access to.
Permissions are specified in a comma separated list such as:
view_items,view_and_copy_passwords,edit_items
1Password Teams and 1Password Families include three permissions:
allow_viewing, allow_editing, allow_managing
1Password Business includes the permissions above as well as more granular options:
allow_viewing
view_items, view_and_copy_passwords, view_item_history
allow_editing
create_items, edit_items, archive_items, delete_items, import_items,
export_items, copy_and_share_items, print_items
allow_managing
manage_vault
When granting or revoking permissions, some permissions require dependent permissions to be granted or revoked alongside them.
[Learn more about managing vault permissions.](https://developer.1password.com/docs/cli/vault-permissions/)
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-grant-examples "Direct link to Examples")
Grant a user certain permissions in a vault with a business account:
op vault user grant --vault VAULT --user USER \
--permissions view_items,create_items,allow_viewing
op vault user grant --vault VAULT --user USER \
--permissions allow_viewing,export_items
Grant a user certain permissions in a vault with a team account:
op vault user grant --vault VAULT --user USER \
--permissions allow_viewing,allow_editing
## vault user list[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-list "Direct link to vault user list")
List all users with access to the vault and their permissions.
op vault user list <vault> [flags]
## vault user revoke[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-revoke "Direct link to vault user revoke")
Revoke a user's permissions in a vault, in part or in full.
op vault user revoke [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-revoke-flags "Direct link to Flags")
--no-input input Do not prompt for input on interactive terminal.
--permissions permissions The permissions to revoke from the user.
--user user The user to revoke access from.
--vault vault The vault to revoke access to.
Not specifying any permissions revokes the user's access to the vault.
Removing all existing permissions also revokes the user’s access to the vault.
Permissions are specified in a comma separated list such as:
view_items,view_and_copy_passwords,edit_items
1Password Teams and 1Password Families include three permissions:
allow_viewing, allow_editing, allow_managing
1Password Business includes the permissions above as well as more granular options:
allow_viewing
view_items, view_and_copy_passwords, view_item_history
allow_editing
create_items, edit_items, archive_items, delete_items, import_items,
export_items, copy_and_share_items, print_items
allow_managing
manage_vault
When granting or revoking permissions, some permissions require dependent permissions to be granted or revoked alongside them.
[Learn more about managing vault permissions.](https://developer.1password.com/docs/cli/vault-permissions/)
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/vault/#vault-user-revoke-examples "Direct link to Examples")
Remove a user from a vault:
op vault user revoke --vault VAULT --user USER
Revoke certain permissions from a user in a vault with a business account:
op vault user revoke --vault VAULT --user USER \
--permissions view_items,create_items,allow_editing
Revoke certain permissions from a user in a vault with a team account:
op vault user revoke --vault VAULT --user USER \
--permissions allow_viewing,allow_editing
### Was this page helpful?
YesNo
