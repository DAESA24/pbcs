---
title: "group | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/group/"
captured: 2025-12-15
category: concepts
relevance:
  - secret retrieval
  - script integration
  - vault management
keywords:
  - vault
  - item
related: []
---

# group | 1Password CLI | 1Password Developer

On this page
# group
Manage the groups in your 1Password account.
Groups can be used to organize your team and delegate administrative responsibilities. You can give groups access to vaults and assign them permissions, so you don't have to keep track of everyone separately.
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#subcommands "Direct link to Subcommands")
  * [group create](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-create): Create a group
  * [group delete](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-delete): Remove a group
  * [group edit](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-edit): Edit a group's name or description
  * [group get](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-get): Get details about a group
  * [group list](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-list): List groups
  * [group user](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user): Manage group membership


## group create[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-create "Direct link to group create")
Create a group and receive a JSON object with the group's ID.
op group create <name> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-create-flags "Direct link to Flags")
--description string Set the group's description.
## group delete[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-delete "Direct link to group delete")
Remove a group. Specify the group to delete by its name or ID.
op group delete [{ <groupName> | <groupID> | - }] [flags]
## group edit[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-edit "Direct link to group edit")
Edit a group's name or description. Specify the group to edit by its name or ID.
op group edit [{ <groupName> | <groupID> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-edit-flags "Direct link to Flags")
--description description Change the group's description.
--name name Change the group's name.
## group get[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-get "Direct link to group get")
Get details about a group. Specify the group by its name or ID.
op group get [{ <groupName> | <groupID> | - }] [flags]
#### Use standard input to specify objects[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#use-standard-input-to-specify-objects "Direct link to Use standard input to specify objects")
If you enter a hyphen (`-`) instead of a single object for this command, the tool will read object specifiers from standard input (stdin). Separate each specifier with a new line. For more information about how to specify objects, run `op help`.
You can also pass the command a list or array of JSON objects. The tool will get an item for any object that has an ID, ignoring line breaks. This is useful for passing information from one `op` command to another.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-get-examples "Direct link to Examples")
Get details for all groups:
op group list --format=json | op group get -
Get details for the groups who have access to a vault:
op group list --vault "Production keys" --format=json | op group get -
## group list[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-list "Direct link to group list")
List groups.
op group list [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-list-flags "Direct link to Flags")
--user user List groups that a user belongs to.
--vault vault List groups that have direct access to a vault.
Returns all groups in an account by default.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-list-examples "Direct link to Examples")
Get details for all groups:
op group list | op group get -
Get details for the groups that have access to a vault:
op group list --vault Staging --format=json | op group get -
Get details for the groups that a user belongs to:
op group list --user wendy_appleseed@1password.com --format=json | op group get -
## group user[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user "Direct link to group user")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-subcommands "Direct link to Subcommands")
  * [group user grant](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-grant): Add a user to a group
  * [group user list](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-list): Retrieve users that belong to a group
  * [group user revoke](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-revoke): Remove a user from a group


## group user grant[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-grant "Direct link to group user grant")
Grant a user access to a group.
op group user grant [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-grant-flags "Direct link to Flags")
--group string Specify the group to grant the user access to.
--role string Specify the user's role as a member or manager. Default: member.
--user string Specify the user to grant group access to.
## group user list[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-list "Direct link to group user list")
Retrieve users that belong to a group.
op group user list <group> [flags]
## group user revoke[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-revoke "Direct link to group user revoke")
Revoke a user's access to a group.
op group user revoke [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/group/#group-user-revoke-flags "Direct link to Flags")
--group string Specify the group to remove the user from.
--help Get help with group user revoke.
--user string Specify the user to remove from the group.
### Was this page helpful?
YesNo
