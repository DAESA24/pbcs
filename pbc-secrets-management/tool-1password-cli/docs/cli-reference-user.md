---
title: "user | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/user/"
captured: 2025-12-15
category: concepts
relevance:
  - authentication
  - vault management
keywords:
  - vault
  - item
related: []
---

# user | 1Password CLI | 1Password Developer

On this page
# user
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#subcommands "Direct link to Subcommands")
  * [user confirm](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-confirm): Confirm a user
  * [user delete](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-delete): Remove a user and all their data from the account
  * [user edit](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-edit): Edit a user's name or Travel Mode status
  * [user get](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-get): Get details about a user
  * [user list](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-list): List users
  * [user provision](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-provision): Provision a user in the authenticated account
  * [user reactivate](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-reactivate): Reactivate a suspended user
  * [user recovery](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-recovery): Manage user recovery in your 1Password account
  * [user suspend](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-suspend): Suspend a user


## user confirm[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-confirm "Direct link to user confirm")
Specify the user by their e-mail address, name, or ID.
op user confirm [{ <email> | <name> | <userID> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-confirm-flags "Direct link to Flags")
--all Confirm all unconfirmed users.
Specify the user by their e-mail address, name, or ID.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-confirm-examples "Direct link to Examples")
Confirm a user by specifying their name:
op user confirm "Wendy Appleseed"
Confirm a user by specifying their email:
op user confirm "wendy.appleseed@example.com"
## user delete[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-delete "Direct link to user delete")
Remove a user and all their data from the account.
op user delete [{ <email> | <name> | <userID> | - }] [flags]
Specify the user by their e-mail address, name, or ID.
## user edit[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-edit "Direct link to user edit")
Change a user's name or Travel Mode status.
op user edit [{ <email> | <name> | <userID> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-edit-flags "Direct link to Flags")
--name string Set the user's name.
--travel-mode on|off Turn Travel Mode on or off for the user. (default off)
Specify the user by their e-mail address, name, or ID.
## user get[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-get "Direct link to user get")
Get details about a user.
op user get [{ <email> | <name> | <userID> | --me | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-get-flags "Direct link to Flags")
--fingerprint Get the user's public key fingerprint.
--me Get the authenticated user's details.
--public-key Get the user's public key.
Specify the user by their e-mail address, name, or ID.
#### Use standard input to specify objects[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#use-standard-input-to-specify-objects "Direct link to Use standard input to specify objects")
If you enter a hyphen (`-`) instead of a single object for this command, the tool will read object specifiers from standard input (stdin). Separate each specifier with a new line. For more information about how to specify objects, run `op help`.
You can also pass the command a list or array of JSON objects. The tool will get an item for any object that has an ID, ignoring line breaks. This is useful for passing information from one `op` command to another.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-get-examples "Direct link to Examples")
Look up a user by name:
op user get "Wendy Appleseed"
Look up a user by e-mail:
op user get wendy.appleseed@example.com
Get details for all users:
op user list --format=json | op user get -
Get the public key for all users in a group:
op user list --group "Frontend Developers" --format=json | op user get - --publickey
Get details for all users who have access to a vault:
op user list --vault Staging --format=json | op user get -
## user list[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-list "Direct link to user list")
List users.
op user list [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-list-flags "Direct link to Flags")
--group group List users who belong to a group.
--vault vault List users who have direct access to vault.
Returns all users in an account by default. Use flags to filter results.
When you use the `--group` option, the output includes the user's role in the group.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-list-examples "Direct link to Examples")
Get details for all users:
op user list --format=json | op user get -
Get the public key for all users in a group:
op user list --group "Frontend Developers" --format=json | op user get - --publickey
Get details for all users who have access to a vault:
op user list --vault Staging --format=json | op user get -
## user provision[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-provision "Direct link to user provision")
Provision a user in the authenticated account.
op user provision [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-provision-flags "Direct link to Flags")
--email string Provide the user's email address.
--language string Provide the user's account language. (default "en")
--name string Provide the user's name.
Provisioned users will receive an invitation email to join the 1Password account.
Once a user accepts an invitation, an admin must confirm them on 1Password.com or using the `op user confirm` command.
Invited users will not be considered for billing until they accept their invitation.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-provision-examples "Direct link to Examples")
Invite a user by specifying their e-mail address and name:
op user provision --name "Wendy Appleseed" --email "wendy.appleseed@example.com"
## user reactivate[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-reactivate "Direct link to user reactivate")
Reactivate a suspended user.
op user reactivate [{ <email> | <name> | <userID> | - }] [flags]
A user may be specified by their e-mail address, name, or ID.
## user recovery[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-recovery "Direct link to user recovery")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-recovery-subcommands "Direct link to Subcommands")
  * [user recovery begin](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-recovery-begin): Begin recovery for users in your 1Password account


## user recovery begin[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-recovery-begin "Direct link to user recovery begin")
Begin recovery for users in your 1Password account:
op user recovery begin [ { <email> | <name> | <userID> } ] [flags]
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-recovery-begin-examples "Direct link to Examples")
Begin recovery for multiple users by UUID:
op user recovery begin ZMAE4RTRONHN7LGELNYYO373KM WHPOFIMMYFFITBVTOTZUR3R324
## user suspend[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-suspend "Direct link to user suspend")
Suspend a user.
op user suspend [{ <email> | <name> | <userID> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/user/#user-suspend-flags "Direct link to Flags")
--deauthorize-devices-after duration Deauthorize the user's devices after a time
(rounded down to seconds).
Specify the user by their e-mail address, name, or ID.
A suspended user will immediately be logged out of all devices and will not be able to log in or access any data.
Users in a suspended state are not considered in billing.
You can reactivate a suspended user with the `op user reactivate` command.
### Was this page helpful?
YesNo
