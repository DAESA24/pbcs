---
title: "Uninstall 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/uninstall/"
captured: 2025-12-15
category: concepts
relevance:
  - vault management
keywords:
  - item
related: []
---

# Uninstall 1Password CLI | 1Password Developer

On this page
Make sure you have access to your Secret Key and account password before removing 1Password account information from your device.
## Step 1: Remove your 1Password account information[​](https://developer.1password.com/docs/cli/uninstall/#step-1-remove-your-1password-account-information "Direct link to Step 1: Remove your 1Password account information")
Your 1Password CLI configuration file contains account details for accounts you've signed in to on the command line using your account password and Secret Key. It does not contain information for accounts you've signed in to using the 1Password desktop app integration.
Your config file can be found in one of the following locations: `~/.op/config`, `~/.config/op/config`, or `~/.config/.op/config`.
To remove all account information from your config file:
op account forget --all
## Step 2: Uninstall 1Password CLI[​](https://developer.1password.com/docs/cli/uninstall/#step-2-uninstall-1password-cli "Direct link to Step 2: Uninstall 1Password CLI")
  * Mac
  * Windows
  * Linux


  * homebrew
  * Manual


To uninstall 1Password CLI with homebrew:
brew uninstall 1password-cli
To manually uninstall 1Password CLI, run:
rm /usr/local/bin/op
  * Scoop
  * winget
  * Manual


To uninstall 1Password CLI with Scoop:
scoop uninstall 1password-cli
To uninstall 1Password CLI with winget:
winget uninstall 1password-cli
To uninstall 1Password CLI on a Windows PC:
  1. Open Powershell **as an administrator**.
  2. Run the following command:


Remove-Item -Recurse -Force "C:\Program Files\1Password CLI"
To uninstall 1Password CLI on Linux, run:
rm /usr/local/bin/op
The 1Password CLI directory and all of its contents will be deleted.
### Was this page helpful?
YesNo
