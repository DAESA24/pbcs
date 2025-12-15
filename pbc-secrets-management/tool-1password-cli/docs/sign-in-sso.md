---
title: "Unlock 1Password CLI with SSO | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/sign-in-sso/"
captured: 2025-12-15
category: concepts
relevance:
  - environment variables
  - script integration
  - authentication
  - vault management
keywords:
  - op signin
  - environment variable
  - biometric
  - authentication
related: []
---

# Unlock 1Password CLI with SSO | 1Password Developer

On this page
This feature is only available as part of [1Password Unlock with SSO](https://support.1password.com/sso/).
If your 1Password administrator has [set up 1Password Unlock with SSO](https://support.1password.com/sso/), you can sign in to 1Password CLI with your identity provider.
If the 1Password account you sign in to with SSO doesn't allow biometric unlock, you'll be prompted to allow 1Password CLI access to the 1Password app when you sign in.
## Requirements[​](https://developer.1password.com/docs/cli/sign-in-sso/#requirements "Direct link to Requirements")
Before you start, you'll need to:
  1. [Join your team](https://support.1password.com/sso-get-started#join-your-team), or [switch to unlock with SSO](https://support.1password.com/sso-get-started#switch-to-unlock-with-sso).
  2. Install the latest version of 1Password for [Mac](https://1password.com/downloads/mac), [Windows](https://1password.com/downloads/windows), or [Linux](https://1password.com/downloads/linux).
  3. Sign in to 1Password for [Mac](https://support.1password.com/sso-sign-in#in-the-apps/), [Windows](https://support.1password.com/sso-sign-in#in-the-apps/), or [Linux](https://support.1password.com/sso-sign-in#in-the-apps/) using SSO.
  4. Install [the latest Password CLI build](https://developer.1password.com/docs/cli/get-started/).


## Step 1: Connect 1Password CLI with the 1Password app[​](https://developer.1password.com/docs/cli/sign-in-sso/#step-1-connect-1password-cli-with-the-1password-app "Direct link to Step 1: Connect 1Password CLI with the 1Password app")
To turn on the app integration and set up 1Password CLI to authenticate with your identity provider:
  * Mac
  * Windows
  * Linux


  1. Open and unlock the [1Password app](https://1password.com/downloads/).
  2. Select your account or collection at the top of the sidebar.
  3. Navigate to **Settings** >
  4. Select **Integrate with 1Password CLI**.
  5. If you want to authenticate 1Password CLI with your fingerprint, turn on **[Touch ID](https://support.1password.com/touch-id-mac/)** in the app.


![The 1Password Developer settings pane with the Integrate with 1Password CLI option selected.](https://developer.1password.com/img/cli/developer-settings-light.png)
  1. Open and unlock the [1Password app](https://1password.com/downloads/).
  2. Select your account or collection at the top of the sidebar.
  3. Turn on **[Windows Hello](https://support.1password.com/windows-hello/)** in the app.
  4. Navigate to **Settings** >
  5. Select **Integrate with 1Password CLI**.


![The 1Password Developer settings pane with the Integrate with 1Password CLI option selected.](https://developer.1password.com/img/cli/developer-settings-windows-light.png)
  1. Open and unlock the [1Password app](https://1password.com/downloads/).
  2. Select your account or collection at the top of the sidebar.
  3. Navigate to **Settings** >
  4. Turn on **[Unlock using system authentication](https://support.1password.com/system-authentication-linux/)**.
  5. Navigate to **Settings** >
  6. Select **Integrate with 1Password CLI**.


![The 1Password Developer settings pane with the Integrate with 1Password CLI option selected.](https://developer.1password.com/img/cli/developer-settings-linux.png)
## Step 2: Sign in with SSO[​](https://developer.1password.com/docs/cli/sign-in-sso/#step-2-sign-in-with-sso "Direct link to Step 2: Sign in with SSO")
Once the 1Password app integration is turned on, open the terminal and type [`op signin`](https://developer.1password.com/docs/cli/get-started#step-3-enter-any-command-to-sign-in). Use the arrow keys to select your SSO-enabled account from the list of all accounts added to your 1Password app. 1Password CLI will prompt you to authenticate.
op signin
Select account [Use arrows to move, type to filter]
> ACME Corp (acme.1password.com)
AgileBits (agilebits.1password.com)
Add another account
After you sign in for the first time, 1Password CLI will automatically sign in to your most recently used account.
If you want to [sign in to a different account](https://developer.1password.com/docs/cli/use-multiple-accounts/), you can use the `--account` flag or an environment variable.
## Get help[​](https://developer.1password.com/docs/cli/sign-in-sso/#get-help "Direct link to Get help")
If the 1Password account you sign in to with SSO doesn't allow biometric unlock, you'll be prompted to allow 1Password CLI access to the 1Password app when you sign in.
## Learn more[​](https://developer.1password.com/docs/cli/sign-in-sso/#learn-more "Direct link to Learn more")
  * [Set up 1Password Unlock with SSO](https://support.1password.com/sso/)
  * [Get started with 1Password Unlock with SSO](https://support.1password.com/sso-get-started/)
  * [Sign in to 1Password with SSO](https://support.1password.com/sso-sign-in/)
  * [Link new apps and browsers to unlock with SSO](https://support.1password.com/sso-linked-apps-browsers/)
  * [If you're having trouble unlocking 1Password with SSO](https://support.1password.com/sso-troubleshooting/)


### Was this page helpful?
YesNo
