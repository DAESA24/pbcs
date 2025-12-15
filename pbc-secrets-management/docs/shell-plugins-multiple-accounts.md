---
title: "Use 1Password Shell Plugins to authenticate with multiple accounts | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/multiple-accounts/"
captured: 2025-12-15
category: integrations
relevance:
  - environment variables
  - script integration
  - authentication
keywords:
  - op signin
related: []
---

# Use 1Password Shell Plugins to authenticate with multiple accounts | 1Password Developer

On this page
# Use shell plugins to authenticate with multiple accounts
You can configure [1Password Shell Plugins](https://developer.1password.com/docs/cli/shell-plugins/) to authenticate with different accounts in different directories, so you don't have to spend time signing in or out between projects.
For example, you can set the GitHub shell plugin to authenticate with your work credentials in the directories for your work repositories and your personal credentials in the directories for your personal repositories.
## Step 1: Organize your directories by account[​](https://developer.1password.com/docs/cli/shell-plugins/multiple-accounts/#step-1-organize-your-directories-by-account "Direct link to Step 1: Organize your directories by account")
Before you configure your shell plugins to use multiple accounts, group the project directories on your computer by the accounts they use.
For example, if you have a personal and a work GitHub account, you might organize your personal and work GitHub repository folders like this:
github/
├─ personal/
│ ├─ personal-repo-1
│ ├─ personal-repo-2
│ ├─ personal-repo-3
├─ work/
│ ├─ work-repo-1
│ ├─ work-repo-2
## Step 2: Configure default credentials for each environment[​](https://developer.1password.com/docs/cli/shell-plugins/multiple-accounts/#step-2-configure-default-credentials-for-each-environment "Direct link to Step 2: Configure default credentials for each environment")
After you organize your projects under account-level directories, you can set default credentials for your shell plugin to use in each directory and all its subfolders.
  1. Change directories to one of the account-level folders you created. For example:
cd projects/work
  2. Sign in to the 1Password account where the credentials you want to use are stored:
op signin
  3. Choose a plugin to initialize, or run `op plugin init` to choose from a list of all available plugins. For example, to initialize the GitHub plugin:
op plugin init gh
  4. Import or select the appropriate credentials to use with the account.
  5. Select **Use automatically when in this directory or subdirectories** as the default credential scope.
  6. Repeat the process in other account-level folders with their respective credentials.


This will make the credentials you configure in each account-level folder the default for all subfolders within it, as long as no other directory-specific defaults are set in them.
After you set defaults in all your account-level folders, use the shell plugin as you normally would across all your projects. When you use the plugin in a folder within the personal or work directories, the plugin will automatically authenticate with the appropriate credentials.
## Learn more[​](https://developer.1password.com/docs/cli/shell-plugins/multiple-accounts/#learn-more "Direct link to Learn more")
  * [Get started with 1Password Shell Plugins](https://developer.1password.com/docs/cli/shell-plugins/)
  * [Build your own shell plugins](https://developer.1password.com/docs/cli/shell-plugins/contribute/)


### Was this page helpful?
YesNo
