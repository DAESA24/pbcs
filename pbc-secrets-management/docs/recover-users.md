---
title: "Recover accounts using 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/recover-users/"
captured: 2025-12-15
category: concepts
relevance:
  - authentication
  - vault management
keywords:
  - vault
  - authentication
related: []
---

# Recover accounts using 1Password CLI | 1Password Developer

On this page
You can use 1Password CLI to begin the account recovery process for a family or team member if they can't sign in to or unlock 1Password. When you recover an account for someone:
  * They'll receive a new Secret Key and create a new 1Password account password.  
If your team uses Unlock with SSO, they'll be able to [link a new app or browser to their account](https://support.1password.com/sso-linked-apps-browsers/) again.
  * They'll be able to access all the data they had before.
  * They'll need to sign in again on all their devices once recovery is complete.
  * Their two-factor authentication will be reset.


## Requirements[​](https://developer.1password.com/docs/cli/recover-users/#requirements "Direct link to Requirements")
  * [Sign up for 1Password](https://1password.com/pricing/password-manager).
  * [Install 1Password CLI](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli) version `2.32.0` or later.


You can recover accounts for other people if:
  * You're a team [administrator](https://support.1password.com/groups#administrators) or [owner](https://support.1password.com/groups#owners).
  * You belong to a [custom group](https://support.1password.com/custom-groups/) that has the "Recover Accounts" permission.
  * You're a [family organizer](https://support.1password.com/family-organizer/).


## Begin recovery[​](https://developer.1password.com/docs/cli/recover-users/#begin-recovery "Direct link to Begin recovery")
Use the command `op user recovery begin` with a person's name, email address, or [unique identifier (ID)](https://developer.1password.com/docs/cli/reference#unique-identifiers-ids) to begin the account recovery process. You can recover up to ten accounts with each command.
op user recovery begin { <email> | <name> | <userID> }
For example, to begin recovery for multiple accounts using each person's ID:
op user recovery begin ZMAE4RTRONHN7LGELNYYO373KM WHPOFIMMYFFITBVTOTZUR3R324 FGH76DFS89FYCU6342CSDWIFJU
The person whose account you're recovering will get an email from 1Password. When they select **Recover my account** in the email, a page will open in their browser and they'll be asked to confirm their email address. Then they'll get a new Secret Key and create a new account password.
## Complete recovery[​](https://developer.1password.com/docs/cli/recover-users/#complete-recovery "Direct link to Complete recovery")
After the person whose account you recovered creates a new account password, you'll need to complete the recovery process before they can access their account.
Learn how to [complete account recovery for one or more people](https://support.1password.com/recovery#complete-recovery).
## Learn more[​](https://developer.1password.com/docs/cli/recover-users/#learn-more "Direct link to Learn more")
  * [Add and remove team members](https://developer.1password.com/docs/cli/provision-users)
  * [Grant and revoke vault permissions](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions)
  * [Sign back in to 1Password after your account has been recovered](https://support.1password.com/after-recovery/)


### Was this page helpful?
YesNo
