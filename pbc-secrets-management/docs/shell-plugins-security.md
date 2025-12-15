---
title: "About 1Password Shell Plugins security | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/security/"
captured: 2025-12-15
category: security
relevance:
  - script integration
  - authentication
  - vault management
keywords:
  - biometric
  - session
related: []
---

# About 1Password Shell Plugins security | 1Password Developer

On this page
## Authorization model[​](https://developer.1password.com/docs/cli/shell-plugins/security/#authorization-model "Direct link to Authorization model")
To get your consent when a 1Password CLI command or 1Password Shell Plugin is invoked, 1Password will present you with an approval dialog:
![A CLI being authenticated using 1Password CLI biometric unlock.](https://developer.1password.com/img/shell-plugins/aws-5.png)
This dialog will show which application is requesting permission to use which 1Password account. After you approve the request, a _session_ will be established between 1Password and the terminal window or tab the plugin was invoked from.
Any consecutive invocations of 1Password CLI within that terminal window can use your 1Password account without additional authorization until 1Password locks. This includes invocations of the same plugin, a different plugin and any other 1Password CLI commands. As always when working with secrets, it's worth being mindful of the processes, scripts, and plugins you run that can access those secrets.
A session is ended in any of the following scenarios:
  * When 1Password is locked
  * After 10 minutes of inactivity
  * After 12 hours
  * When `op signout` is run in the authorized terminal session
  * When `op signout --all` is run in any terminal session


## Extendability & community contributions[​](https://developer.1password.com/docs/cli/shell-plugins/security/#extendability--community-contributions "Direct link to Extendability & community contributions")
1Password Shell Plugins is [extendable](https://developer.1password.com/docs/cli/shell-plugins/contribute/). Contributed plugins are curated and reviewed by 1Password before they are included and shipped in 1Password CLI.
1Password has only reviewed contributed plugins if they are included in 1Password CLI. We recommend you only run plugins included in 1Password CLI and plugins you've written yourself. In practice, this means you should not download binaries and place them in `~/.op/plugins/local`.
## Learn more[​](https://developer.1password.com/docs/cli/shell-plugins/security/#learn-more "Direct link to Learn more")
  * [Biometric security](https://developer.1password.com/docs/cli/app-integration/)


### Was this page helpful?
YesNo
