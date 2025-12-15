---
title: "Test shell plugins | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/test/"
captured: 2025-12-15
category: integrations
relevance:
  - script integration
  - authentication
keywords:
  - op signin
  - authentication
  - session
related: []
---

# Test shell plugins | 1Password Developer

On this page
You can test [1Password Shell Plugins](https://developer.1password.com/docs/cli/shell-plugins/) without making any changes to your current workflows.
To do this, you'll configure a shell plugin with default credentials that only last for the duration of your current terminal session, then source the shell plugin aliases script in your current terminal session instead of adding it to your shell profile. When you close your terminal window, your temporary shell plugin configuration will be cleared.
## Step 1: Temporarily configure a shell plugin[​](https://developer.1password.com/docs/cli/shell-plugins/test/#step-1-temporarily-configure-a-shell-plugin "Direct link to Step 1: Temporarily configure a shell plugin")
  1. Sign in to the 1Password account where the credentials you want to use with the shell plugin are stored:
op signin
  2. Choose a plugin to test, or run `op plugin init` to choose from a list of all available plugins. For example, to test the AWS shell plugin:
op plugin init aws
  3. Import or select the credentials you want to test with the plugin.
  4. When you're prompted to choose when the credentials will be used to authenticate, select **Prompt me for each new terminal session**. This will configure your credentials as a temporary default for the duration of your current terminal session.
  5. Instead of adding the command to source the `plugins.sh` file to your shell profile, source the `plugins.sh` file in your current terminal session. This will create an alias for the CLI executable that lasts for the duration of your current terminal session. For example:
source ~/.config/op/plugins.sh
The location of the `plugins.sh` file will vary depending on your [configuration directory](https://developer.1password.com/docs/cli/config-directories/).


## Step 2: Test the shell plugin[​](https://developer.1password.com/docs/cli/shell-plugins/test/#step-2-test-the-shell-plugin "Direct link to Step 2: Test the shell plugin")
You can test the shell plugin for the duration of your current terminal session.
  1. Sign out of 1Password CLI to make sure you'll be prompted to authenticate:
op signout
  2. Run a command with the CLI that requires authentication. For example, if you configured a shell plugin for AWS:
aws s3 ls


When you're done testing, close the terminal window to clear your default credentials and remove the alias for the CLI executable.
To continue using a shell plugin, follow the installation guide for the [plugin of your choice](https://developer.1password.com/docs/cli/shell-plugins/).
### Was this page helpful?
YesNo
