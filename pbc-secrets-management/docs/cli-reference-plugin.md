---
title: "plugin | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/plugin/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - authentication
  - security patterns
keywords:
  - item
  - field
  - authentication
  - session
related: []
---

# plugin | 1Password CLI | 1Password Developer

On this page
# plugin
Manage your shell plugin configurations.
You can use shell plugins to securely authenticate third-party CLIs with 1Password, rather than storing your CLI credentials in plaintext. After you configure a plugin, 1Password CLI will prompt you to authenticate the third-party CLI with your fingerprint or other system authentication option.
[Learn more about shell plugins.](https://developer.1password.com/docs/cli/shell-plugins)
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#subcommands "Direct link to Subcommands")
  * [plugin clear](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-clear): Clear shell plugin configuration
  * [plugin init](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-init): Configure a shell plugin
  * [plugin inspect](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-inspect): Inspect your existing shell plugin configurations
  * [plugin list](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-list): List all available shell plugins
  * [plugin run](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-run): Provision credentials from 1Password and run this command


## plugin clear[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-clear "Direct link to plugin clear")
Clear an existing shell plugin configuration.
op plugin clear <plugin-executable> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-clear-flags "Direct link to Flags")
--all Clear all configurations for this plugin that apply to this directory
and/or terminal session, including the global default.
-f, --force Apply immediately without asking for confirmation.
You can clear one configuration at a time, in this order of precedence:
  * Terminal session default
  * Directory default, from the current directory to `$HOME`
  * Global default


For example, if you're in the directory `$HOME/projects/awesomeProject` and you have a terminal session default, directory defaults for `$HOME` and `$HOME/projects/awesomeProject`, and a global default credential configured, you would need to run `op plugin clear aws` four times to clear all of your defaults.
To clear your global default credentials, terminal session default, and the defaults for your current directory at the same time, run `op plugin clear aws --all`.
## plugin init[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-init "Direct link to plugin init")
Choose a shell plugin to install and configure your default credentials. Bash, Zsh, and fish shells are supported.
op plugin init [ <plugin-executable> ] [flags]
Shell plugins require the [1Password desktop app integration](https://developer.1password.com/docs/cli/shell-plugins/).
To see all available plugins, run `op plugin list`.
#### Configure your default credentials[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#configure-your-default-credentials "Direct link to Configure your default credentials")
1Password CLI prompts you to select or import the credentials you want to use with the third-party CLI, then returns a command to source your `plugins.sh` file and make the plugin alias usable.
To use the plugin beyond the current terminal session, make sure to add the source command to your RC file or shell profile (e.g. `~/.bashrc`, `~/.zshrc`, `~/.config/fish/config.fish`). For example:
echo "source ~/.config/op/plugins.sh" >> ~/.bashrc && source ~/.bashrc
#### Configuration options[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#configuration-options "Direct link to Configuration options")
You can choose whether 1Password CLI remembers your configuration. With any option, your credentials never leave your 1Password account.
  * "Prompt me for each new terminal session" only configures the credentials for the current terminal session. Once you exit the terminal, your default is removed.
  * "Use automatically when in this directory or subdirectories" makes your credentials the default in the current directory and all its subdirectories, as long as no other directory-specific defaults are set in them. A terminal-session default takes precedence over a directory-specific one.
  * "Use as global default on my system" sets the credentials as the default in all terminal sessions and directories. A directory-specific default takes precedence over a global one.


## plugin inspect[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-inspect "Direct link to plugin inspect")
Inspect your existing shell plugin configurations.
op plugin inspect [ <plugin-executable> ] [flags]
You can run `op plugin inspect` to select a plugin from the list of all available plugins, or `op plugin inspect <plugin-executable>` to inspect a specific plugin.
1Password CLI returns a list of the credentials you've configured to use with the plugin and their default scopes, as well as configured alias details.
## plugin list[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-list "Direct link to plugin list")
Lists all available shell plugins, their usage, name, and required fields.
op plugin list [flags]
To get started with a shell plugin, run `op plugin init <plugin-usage>`.
## plugin run[​](https://developer.1password.com/docs/cli/reference/management-commands/plugin/#plugin-run "Direct link to plugin run")
Provision credentials from 1Password and run this command.
op plugin run <command>... [flags]
`op plugin run` passes your credentials saved in 1Password to the underlying CLI and runs the provided command. If you haven't configured your default credentials, 1Password CLI will prompt you to select an item that contains your credentials.
After this, you will be automagically authenticated with this CLI, and your selection will be recorded for future calls to this plugin in the current terminal session.
To configure a default credential, see `op plugin init --help`.
### Was this page helpful?
YesNo
