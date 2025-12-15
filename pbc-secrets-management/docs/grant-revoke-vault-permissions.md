---
title: "Grant and revoke vault permissions | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - item management
  - vault management
keywords:
  - vault
  - item
  - op vault
related: []
---

# Grant and revoke vault permissions | 1Password Developer

On this page
With 1Password CLI, you can manage the permissions each [user](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-user) or [group](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-group) has in each vault, so that everyone has access to the items they need.
Some permissions require [dependent permissions](https://developer.1password.com/docs/cli/vault-permissions/). On interactive shells, you can specify any permission, and 1Password CLI will ask you whether you want to add or revoke dependent permissions. If you're using scripts, or your shell isn't interactive, you must [include dependent permissions](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#scripting) in the command.
[Learn what permissions are available for your account type.](https://developer.1password.com/docs/cli/vault-permissions/)
## Requirements[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#requirements "Direct link to Requirements")
Before you can use 1Password CLI to manage vault permissions, you'll need to:
  * [Sign up for 1Password](https://1password.com/pricing/password-manager)
  * [Install 1Password CLI](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli)


You can manage vault permissions if you're an owner, administrator, or if you have the `manage_vault` permission in a vault.
## Grant permissions in vaults[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#grant-permissions-in-vaults "Direct link to Grant permissions in vaults")
### Users[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#users "Direct link to Users")
Use [`op vault user grant`](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-user-grant) to grant a user permissions in a vault.
For example, to grant the user Wendy Appleseed permission to edit items and manage vault permissions in the Prod vault:
op vault user grant --user wendy.appleseed@agilebits.com --vault Prod --permissions allow_editing,allow_managing
If the permissions you want to grant require dependent permissions to be granted alongside them, 1Password CLI will prompt you to grant those permissions:
In order to grant [allow_editing,allow_managing], the permission(s) [allow_viewing] are also required.
Would you like to grant them as well? [Y/n]
To confirm which users have access to a vault and their current permissions:
op vault user list <vault>
### Groups[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#groups "Direct link to Groups")
Use [`op vault group grant`](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-group-grant) to grant a group permissions in a vault.
For example, to grant the group IT permission to edit items and manage vault permissions in the Prod vault:
op vault group grant --group "IT" --vault Prod --permissions allow_editing,allow_managing
If the permissions you want to grant require dependent permissions to be granted alongside them, 1Password CLI will prompt you to grant those permissions:
In order to grant [allow_editing,allow_managing], the permission(s) [allow_viewing] are also required.
Would you like to grant them as well? [Y/n]
To confirm which groups have access to a vault and their current permissions:
op vault group list <vault>
## Revoke permissions in vaults[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#revoke-permissions-in-vaults "Direct link to Revoke permissions in vaults")
### Users[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#users-1 "Direct link to Users")
Use [`op vault user revoke`](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-user-revoke) to revoke a user's permissions in a vault.
For example, to revoke the user Wendy Appleseed's permission to view items in the Prod vault:
op vault user revoke --user wendy.appleseed@agilebits.com --vault Prod --permissions allow_viewing
If the permission you want to revoke requires dependent permissions to be revoked alongside it, 1Password CLI will prompt you to revoke those permissions:
In order to revoke [allow_viewing], the permission(s) [allow_editing,allow_managing] are also required.
Would you like to revoke them as well? [Y/n]
To confirm that the user's permissions have been revoked:
op vault user list <vault>
### Groups[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#groups-1 "Direct link to Groups")
Use [`op vault group revoke`](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-group-grant) to revoke a group's permissions in a vault.
For example, to revoke the group IT's permission to view items in the Prod vault:
op vault group revoke --group "IT" --vault Prod --permissions allow_viewing
If the permission you want to revoke requires dependent permissions to be revoked alongside it, 1Password CLI will prompt you to revoke those permissions:
In order to revoke [allow_viewing], the permission(s) [allow_editing,allow_managing] are also required.
Would you like to revoke them as well? [Y/n]
To confirm the group's permissions have been revoked:
op vault group list <vault>
## Scripting[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#scripting "Direct link to Scripting")
If you're using scripts to grant and revoke vault permissions, or if your shell isn't interactive, you'll need to include the `--no-input` flag and specify all [dependent permissions](https://developer.1password.com/docs/cli/vault-permissions/) in a comma-separated list after the `--permissions` flag.
For example, the `allow_managing` permission requires the `allow_editing` and `allow_viewing` permission. To grant the user Wendy Appleseed permission to manage vault permissions in the Prod vault:
op vault user grant --no-input --user wendy.appleseed@agilebits.com --vault Prod --permissions allow_managing,allow_editing,allow_viewing
To revoke `allow_editing` from a group that currently also has `allow_managing` granted in a vault:
  

op vault group revoke --no-input --group "IT" --vault Prod --permissions allow_managing,allow_editing
## Learn more[​](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/#learn-more "Direct link to Learn more")
  * [Vault permission dependencies](https://developer.1password.com/docs/cli/vault-permissions/)


### Was this page helpful?
YesNo
