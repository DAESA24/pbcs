---
title: "Uninstall shell plugins | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/uninstall/"
captured: 2025-12-15
category: integrations
relevance:
  - authentication
  - ssh keys
keywords:
  - authentication
  - session
  - ssh
related: []
---

# Uninstall shell plugins | 1Password Developer

On this page
[1Password Shell Plugins](https://developer.1password.com/docs/cli/shell-plugins/) are built so you can stop using them at any time.
  * If you want to [reset a shell plugin configuration](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#clear-your-default-credentials-for-a-plugin), you can clear your default credentials.
  * If you want to [temporarily stop using a shell plugin](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#temporarily-stop-using-a-shell-plugin), you can run `unalias <plugin-executable>` or remove the alias for its executable from your `plugins.sh` file.
  * If you want to [temporarily stop using all shell plugins](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#temporarily-stop-using-all-shell-plugins), you can remove the command to source the `plugins.sh` file from your shell profile.
  * And if you want to [completely uninstall shell plugins](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#completely-stop-using-shell-plugins), you can do that too.


## Clear your default credentials for a plugin[​](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#clear-your-default-credentials-for-a-plugin "Direct link to Clear your default credentials for a plugin")
If you want to remove your default credentials for a shell plugin:
op plugin clear <plugin-executable>
Credentials will be removed in this order:
  1. Terminal session default
  2. Directory default, from the current directory to `$HOME`
  3. Global default


To remove all the credentials you've configured for a shell plugin at the same time:
op plugin clear <plugin-executable> --all
## Temporarily stop using a shell plugin[​](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#temporarily-stop-using-a-shell-plugin "Direct link to Temporarily stop using a shell plugin")
If you want to stop using a shell plugin for the current terminal session, run:
unalias <plugin-executable>
If you want to temporarily stop using a plugin for a longer period of time, you can remove its alias from your `plugins.sh` file. Then 1Password CLI will no longer handle authentication when you use the third-party CLI.
  1. Open your [`plugins.sh` file](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#if-you-cant-find-your-pluginssh-file) file.
  2. Remove the alias for the plugin you want to stop using. For example, `alias aws="op plugin run -- aws"`.
  3. Save the file.
  4. Open a new terminal window or source your shell profile for the change to go into effect.


You can add the alias back to the file at any time to continue using the shell plugin with your current setup.
## Temporarily stop using all shell plugins[​](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#temporarily-stop-using-all-shell-plugins "Direct link to Temporarily stop using all shell plugins")
If you want to temporarily stop using shell plugins without losing your configurations, you can remove the command to source the `plugins.sh` file from your shell profile.
  1. Open your shell profile.
  2. Remove the line that looks like this. Your [`plugins.sh` file path](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#if-you-cant-find-your-pluginssh-file) may vary.
source ~/.config/op/plugins.sh
  3. Open a new terminal session or source your shell profile for the change to go into effect.


1Password will no longer prompt you to authenticate for any third-party CLI.
## Completely stop using shell plugins[​](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#completely-stop-using-shell-plugins "Direct link to Completely stop using shell plugins")
To completely stop using shell plugins and remove all information about your configurations:
  1. [Clear the default credentials](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#clear-your-default-credentials-for-a-plugin) for each of your plugins.
  2. [Remove the command to source the `plugins.sh` file](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#temporarily-stop-using-all-shell-plugins) from your shell profile.
  3. Delete the [`plugins.sh` file](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#if-you-cant-find-your-pluginssh-file) and the `plugins` folder within your `op` directory.
  4. If you configured any directory-specific defaults, remove the `.op` folder from those directories.


## Get help[​](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#get-help "Direct link to Get help")
### If you can't find your plugins.sh file[​](https://developer.1password.com/docs/cli/shell-plugins/uninstall/#if-you-cant-find-your-pluginssh-file "Direct link to If you can't find your plugins.sh file")
The file path for your `plugins.sh` file may vary depending on your [configuration directory](https://developer.1password.com/docs/cli/config-directories/). Common locations include:
  * `~/.op/plugins.sh`
  * `~/.config/op/plugins.sh`
  * `~/op/plugins.sh`


### Was this page helpful?
YesNo
