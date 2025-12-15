---
title: "Sign in to your 1Password account manually | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/sign-in-manually/"
captured: 2025-12-15
category: concepts
relevance:
  - environment variables
  - script integration
  - authentication
  - vault management
keywords:
  - vault
  - op vault
  - op signin
  - environment variable
  - service account
  - session
related: []
---

# Sign in to your 1Password account manually | 1Password Developer

On this page
If you don't want to [use the 1Password app to sign in to 1Password CLI](https://developer.1password.com/docs/cli/get-started#step-2-turn-on-the-1password-desktop-app-integration), you can manually add and sign in to your accounts in the terminal.
If you sign in to 1Password CLI manually, any process running under the current user can, on some platforms, potentially access your 1Password account.
We recommend you [use the 1Password app to sign in to 1Password CLI](https://developer.1password.com/docs/cli/app-integration/) because it offers more robust security guarantees.
When you sign in manually in the terminal, 1Password CLI stores your session key encrypted on disk and the random wrapper key used in the environment of the current shell.
Sessions expire after 30 minutes of inactivity, after which you’ll need to sign in again and save a new token. If you want to immediately terminate your authenticated session, you can run `op signout`.
## Sign in manually[​](https://developer.1password.com/docs/cli/sign-in-manually/#sign-in-manually "Direct link to Sign in manually")
### Step 1: Add an account[​](https://developer.1password.com/docs/cli/sign-in-manually/#step-1-add-an-account "Direct link to Step 1: Add an account")
To manually add a 1Password account to 1Password CLI, use [`op account add`](https://developer.1password.com/docs/cli/reference/management-commands/account/):
op account add
1Password CLI will prompt you to enter your [sign-in address](https://support.1password.com/sign-in-troubleshooting#if-youre-asked-for-a-sign-in-address), email address, [Secret Key](https://support.1password.com/secret-key/), and 1Password account password.
For non-interactive shells in local environments, sign in with the [1Password desktop app integration](https://developer.1password.com/docs/cli/app-integration/) instead.
For non-interactive shells in remote environments, authenticate with a [service account](https://developer.1password.com/docs/service-accounts/) or a [Connect server](https://developer.1password.com/docs/connect/).
#### Set a custom account shorthand[​](https://developer.1password.com/docs/cli/sign-in-manually/#set-a-custom-account-shorthand "Direct link to Set a custom account shorthand")
1Password CLI uses account shorthands to refer to each of the accounts you add. The default shorthand is your [sign-in address](https://support.1password.com/sign-in-troubleshooting#if-youre-asked-for-a-sign-in-address) subdomain (for example, `my` for `my.1password.com`).
To set a custom shorthand, include the `--shorthand` flag when you add an account. For example, to add an account with the shorthand `personal`:
op account add --shorthand personal
### Step 2: Sign in[​](https://developer.1password.com/docs/cli/sign-in-manually/#step-2-sign-in "Direct link to Step 2: Sign in")
If you added your accounts to 1Password CLI manually, you'll need to use the [manual sign-in command](https://developer.1password.com/docs/cli/reference/commands/signin/) to sign in.
This command also works with the [app integration](https://developer.1password.com/docs/cli/app-integration) turned on, so you can use it in scripts to provide compatibility for all users regardless of their sign-in method.
  * Bash, Zsh, sh, fish
  * PowerShell


eval "$(op signin)"
Invoke-Expression "$(op signin)"
After you sign in, 1Password CLI creates a session token and sets the `OP_SESSION` environment variable to it. Include the `--raw` flag to get a token you can export manually.
Session tokens expire after 30 minutes of inactivity, after which you’ll need to sign in again and save a new token.
To sign out, use the command [`op signout`](https://developer.1password.com/docs/cli/reference/commands/signout/).
### Optional: Switch between accounts with the `--account` flag[​](https://developer.1password.com/docs/cli/sign-in-manually/#optional-switch-between-accounts-with-the---account-flag "Direct link to optional-switch-between-accounts-with-the---account-flag")
If you've added multiple accounts and are using an interactive terminal, 1Password CLI will prompt you to select the account you want to sign in to. Use the arrow keys to select an account, then press the `Return` key to sign in.
In most shells, you can bypass the prompt to select an account using the `--account` flag with your [account shorthand, sign-in address, or ID](https://developer.1password.com/docs/cli/sign-in-manually/#appendix-find-an-account-shorthand-or-id). This option isn't available in PowerShell. For example:
  * Bash, Zsh, sh, fish


eval "$(op signin --account personal)"
To always sign in to the same account, set the `OP_ACCOUNT` environment variable to your [account shorthand, sign-in address, or ID](https://developer.1password.com/docs/cli/sign-in-manually/#appendix-find-an-account-shorthand-or-id).
  * Bash, Zsh, sh
  * fish
  * PowerShell


export OP_ACCOUNT=my.1password.com
set -x OP_ACCOUNT my.1password.com
$Env:OP_ACCOUNT = "my.1password.com"
You can sign in to multiple accounts at the same time, then use the `--account` flag to specify which account should execute each command. If you don't specify an account, 1Password CLI will default to the account you most recently signed in to.
For example, to sign in to accounts with the shorthands `personal` and `agilebits`:
  * Bash, Zsh, sh, fish
  * PowerShell


eval "$(op signin --account personal)" && eval "$(op signin --account agilebits)"
Invoke-Expression "$(op signin --account personal)"; Invoke-Expression "$(op signin --account agilebits)"
To run the command `op vault list` in the account with the shorthand `personal`:
op vault list --account personal
Then to run the same command in the `agilebits` account:
op vault list --account agilebits
You can also [specify a custom shorthand](https://developer.1password.com/docs/cli/sign-in-manually/#set-a-custom-account-shorthand) when you add an account.
## Troubleshooting[​](https://developer.1password.com/docs/cli/sign-in-manually/#troubleshooting "Direct link to Troubleshooting")
If you've already [turned on the 1Password app integration](https://developer.1password.com/docs/cli/get-started#step-2-turn-on-the-1password-desktop-app-integration), you'll need to turn it off before you can add an account on the command line.
## Learn more[​](https://developer.1password.com/docs/cli/sign-in-manually/#learn-more "Direct link to Learn more")
  * [Integrate 1Password CLI with the 1Password desktop app](https://developer.1password.com/docs/cli/app-integration/)
  * [About the security of the 1Password desktop app integration](https://developer.1password.com/docs/cli/app-integration-security/)


## Appendix: Find an account shorthand or ID[​](https://developer.1password.com/docs/cli/sign-in-manually/#appendix-find-an-account-shorthand-or-id "Direct link to Appendix: Find an account shorthand or ID")
1Password CLI uses account shorthands to refer to each of the accounts you've added. To see all the accounts you've added, their shorthands, and account details, run `op account list`.
op account list
See result...
SHORTHAND URL EMAIL USER UUID
my https://my.1password.com wendy.c.appleseed@gmail.com A10S...
agilebits https://agilebits-inc.1password.com wendy_appleseed@agilebits.com ONJ9...
You can use the shorthand, sign-in address, or user ID to refer to a specific account in your commands.
### Was this page helpful?
YesNo
