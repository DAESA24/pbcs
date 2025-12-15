---
title: "completion | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/commands/completion/"
captured: 2025-12-15
category: commands
relevance:
  - script integration
keywords:
  - 1password-cli
related: []
---

# completion | 1Password CLI | 1Password Developer

On this page
# completion
Generate shell completion information for 1Password CLI.
op completion <shell> [flags]
If you use Bash, Zsh, fish, or PowerShell, you can add shell completion for 1Password CLI. With completions loaded, after you start typing a command, press Tab to see available commands and options.
#### Load shell completion information for Bash[​](https://developer.1password.com/docs/cli/reference/commands/completion/#load-shell-completion-information-for-bash "Direct link to Load shell completion information for Bash")
To always load the completion information for Bash, add this to your `.bashrc` file:
source <(op completion bash)
To use shell completion in Bash, you’ll need the `bash-completion` package.
#### Load shell completion information for Zsh[​](https://developer.1password.com/docs/cli/reference/commands/completion/#load-shell-completion-information-for-zsh "Direct link to Load shell completion information for Zsh")
To always load the completion information for Zsh, add this to your `.zshrc` file:
eval "$(op completion zsh)"; compdef _op op
#### Load shell completion information for fish[​](https://developer.1password.com/docs/cli/reference/commands/completion/#load-shell-completion-information-for-fish "Direct link to Load shell completion information for fish")
To always load the completion information for fish, add this to your `.fish` file:
op completion fish | source
#### Load shell completion information for PowerShell[​](https://developer.1password.com/docs/cli/reference/commands/completion/#load-shell-completion-information-for-powershell "Direct link to Load shell completion information for PowerShell")
To always load the completion information for PowerShell, add this to your `.ps1` file:
op completion powershell | Out-String | Invoke-Expression
To use shell completion in PowerShell, you need to enable execution of scripts. To do that, start a PowerShell window as administrator and run the following command:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
### Was this page helpful?
YesNo
