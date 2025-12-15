---
title: "Use 1Password CLI with multiple accounts | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/use-multiple-accounts/"
captured: 2025-12-15
category: concepts
relevance:
  - secret retrieval
  - environment variables
  - script integration
  - authentication
  - vault management
keywords:
  - op://
  - vault
  - item
  - op read
  - op vault
  - op signin
  - environment variable
related: []
---

# Use 1Password CLI with multiple accounts | 1Password Developer

On this page
# Use multiple 1Password accounts with 1Password CLI
When you [use the 1Password desktop app integration to sign in to 1Password CLI](https://developer.1password.com/docs/cli/app-integration/), you can access any 1Password account you've added to the app on the command line.
By default, all 1Password CLI commands are executed with the account you most recently signed in to, unless an account is specified with the [`--account` flag](https://developer.1password.com/docs/cli/use-multiple-accounts/#specify-an-account-per-command-with-the---account-flag).
## Choose an account to sign in to with `op signin`[​](https://developer.1password.com/docs/cli/use-multiple-accounts/#choose-an-account-to-sign-in-to-with-op-signin "Direct link to choose-an-account-to-sign-in-to-with-op-signin")
To choose an account to sign in to, run [`op signin`](https://developer.1password.com/docs/cli/reference/commands/signin/) and select the account you want to sign in to from the list of accounts added to your 1Password app.
op signin
See result...
Select account [Use arrows to move, type to filter]
> ACME Corp (acme.1password.com)
AgileBits (agilebits.1password.com)
Add another account
If you don't see the account you want to use, you may need to [add it to the 1Password app](https://support.1password.com/add-account/).
## Specify an account per command with the `--account` flag[​](https://developer.1password.com/docs/cli/use-multiple-accounts/#specify-an-account-per-command-with-the---account-flag "Direct link to specify-an-account-per-command-with-the---account-flag")
You can execute a command with a specific account by including the `--account` flag along with the account's [sign-in address (with or without https://) or ID](https://developer.1password.com/docs/cli/use-multiple-accounts/#find-an-account-sign-in-address-or-id).
For example, to get a list of all vaults in an account with the sign-in address `my.1password.com`:
op vault ls --account my.1password.com
You can use the `--account` flag to specify different accounts in scripts. For example:
PASSWORD_1="$(op read --account agilebits-inc.1password.com op://my-vault/some-item/password)"
PASSWORD_2="$(op read --account acme.1password.com op://other-vault/other-item/password)"
## Set an account with the `OP_ACCOUNT` environment variable[​](https://developer.1password.com/docs/cli/use-multiple-accounts/#set-an-account-with-the-op_account-environment-variable "Direct link to set-an-account-with-the-op_account-environment-variable")
If you only want to sign in to a specific account, set the `OP_ACCOUNT` environment variable to the account's [sign-in address or ID](https://developer.1password.com/docs/cli/use-multiple-accounts/#find-an-account-sign-in-address-or-id). You can also use this to specify an account in scripts.
  * Bash, Zsh, sh
  * fish
  * PowerShell


export OP_ACCOUNT=my.1password.com
set -x OP_ACCOUNT my.1password.com
$Env:OP_ACCOUNT = "my.1password.com"
## Find an account sign-in address or ID[​](https://developer.1password.com/docs/cli/use-multiple-accounts/#find-an-account-sign-in-address-or-id "Direct link to Find an account sign-in address or ID")
To find details about all the accounts you've added to the 1Password app, run `op account list`.
op account list
See result...
$ op account list
URL EMAIL USER ID
my.1password.com wendy.c.appleseed@gmail.com JDFU...
agilebits-inc.1password.com wendy_appleseed@agilebits.com ASDU...
You can use the sign-in address listed under `URL` or the unique identifier listed under `USER ID` to refer to the account.
## Learn more[​](https://developer.1password.com/docs/cli/use-multiple-accounts/#learn-more "Direct link to Learn more")
  * [Use the 1Password desktop app to sign in to 1Password CLI](https://developer.1password.com/docs/cli/app-integration/)


### Was this page helpful?
YesNo
