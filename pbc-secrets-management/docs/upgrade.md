---
title: "Upgrade to 1Password CLI 2 | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/upgrade/"
captured: 2025-12-15
category: concepts
relevance:
  - environment variables
  - script integration
  - authentication
  - item management
  - vault management
keywords:
  - vault
  - item
  - field
  - op item
  - environment variable
  - template
  - biometric
related: []
---

# Upgrade to 1Password CLI 2 | 1Password Developer

On this page
# Upgrade to 1Password CLI 2
_Learn how to[upgrade to 1Password CLI 2](https://developer.1password.com/docs/cli/upgrade/#step-1-choose-an-upgrade-strategy) from an earlier version, and [update your scripts](https://developer.1password.com/docs/cli/upgrade/#step-2-update-your-scripts) to the new command syntax._
1Password CLI 1 is deprecated as of **October 1, 2024**. Upgrade to 1Password CLI 2 to avoid disruptions with scripts or integrations that use version 1.
### About 1Password CLI 2[​](https://developer.1password.com/docs/cli/upgrade/#about-1password-cli-2 "Direct link to About 1Password CLI 2")
We released version 2 of the 1Password CLI in March 2022. Since then, more than 96% of users have adopted the latest version.
1Password CLI 2 includes a number of changes to the schema to make the tool easier to use as well as new features to help you provision secrets.
#### New schema[​](https://developer.1password.com/docs/cli/upgrade/#new-schema "Direct link to New schema")
1Password CLI 2 introduces a noun-verb command structure that groups commands by topic rather than by operation. You can find all available topics with `op --help`, and see the commands avaialble for each topic with `op <topic> --help`. Topics include:
  * [vault](https://developer.1password.com/docs/cli/reference/management-commands/vault/)
  * [item](https://developer.1password.com/docs/cli/reference/management-commands/item/)
  * [document](https://developer.1password.com/docs/cli/reference/management-commands/document/)
  * [user](https://developer.1password.com/docs/cli/reference/management-commands/user/)
  * [group](https://developer.1password.com/docs/cli/reference/management-commands/group/)
  * [account](https://developer.1password.com/docs/cli/reference/management-commands/account/)
  * [connect](https://developer.1password.com/docs/cli/reference/management-commands/connect/)
  * [events-api](https://developer.1password.com/docs/cli/reference/management-commands/events-api/)


Other schema changes include:
  * The default output is now a human-friendly, tabular schema.  
[Learn how to change the default output to JSON.](https://developer.1password.com/docs/cli/upgrade/#json-default)
  * The JSON output schema now contains more useful information.
  * Improved stdin processing allows you to chain more commands together.
  * The new schema uses flags instead of positional arguments.


#### Secrets provisioning[​](https://developer.1password.com/docs/cli/upgrade/#secrets-provisioning "Direct link to Secrets provisioning")
To help you provision secrets locally, 1Password CLI 2 allows you to load secrets directly from 1Password in environment variables and configuration files. With secrets provisioning, you can replace your plaintext secrets with references to the secrets stored in 1Password and load them at runtime in your scripts, applications, and other workflows.
#### Integrate 1Password CLI with the 1Password desktop app[​](https://developer.1password.com/docs/cli/upgrade/#integrate-1password-cli-with-the-1password-desktop-app "Direct link to Integrate 1Password CLI with the 1Password desktop app")
You can sign in to 1Password CLI 2 with the accounts you've added to the 1Password desktop app, then authenticate your accounts on the command line with biometrics.
#### Shell plugins[​](https://developer.1password.com/docs/cli/upgrade/#shell-plugins "Direct link to Shell plugins")
To simplify and secure your workflow, 1Password CLI 2 introduces shell plugins that allow you to securely authenticate third-party command-line tools using biometrics.
#### Package manager installation[​](https://developer.1password.com/docs/cli/upgrade/#package-manager-installation "Direct link to Package manager installation")
1Password CLI 2 supports easier installation with package managers including Apt, Yum, Alpine, and tar.
You can [find all changes in the changelog](https://releases.1password.com/developers/cli/).
To share feedback with us, 
## Step 1: Choose an upgrade strategy[​](https://developer.1password.com/docs/cli/upgrade/#step-1-choose-an-upgrade-strategy "Direct link to Step 1: Choose an upgrade strategy")
There are multiple ways to upgrade to 1Password CLI 2. You can upgrade immediately or gradually, depending on your workflow and toolchain.
### Upgrade immediately[​](https://developer.1password.com/docs/cli/upgrade/#upgrade-immediately "Direct link to Upgrade immediately")
The quickest way to upgrade to 1Password CLI 2 is to overwrite your existing installation. This is a good option if you have a small team who can upgrade their local installations simultaneously.
  1. Use `which op` (or `(Get-Command op).Path` on Windows) to get the directory of the current installation.
  2. `op` to the same directory, overwriting the existing copy.
  3. To verify the installation, check the version number:
op --version
  4. [Update your scripts to use the 1Password CLI 2 syntax.](https://developer.1password.com/docs/cli/upgrade/#step-2-update-your-scripts)


Make sure everyone on your team upgrades to 1Password CLI 2. After you update your scripts, they won't work with earlier versions of 1Password CLI.
### Upgrade gradually[​](https://developer.1password.com/docs/cli/upgrade/#upgrade-gradually "Direct link to Upgrade gradually")
If you're not ready to upgrade immediately, you can use Docker to upgrade individual projects or use both versions of 1Password CLI side-by-side. We will continue to support version 1 for one year after version 2 is released.
#### Use Docker to upgrade individual projects[​](https://developer.1password.com/docs/cli/upgrade/#use-docker-to-upgrade-individual-projects "Direct link to Use Docker to upgrade individual projects")
If you want to upgrade project by project, you can Dockerize your workflow so that each team member uses the version of 1Password CLI in a Docker image for a specific project. This is a good option for large teams, because it doesn't require each team member to update a local installation.
  1. [add the CLI](https://developer.1password.com/docs/cli/get-started/). Your Dockerfile should look like this:
FROM 1password/op:2
COPY ./your-script.sh /your-script.sh
CMD ["/your-script.sh"]
  2. After upgrading to 1Password CLI 2, [update your scripts](https://developer.1password.com/docs/cli/upgrade/#step-2-update-your-scripts) to use the new command syntax.


This approach also sets you up to move your scripts to headless environments such as CI/CD pipelines.
#### Use both versions of 1Password CLI[​](https://developer.1password.com/docs/cli/upgrade/#use-both-versions-of-1password-cli "Direct link to Use both versions of 1Password CLI")
If your scripts depend on the local installation on each team member's machine, and you still want to migrate gradually, this is your best option.
Each team member should do the following:
  1. Rename the earlier version of 1Password CLI `op1`.
  2. Find and replace all occurences of `op` with `op1`.
  3. Install `$PATH`. 
For macOS 1Password CLI 2 has to be moved _exactly_ to `/usr/local/bin/op`.  
For Linux, it is recommended to be moved to `/usr/local/bin/op`.
  4. [Update your scripts](https://developer.1password.com/docs/cli/upgrade/#step-2-update-your-scripts) one-by-one to use the new `op`. You can continue to use your current scripts with the earlier version of 1Password CLI installed as `op1`.
  5. When you've updated all your scripts and are ready to upgrade, uninstall the earlier version of 1Password CLI.
  6. Find and replace all occurrences of `op1` in your scripts to `op`.


## Step 2: Update your scripts[​](https://developer.1password.com/docs/cli/upgrade/#step-2-update-your-scripts "Direct link to Step 2: Update your scripts")
If you've been using an earlier version of 1Password CLI in scripts, you'll need to update your scripts to the new syntax.
After you install 1Password CLI 2, use the following table to update your scripts. It shows all the updated commands and associated changes to arguments or flags.
Old command | CLI 2 command | Notes  
---|---|---  
[create vault](https://developer.1password.com/docs/cli/v1/reference#create-vault) | [vault create](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-create) |   
[get vault](https://developer.1password.com/docs/cli/v1/reference#get-vault) | [vault get](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-get) |   
[edit vault](https://developer.1password.com/docs/cli/v1/reference#edit-vault) | [vault edit](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-edit) |  `--travel-mode=on/off` flag introduced  
[delete vault](https://developer.1password.com/docs/cli/v1/reference#delete-vault) | [vault delete](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-delete) | allows piped input when the `-` argument is provided  
[list vaults](https://developer.1password.com/docs/cli/v1/reference#list-vaults) | [vault list](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-list) | 
  * by default, lists vaults you have read access to
  * to see all the vaults you can manage, include `--permission manage`

  
[list users --vault](https://developer.1password.com/docs/cli/v1/reference#list-users) | [vault user list](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-user-list) |   
[add group](https://developer.1password.com/docs/cli/v1/reference#add-group) | [vault group grant](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-group-grant) | 
  * `--permission` flag must be used to specify the permissions to grant
  * granting allow_viewing, allow_editing and allow_managing is equivalent to granting all permissions
  * `group` and `vault` arguments changed to `--group` and `--vault` flags

  
[remove group](https://developer.1password.com/docs/cli/v1/reference#remove-group) | [vault group revoke](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-group-revoke) | 
  * `--permission` flag must be used to specify the permissions to revoke
  * revoking allow_viewing, allow_editing, and allow_managing is equivalent to revoking all permissions
  * `group` and `vault` arguments changed to `--group` and `--vault` flags

  
[add user](https://developer.1password.com/docs/cli/v1/reference#add-user) <user> <vault> | [vault user grant](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-user-grant) | 
  * `--permission` flag must be used to specify the permissions to grant
  * granting allow_viewing, allow_editing and allow_managing is equivalent to granting all permissions
  * `user` and `vault` arguments changed to `--user` and `--vault` flags

  
[remove user](https://developer.1password.com/docs/cli/v1/reference#remove-user) <user> <vault> | [vault user revoke](https://developer.1password.com/docs/cli/reference/management-commands/vault#vault-user-revoke) | 
  * `--permission` flag must be used to specify the permissions to revoke
  * revoking allow_viewing, allow_editing and allow_managing is equivalent to revoking all permissions
  * `user` and `vault` arguments changed to `--user` and `--vault` flags

  
[signin](https://developer.1password.com/docs/cli/v1/reference#signin) <url> | [account add](https://developer.1password.com/docs/cli/reference/management-commands/account#account-add) | 
  * for new accounts/urls
  * the password can be piped in if email, address, and secret key are provided via flag

  
[signin](https://developer.1password.com/docs/cli/v1/reference#signin) --list | [account list](https://developer.1password.com/docs/cli/reference/management-commands/account#account-list) | account list will format its output based on output format selection (JSON vs human readable)  
[forget account](https://developer.1password.com/docs/cli/v1/reference#forget) | [account forget](https://developer.1password.com/docs/cli/reference/management-commands/account#account-forget) | new `-—all` flag for forgetting all accounts  
[get account](https://developer.1password.com/docs/cli/v1/reference#get-account) | [account get](https://developer.1password.com/docs/cli/reference/management-commands/account#account-get) |   
[confirm user](https://developer.1password.com/docs/cli/v1/reference#confirm) | [user confirm](https://developer.1password.com/docs/cli/reference/management-commands/user#user-confirm) | allows piped input when the `-` argument is provided  
[create user](https://developer.1password.com/docs/cli/v1/reference#create-user) | [user provision](https://developer.1password.com/docs/cli/reference/management-commands/user#user-provision) |  `email` and `name` arguments changed to `--email` and `--name` flags  
[delete user](https://developer.1password.com/docs/cli/v1/reference#delete-user) | [user delete](https://developer.1password.com/docs/cli/reference/management-commands/user#user-delete) | allows piped input when the `-` argument is provided  
[edit user](https://developer.1password.com/docs/cli/v1/reference#edit-user) | [user edit](https://developer.1password.com/docs/cli/reference/management-commands/user#user-edit) | allows piped input when the `-` argument is provided  
[reactivate user](https://developer.1password.com/docs/cli/v1/reference#reactivate) | [user reactivate](https://developer.1password.com/docs/cli/reference/management-commands/user#user-reactivate) | allows piped input when the `-` argument is provided  
[suspend user](https://developer.1password.com/docs/cli/v1/reference#suspend) | [user suspend](https://developer.1password.com/docs/cli/reference/management-commands/user#user-suspend) |  `--deauthorize-devices-after` flag accepts any duration unit, not just seconds  
[list users](https://developer.1password.com/docs/cli/v1/reference#list-users) | [user list](https://developer.1password.com/docs/cli/reference/management-commands/user#user-list) |   
[get user](https://developer.1password.com/docs/cli/v1/reference#get-user) | [user get](https://developer.1password.com/docs/cli/reference/management-commands/user#user-get) | 
  * added `-—me` flag to get the currently authenticated user
  * `—publickey` changed to `—public-key`

  
[create connect server](https://developer.1password.com/docs/cli/v1/reference#create-connect-server) | [connect server create](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-server-create) | add `—-server` flag instead of using an argument for specifying the related server  
[delete connect server](https://developer.1password.com/docs/cli/v1/reference#delete-connect-server) | [connect server delete](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-server-delete) | allows piped input when the `-` argument is provided  
[edit connect server](https://developer.1password.com/docs/cli/v1/reference#edit-connect-server) | [connect server edit](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-server-edit) |   
[list connect servers](https://developer.1password.com/docs/cli/v1/reference#list-connect-servers) | [connect server list](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-server-list) |   
- | [connect server get](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-server-get) |   
[create connect token](https://developer.1password.com/docs/cli/v1/reference#create-connect-token) | [connect token create](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-token-create) |   
[delete connect token](https://developer.1password.com/docs/cli/v1/reference#delete-connect-token) | [connect token delete](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-token-delete) |   
[edit connect token](https://developer.1password.com/docs/cli/v1/reference#edit-connect-token) | [connect token edit](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-token-edit) | argument name changed from `jti` to `token`  
[list connect tokens](https://developer.1password.com/docs/cli/v1/reference#list-connect-tokens) | [connect token list](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-token-list) | ConnectVault.ACL is now displayed in lowercase_with_underscores  
[add connect server](https://developer.1password.com/docs/cli/v1/reference#add-connect-server) | [connect vault grant](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-vault-grant) |  `server` and `vault` arguments changed to `--server` and `--vault` flags  
[remove connect server](https://developer.1password.com/docs/cli/v1/reference#remove-connect-server) | [connect vault revoke](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-vault-revoke) |  `server` and `vault` arguments changed to `--server` and `--vault` flags  
[manage connect add group](https://developer.1password.com/docs/cli/v1/reference#manage-connect-add) | [connect group grant](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-group-grant) |  `server` and `group` arguments changed to `--server` and `--group` flags  
[manage connect remove group](https://developer.1password.com/docs/cli/v1/reference#manage-connect-remove) | [connect group revoke](https://developer.1password.com/docs/cli/reference/management-commands/connect#connect-group-revoke) |  `server` and `group` arguments changed to `--server` and `--group` flags  
[create item](https://developer.1password.com/docs/cli/v1/reference#create-item) | [item create](https://developer.1password.com/docs/cli/reference/management-commands/item#item-create) | 
  * `--template` flag to specify item template file replaces encode item as an argument
  * `category` argument changed to `--category` flag
  * Template JSON format has changed. [Learn more about the new format.](https://developer.1password.com/docs/cli/upgrade/#appendix-json)

  
[delete item](https://developer.1password.com/docs/cli/v1/reference#delete-item) | [item delete](https://developer.1password.com/docs/cli/reference/management-commands/item#item-delete) | allows piped input when the `-` argument is provided  
[edit item](https://developer.1password.com/docs/cli/v1/reference#edit-item) | [item edit](https://developer.1password.com/docs/cli/reference/management-commands/item#item-edit) | new `--tags`, `--title`, `--url` flags  
[get item](https://developer.1password.com/docs/cli/v1/reference#get-item) | [item get](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get) |   
[list items](https://developer.1password.com/docs/cli/v1/reference#list-items) | [item list](https://developer.1password.com/docs/cli/reference/management-commands/item#item-list) |   
[list templates](https://developer.1password.com/docs/cli/v1/reference#list-templates) | [item template list](https://developer.1password.com/docs/cli/reference/management-commands/item#item-template-list) |   
[get template](https://developer.1password.com/docs/cli/v1/reference#get-template) | [item template get](https://developer.1password.com/docs/cli/reference/management-commands/item#item-template-get) |   
[create group](https://developer.1password.com/docs/cli/v1/reference#create-group) | [group create](https://developer.1password.com/docs/cli/reference/management-commands/group#group-create) |   
[delete group](https://developer.1password.com/docs/cli/v1/reference#delete-group) | [group delete](https://developer.1password.com/docs/cli/reference/management-commands/group#group-delete) | allows piped input when the `-` argument is provided  
[edit group](https://developer.1password.com/docs/cli/v1/reference#edit-group) | [group edit](https://developer.1password.com/docs/cli/reference/management-commands/group#group-edit) | allows piped input when the `-` argument is provided  
[list groups](https://developer.1password.com/docs/cli/v1/reference#list-groups) | [group list](https://developer.1password.com/docs/cli/reference/management-commands/group#group-list) |   
[get group](https://developer.1password.com/docs/cli/v1/reference#get-group) | [group get](https://developer.1password.com/docs/cli/reference/management-commands/group#group-get) |   
[add user](https://developer.1password.com/docs/cli/v1/reference#add-user) <user> <group> | [group user grant](https://developer.1password.com/docs/cli/reference/management-commands/group#group-user-grant) |  `user` and `group` arguments changed to `--user` and `--group` flags  
[remove user](https://developer.1password.com/docs/cli/v1/reference#remove-user) <user> <group> | [group user revoke](https://developer.1password.com/docs/cli/reference/management-commands/group#group-user-revoke) |  `user` and `group` args changed to `--user` and `--group` flags  
[op list users --group <group>](https://developer.1password.com/docs/cli/v1/reference#list-users) | [group user list](https://developer.1password.com/docs/cli/reference/management-commands/group#group-user-list) | op list users `--group GROUP` still works  
[delete trash](https://developer.1password.com/docs/cli/v1/reference#delete-trash) | - | deprecated  
[create document](https://developer.1password.com/docs/cli/v1/reference#create-document) | [document create](https://developer.1password.com/docs/cli/reference/management-commands/document#document-create) |  `--filename` flag changed to `--file-name` flag  
[edit document](https://developer.1password.com/docs/cli/v1/reference#edit-document) | [document edit](https://developer.1password.com/docs/cli/reference/management-commands/document#document-edit) |  `--filename` flag changed to `--file-name` flag  
[list documents](https://developer.1password.com/docs/cli/v1/reference#list-documents) | [document list](https://developer.1password.com/docs/cli/reference/management-commands/document#document-list) |   
[get document](https://developer.1password.com/docs/cli/v1/reference#get-document) | [document get](https://developer.1password.com/docs/cli/reference/management-commands/document#document-get) |   
[delete document](https://developer.1password.com/docs/cli/v1/reference#delete-document) | [document delete](https://developer.1password.com/docs/cli/reference/management-commands/document#document-delete) |   
[create integration events-api](https://developer.1password.com/docs/cli/v1/reference#create-integration-events-api) | [events-api create](https://developer.1password.com/docs/cli/reference/management-commands/events-api#events-api-create) |   
[list events](https://developer.1password.com/docs/cli/v1/reference#list-events) | - | Use [1Password Events API](https://developer.1password.com/docs/events-api/) instead.  
[encode](https://developer.1password.com/docs/cli/v1/reference#encode) | - | deprecated, use `create item --template=file.json` instead  
[get totp](https://developer.1password.com/docs/cli/v1/reference#get-totp) | [item get --otp](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get) |   
## Appendix: Change default output to JSON[​](https://developer.1password.com/docs/cli/upgrade/#json-default "Direct link to Appendix: Change default output to JSON")
The default output format for 1Password CLI 2 is a human-readable, tabular schema. You can change the default to machine-readable JSON in two ways:
  * For a single command, include the `--format json` flag with your command. For example, `op item get <name> --format json`.
  * To always default to JSON, set the `$OP_FORMAT` environment variable to `json`.


## Appendix: Item JSON template[​](https://developer.1password.com/docs/cli/upgrade/#appendix-json "Direct link to Appendix: Item JSON template")
You can expect to see several formatting improvements and field name changes in 1Password CLI 2 [item JSON templates](https://developer.1password.com/docs/cli/item-template-json/).
**Old template**
{
"fields": [
{
"designation": "username",
"name": "username",
"type": "T",
"value": ""
},
{
"designation": "password",
"name": "password",
"type": "P",
"value": ""
}
],
"notesPlain": "",
"passwordHistory": [],
"sections": []
}
**New template**
{
"title": "",
"category": "LOGIN",
"fields": [
{
"id": "username",
"type": "STRING",
"purpose": "USERNAME",
"label": "username",
"value": ""
},
{
"id": "password",
"type": "CONCEALED",
"purpose": "PASSWORD",
"label": "password",
"value": ""
},
{
"id": "notesPlain",
"type": "STRING",
"purpose": "NOTES",
"label": "notesPlain",
"value": ""
}
]
}
This is how 1Password CLI 1 template fields correspond to 1Password CLI 2:
**Item**
1Password CLI 1 | 1Password CLI 2 | Notes  
---|---|---  
`uuid` |  |   
`templateUuid` | `category` |   
`details` | - | replaced by `sections` and `fields`  
**Section**
1Password CLI 1 | 1Password CLI 2 | Notes  
---|---|---  
`name` | `id` |   
`title` | `label` |   
`fields` | - | moved separately  
**Field**
1Password CLI 1 | 1Password CLI 2  
---|---  
`n` | `id`  
`k` | `type`  
`t` | `label`  
`v` | `value`  
- | `section`  
## Get help[​](https://developer.1password.com/docs/cli/upgrade/#get-help "Direct link to Get help")
If you need help upgrading to 1Password CLI 2, [Developer Slack workspace](https://developer.1password.com/joinslack) and ask a question in the `#cli` channel.
## Learn more[​](https://developer.1password.com/docs/cli/upgrade/#learn-more "Direct link to Learn more")
  * [Get started with 1Password CLI 2](https://developer.1password.com/docs/cli/get-started/)
  * [1Password CLI 2 release notes](https://releases.1password.com/developers/cli/)


### Was this page helpful?
YesNo
