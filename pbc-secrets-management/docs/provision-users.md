---
title: "Add and remove team members with 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/provision-users/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - authentication
  - vault management
keywords:
  - vault
  - item
related: []
---

# Add and remove team members with 1Password CLI | 1Password Developer

On this page
# Add and remove team members
## Requirements[​](https://developer.1password.com/docs/cli/provision-users/#requirements "Direct link to Requirements")
Before you can use 1Password CLI to add and remove team members, you'll need to:
  1. [Sign up for 1Password Business](https://1password.com/pricing/password-manager).
  2. [Install 1Password CLI](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli).


## Turn on automated provisioning with 1Password CLI[​](https://developer.1password.com/docs/cli/provision-users/#turn-on-automated-provisioning-with-1password-cli "Direct link to Turn on automated provisioning with 1Password CLI")
To get started, an owner or administrator must visit the [Provisioning settings page on 1Password.com](https://start.1password.com/settings/provisioning/cli) and select **Turn On CLI Provisioning**. This will create a [Provision Managers](https://support.1password.com/groups#provision-managers) group with the permissions needed to provision and confirm team members, as well as recover accounts. The person who created the group will be added to it.
## Manage who can provision team members[​](https://developer.1password.com/docs/cli/provision-users/#manage-who-can-provision-team-members "Direct link to Manage who can provision team members")
By default, the owner or administrator who created the [Provision Managers](https://support.1password.com/groups#provision-managers) group is the only person added to it. If other team members need to be able to provision users, use [`op group user grant`](https://developer.1password.com/docs/cli/reference/management-commands/group#group-user-grant) to add them to the group.
For example, to add Wendy Appleseed to the Provision Managers group:
op group user grant --group "Provision Managers" --user "wendy.appleseed@agilebits.com"
To see a list of everyone in the Provision Managers group:
op group user list "Provision Managers"
## Add team members[​](https://developer.1password.com/docs/cli/provision-users/#add-team-members "Direct link to Add team members")
To invite people to your team, use [`op user provision`](https://developer.1password.com/docs/cli/reference/management-commands/user#user-provision) with the team member's name and email address.
For example, to invite Wendy Appleseed to join your 1Password account:
op user provision --name "Wendy Appleseed" --email "wendy.appleseed@agilebits.com"
The person will receive an email invitation to join the team. After they've accepted the invitation, a member of the Provision Managers group can confirm them.
## Confirm team members[​](https://developer.1password.com/docs/cli/provision-users/#confirm-team-members "Direct link to Confirm team members")
Anyone who belongs to the [Provision Managers](https://support.1password.com/groups#provision-managers) group can confirm new team members with [`op user confirm`](https://developer.1password.com/docs/cli/provision-users/#with-op-user-confirm) or [on 1Password.com](https://developer.1password.com/docs/cli/provision-users/#on-1passwordcom).
### With `op user confirm`[​](https://developer.1password.com/docs/cli/provision-users/#with-op-user-confirm "Direct link to with-op-user-confirm")
To confirm a team member on the command line, use [`op user confirm`](https://developer.1password.com/docs/cli/reference/management-commands/user#user-confirm) with their name or email address. To confirm all unconfirmed team members, include the `--all` flag.
For example, to confirm Wendy Appleseed:
op user confirm "wendy.appleseed@agilebits.com"
To confirm all pending users:
op user confirm --all
### On 1Password.com[​](https://developer.1password.com/docs/cli/provision-users/#on-1passwordcom "Direct link to On 1Password.com")
To confirm a team member on 1Password.com:
  1. [Sign in](https://start.1password.com/signin) to your account on 1Password.com.
  2. Select **[People](https://start.1password.com/people)** in the sidebar.
  3. Select the name of any team member with the Pending Provision status.
  4. Select **Confirm** or **Reject**.


If you don't see the option to confirm or reject a team member, ask your administrator to [add you to the Provision Managers group](https://developer.1password.com/docs/cli/provision-users/#manage-who-can-provision-team-members).
## Remove team members[​](https://developer.1password.com/docs/cli/provision-users/#remove-team-members "Direct link to Remove team members")
To remove someone's access to vaults and items, you can suspend or delete their account.
### Suspend an account temporarily[​](https://developer.1password.com/docs/cli/provision-users/#suspend-an-account-temporarily "Direct link to Suspend an account temporarily")
Use [`op user suspend`](https://developer.1password.com/docs/cli/reference/management-commands/user#user-suspend) to suspend a team member temporarily.
Include the `--deauthorize-devices-after` flag, followed by the number of seconds, minutes, or hours (for example, `600s`, `10m`, or `1h`) to set the time after suspension to deauthorize the suspended team member's devices. The maximum time permitted is 24 hours. If unspecified, their devices will be deauthorized immediately.
For example, to suspend Wendy Appleseed temporarily and deauthorize her devices after 10 minutes:
op user suspend "wendy.appleseed@agilebits.com --deauthorize-devices-after 10m"
You can reactivate a suspended user with [`op user reactivate`](https://developer.1password.com/docs/cli/reference/management-commands/user#user-reactivate).
### Remove an account permanently[​](https://developer.1password.com/docs/cli/provision-users/#remove-an-account-permanently "Direct link to Remove an account permanently")
Use [`op user delete`](https://developer.1password.com/docs/cli/reference/management-commands/user#user-delete) to permanently remove a team member's access to vaults and items and delete all of their data from the account.
For example, to remove Wendy Appleseed:
op user delete "wendy.appleseed@agilebits.com"
## Learn more[​](https://developer.1password.com/docs/cli/provision-users/#learn-more "Direct link to Learn more")
  * [Add and remove team members on 1Password.com](https://support.1password.com/add-remove-team-members/)
  * [Automate provisioning in 1Password Business using SCIM](https://support.1password.com/scim/)


### Was this page helpful?
YesNo
