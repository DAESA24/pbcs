---
title: "Use 1Password Shell Plugins to switch between multiple environments | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/environments/"
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

# Use 1Password Shell Plugins to switch between multiple environments | 1Password Developer

On this page
# Use shell plugins to switch between multiple environments
You can use [1Password Shell Plugins](https://developer.1password.com/docs/cli/shell-plugins/) to seamlessly switch between different sets of credentials for different environments, so you don't have to spend time signing in or out between environments.
For example, you can set the Terraform shell plugin to use your development credentials in the working directory for your development environment and your production credentials in the working directory for your production environment. Then when you run a Terraform command in either directory, the Terraform plugin will automatically authenticate with the appropriate credentials.
## Step 1: Organize your directories by environment[​](https://developer.1password.com/docs/cli/shell-plugins/environments/#step-1-organize-your-directories-by-environment "Direct link to Step 1: Organize your directories by environment")
Before you configure a shell plugin for context switching between environments, group the directories you want to use with the plugin by environment.
For example, if you wanted to use the Terraform shell plugin in both development and production environments, you would organize your directories like this:
projects/
├─ development/
│ ├─ dev-project-1
│ ├─ dev-project-2
├─ production/
│ ├─ prod-project-1
│ ├─ prod-project-2
## Step 2: Configure default credentials for each environment[​](https://developer.1password.com/docs/cli/shell-plugins/environments/#step-2-configure-default-credentials-for-each-environment "Direct link to Step 2: Configure default credentials for each environment")
After you organize your directories by environment, you can set default credentials for your shell plugin to use in each directory and all its subfolders.
  1. Change directories to one of the environment-level folders you created. For example:
cd projects/production
  2. Sign in to the 1Password account where the credentials you want to use are stored:
op signin
  3. Choose a plugin to initialize, or run `op plugin init` to choose from a list of all available plugins. For example, to initialize the Terraform shell plugin:
op plugin init terraform
  4. Import or select the appropriate credentials for the environment.
  5. Select **Use automatically when in this directory or subdirectories** as the default credential scope.
  6. Repeat the process in other environment-level folders with their respective credentials.


This will make the credentials you configure in each environment-level folder the default for all subfolders within it, as long as no other directory-specific defaults are set in them.
## Step 3: Use the plugin in multiple environments[​](https://developer.1password.com/docs/cli/shell-plugins/environments/#step-3-use-the-plugin-in-multiple-environments "Direct link to Step 3: Use the plugin in multiple environments")
After you set default credentials in all your environment-level folders, you can use the shell plugin in the working directories for each environment without needing to sign in or out.
  1. Enter the working directory for an environment. For example, to change directories into the development environment from the example above:
cd ~/projects/development
  2. Run a job in that environment. For example:
terraform apply
  3. Switch to a different environment. For example, to change to the production environment:
cd ~/projects/production
  4. Run a job in that environment:
terraform apply
  5. Exit the environment:
op signout


The shell plugin will automatically authenticate with the appropriate credentials for each environment, without requiring any action on your part.
## Learn more[​](https://developer.1password.com/docs/cli/shell-plugins/environments/#learn-more "Direct link to Learn more")
  * [Get started with 1Password Shell Plugins](https://developer.1password.com/docs/cli/shell-plugins/)
  * [Build your own shell plugins](https://developer.1password.com/docs/cli/shell-plugins/contribute/)


### Was this page helpful?
YesNo
