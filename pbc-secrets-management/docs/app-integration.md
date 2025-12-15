---
title: "Use the 1Password desktop app to sign in to 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/app-integration/"
captured: 2025-12-15
category: concepts
relevance:
  - environment variables
  - script integration
  - authentication
  - vault management
  - security patterns
keywords:
  - vault
  - item
  - op vault
  - op signin
  - environment variable
  - biometric
  - authentication
related: []
---

# Use the 1Password desktop app to sign in to 1Password CLI | 1Password Developer

On this page
You can use the [1Password desktop app](https://1password.com/downloads) integration to quickly and securely sign in to [1Password CLI](https://developer.1password.com/docs/cli/get-started/). The app integration allows you to:
  * Seamlessly sign to the 1Password accounts you've added to the app in your terminal.
  * Authenticate 1Password CLI the same way you unlock your device, like with your fingerprint, face, Apple Watch, Windows Hello PIN, or device user password.
  * Track recent 1Password CLI activity from your 1Password app.


## Requirements[​](https://developer.1password.com/docs/cli/app-integration/#requirements "Direct link to Requirements")
  * Mac
  * Windows
  * Linux


  * [1Password subscription](https://1password.com/pricing/password-manager)
  * [1Password for Mac](https://1password.com/downloads/mac)


  * [1Password subscription](https://1password.com/pricing/password-manager)
  * [1Password for Windows](https://1password.com/downloads/windows)


  * [1Password subscription](https://1password.com/pricing/password-manager)
  * [1Password for Linux](https://1password.com/downloads/linux)
  * A PolKit authentication agent running


## Set up the app integration[​](https://developer.1password.com/docs/cli/app-integration/#set-up-the-app-integration "Direct link to Set up the app integration")
### Step 1: Turn on the app integration[​](https://developer.1password.com/docs/cli/app-integration/#step-1-turn-on-the-app-integration "Direct link to Step 1: Turn on the app integration")
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
### Step 2: Enter any command to sign in[​](https://developer.1password.com/docs/cli/app-integration/#step-2-enter-any-command-to-sign-in "Direct link to Step 2: Enter any command to sign in")
After you've turned on the app integration, enter any command and you'll be prompted to authenticate. For example, run this command to see all the vaults in your account:
op vault list
#### If you have multiple accounts[​](https://developer.1password.com/docs/cli/app-integration/#if-you-have-multiple-accounts "Direct link to If you have multiple accounts")
If you've added multiple 1Password accounts to your desktop app, you can use [`op signin`](https://developer.1password.com/docs/cli/reference/commands/signin/) to select an account to sign in to with 1Password CLI. Use the arrow keys to choose from the list of all accounts added to your 1Password app.
op signin
See result...
Select account [Use arrows to move, type to filter]
> ACME Corp (acme.1password.com)
AgileBits (agilebits.1password.com)
Add another account
You can also [select an account on a per-command basis using the `--account` flag](https://developer.1password.com/docs/cli/use-multiple-accounts#specify-an-account-per-command-with-the---account-flag) with your account's sign-in address or ID.
op vault ls --account my.1password.com
If you're signed in to multiple accounts in the app but only want to use a specific account with 1Password CLI, you can [set the `OP_ACCOUNT` environment variable](https://developer.1password.com/docs/cli/use-multiple-accounts#set-an-account-with-the-op_account-environment-variable) to your account's sign-in address or ID.
### Optional: Remove previously added account details[​](https://developer.1password.com/docs/cli/app-integration/#optional-remove-previously-added-account-details "Direct link to Optional: Remove previously added account details")
Make sure you have access to your Secret Key and account password before removing account details from your configuration file.
If you previously [added an account to 1Password CLI manually](https://developer.1password.com/docs/cli/sign-in-manually/) and now want to exclusively use the 1Password app to sign in, you can remove your account details from your configuration file.
Your configuration file is in one of the following locations:
  * `~/.op/config`
  * `~/.config/op/config`
  * `~/.config/.op/config`


Use the [account forget](https://developer.1password.com/docs/cli/reference/management-commands/account#account-forget) command to remove all existing account information from your configuration file. This won't impact the accounts added to your 1Password app.
op account forget --all
### Optional: Set the biometric unlock environment variable[​](https://developer.1password.com/docs/cli/app-integration/#optional-set-the-biometric-unlock-environment-variable "Direct link to Optional: Set the biometric unlock environment variable")
You can use the `OP_BIOMETRIC_UNLOCK_ENABLED` environment variable to temporarily toggle the app integration on or off.
  * Bash, Zsh, sh
  * fish
  * PowerShell


To turn on the integration:
export OP_BIOMETRIC_UNLOCK_ENABLED=true
To turn off the integration:
export OP_BIOMETRIC_UNLOCK_ENABLED=false
To turn on the integration:
set -x OP_BIOMETRIC_UNLOCK_ENABLED true
To turn off the integration:
set -x OP_BIOMETRIC_UNLOCK_ENABLED false
To turn on the integration:
$Env:OP_BIOMETRIC_UNLOCK_ENABLED = "true"
To turn off the integration:
$Env:OP_BIOMETRIC_UNLOCK_ENABLED = "false"
## Track 1Password CLI activity[​](https://developer.1password.com/docs/cli/app-integration/#track-1password-cli-activity "Direct link to Track 1Password CLI activity")
You can track 1Password CLI activity authenticated with the 1Password app, including the command, when it was run, the application where it was run, and the name of the account accessed.
To see your 1Password CLI activity log:
  1. Open and unlock the 1Password desktop app.
  2. Select your account or collection at the top of the sidebar and choose **Settings** >
  3. Turn on **Show 1Password Developer in Sidebar**.
  4. Close the settings window, then select **Developer** in the sidebar.
  5. Select **View CLI**.


![The 1Password CLI activity log.](https://developer.1password.com/img/cli/activity-log-light.png)
You'll see a table with your recent 1Password CLI activity.
Learn more about [1Password Developer](https://support.1password.com/developer/).
## Troubleshooting[​](https://developer.1password.com/docs/cli/app-integration/#troubleshooting "Direct link to Troubleshooting")
### If `op signin` doesn't list your account[​](https://developer.1password.com/docs/cli/app-integration/#if-op-signin-doesnt-list-your-account "Direct link to if-op-signin-doesnt-list-your-account")
`op signin` returns a list of all accounts you've added to the 1Password desktop app. To sign in to 1Password CLI with a new 1Password account, you'll need to [add the account to the app](https://support.1password.com/add-account/).
### If you see a connection error[​](https://developer.1password.com/docs/cli/app-integration/#if-you-see-a-connection-error "Direct link to If you see a connection error")
If you see a `connectionreset` error, or an error that 1Password CLI couldn't connect to the 1Password desktop app, try the following:
  * Mac
  * Windows
  * Linux


Open **System Settings** > **General** > **Login Items** and make sure **Allow in background** is turned on for 1Password.
  

If you still see an error, try the following:
  1. Make sure you're using the latest version of the 1Password desktop app.
  2. Restart the app.


If you're using 1Password for Mac version 8.10.12 or earlier, the 1Password CLI binary must be located in the `/usr/local/bin/` directory.
  1. Make sure you're using the latest version of the 1Password desktop app.
  2. Restart the app.


  1. Make sure you're using the latest version of the 1Password desktop app.
  2. Restart the app.


If you see a `LostConnectionToApp` error when you try to authenticate:
  * Mac
  * Windows
  * Linux


Make sure the option to keep 1Password in the menu bar is turned on:
  1. Open and unlock the 1Password desktop app.
  2. Select your account or collection at the top of the sidebar.
  3. Select **Settings** > **General**.
  4. Make sure "Keep 1Password in the menu bar" is selected.


Make sure the option to keep 1Password in the notification area is turned on:
  1. Open and unlock the 1Password desktop app.
  2. Select your account or collection at the top of the sidebar.
  3. Select **Settings** > **General**.
  4. Make sure "Keep 1Password in the notification area" is selected.


Make sure the option to keep 1Password in the system tray is turned on:
  1. Open and unlock the 1Password desktop app.
  2. Select your account or collection at the top of the sidebar.
  3. Select **Settings** > **General**.
  4. Make sure "Keep 1Password in the system tray" is selected.


### If you aren't prompted to authenticate with your preferred method[​](https://developer.1password.com/docs/cli/app-integration/#if-you-arent-prompted-to-authenticate-with-your-preferred-method "Direct link to If you aren't prompted to authenticate with your preferred method")
If you've turned on the app integration, but aren't prompted to sign in to 1Password CLI with your expected authentication method:
  * Mac
  * Windows
  * Linux


Make sure you've set up [Touch ID](https://support.1password.com/touch-id-mac/) or an [Apple Watch](https://support.1password.com/apple-watch-mac/) to unlock 1Password on your Mac.
Make sure you've set up [Windows Hello](https://support.1password.com/windows-hello/) to unlock 1Password on your Windows PC.
  1. Make sure you've set up [system authentication](https://support.1password.com/system-authentication-linux/) to unlock 1Password on your Linux computer.
  2. Update the authentication method in your Linux settings to use a 


## Learn more[​](https://developer.1password.com/docs/cli/app-integration/#learn-more "Direct link to Learn more")
  * [Use multiple 1Password accounts with 1Password CLI](https://developer.1password.com/docs/cli/use-multiple-accounts/)
  * [Add accounts to the 1Password app](https://support.1password.com/add-account/)
  * [1Password app integration security](https://developer.1password.com/docs/cli/app-integration-security/)


### Was this page helpful?
YesNo
