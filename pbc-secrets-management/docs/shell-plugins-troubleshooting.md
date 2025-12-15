---
title: "1Password Shell Plugins troubleshooting | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/"
captured: 2025-12-15
category: integrations
relevance:
  - environment variables
  - script integration
  - authentication
keywords:
  - authentication
related: []
---

# 1Password Shell Plugins troubleshooting | 1Password Developer

On this page
## Using shell plugins[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#using-shell-plugins "Direct link to Using shell plugins")
### If you're using a non-interactive shell[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#if-youre-using-a-non-interactive-shell "Direct link to If you're using a non-interactive shell")
1Password Shell Plugins are built to be used with interactive shells. An interactive shell is required for the shell plugin to prompt for authentication.
### If your script doesn't inherit shell plugin aliases[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#if-your-script-doesnt-inherit-shell-plugin-aliases "Direct link to If your script doesn't inherit shell plugin aliases")
Scripts might not inherit your shell plugin aliases if they're run in a subshell where the `plugins.sh` file isn't sourced. When this happens, the CLI command in the script will output an error instead of running correctly.
For example, the following script runs a `doctl` command in a subshell, and as a result wouldn't inherit the `doctl` shell plugin alias:
yourscript.sh
#!/usr/bin/env bash
  

doctl account get
To make the script run correctly, you can wrap the `doctl` command in [`op plugin run`](https://developer.1password.com/docs/cli/reference/management-commands/plugin#plugin-run). For example:
yourscript.sh
#!/usr/bin/env bash
  

op plugin run doctl account get
### If autocompletion stops working[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#if-autocompletion-stops-working "Direct link to If autocompletion stops working")
If autocompletion stops working in Zsh after you configure a shell plugin, run the following command to configure completion for aliases:
setopt completealiases
## Contributing shell plugins[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#contributing-shell-plugins "Direct link to Contributing shell plugins")
### If your locally-built plugin stops working[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#if-your-locally-built-plugin-stops-working "Direct link to If your locally-built plugin stops working")
If your locally-built plugin stops working, you might need to update your 1Password CLI version or rebuild your plugin with the latest shell plugins SDK.
#### Update your 1Password CLI installation[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#update-your-1password-cli-installation "Direct link to Update your 1Password CLI installation")
If you're using an outdated version of the CLI, you'll see this error message:
1Password CLI is outdated, please run:
  

op update
  

to update 1Password CLI to the latest version and to be able to use
this Shell Plugin.
To update your 1Password CLI installation to the latest version:
op update
Or [update 1Password CLI with a package manager](https://developer.1password.com/docs/cli/reference/update#update-with-a-package-manager).
#### Rebuild your plugins with the latest shell plugins SDK[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#rebuild-your-plugins-with-the-latest-shell-plugins-sdk "Direct link to Rebuild your plugins with the latest shell plugins SDK")
If the shell plugins SDK is outdated, you'll see this error message:
1Password Shell Plugin is out of date. Remove the plugin at
'/Users/<user>/.op/plugins/local/aws' or rebuild it with the
latest Shell Plugin SDK to use it.
To update to the latest shell plugins SDK, you'll need to merge the `main` branch of the 
  1. Navigate to the directory where you cloned the shell plugins repo:
cd <path/to/shell-plugins/repo>
  2. If you've made any local changes to your plugin branch, commit or stash them:
git commit -am "<commit message>"
  3. Check out the `main` branch:
git checkout main
  4. Pull the `main` branch:
git pull main
  5. Check out your plugin branch:
git checkout <your-plugin-branch>
  6. Merge `main` into your branch:
git merge main


Then fix any merge conflicts and make any needed changes to the plugin code to conform to the latest version of the SDK.
When you're ready to rebuild your plugin:
make <your-plugin>/build
If you're still having trouble, join our [Developer Slack workspace](https://developer.1password.com/joinslack) and we'll help you figure out a solution.
## Learn more[​](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/#learn-more "Direct link to Learn more")
  * [Uninstall shell plugins](https://developer.1password.com/docs/cli/shell-plugins/uninstall/)
  * [Test shell plugins](https://developer.1password.com/docs/cli/shell-plugins/test/)
  * [Use shell plugins to switch between multiple environments](https://developer.1password.com/docs/cli/shell-plugins/environments/)
  * [Use shell plugins with multiple accounts](https://developer.1password.com/docs/cli/shell-plugins/multiple-accounts/)


### Was this page helpful?
YesNo
