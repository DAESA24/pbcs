---
title: "Update to the latest version of 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/update/"
captured: 2025-12-15
category: concepts
relevance:
  - authentication
keywords:
  - 1password-cli
related: []
---

# Update to the latest version of 1Password CLI | 1Password Developer

On this page
To make sure you're up to date with the latest features and security improvements, always use the latest version of 1Password CLI.
To check what version you currently have installed, use `op --version`.
## Download the latest version[​](https://developer.1password.com/docs/cli/reference/update/#download-the-latest-version "Direct link to Download the latest version")
There are two ways you can download the latest version for your platform and architecture:
  * Visit our 
  * Use `op update` to download the latest version from the command line. Set the `--directory` flag to choose where to download the installer (defaults to `~/Downloads`) and confirm the download.


You can use `op update` without signing in.
After downloading the appropriate installer, follow the [installation instructions](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli) to finish the update.
## Update with a package manager[​](https://developer.1password.com/docs/cli/reference/update/#update-with-a-package-manager "Direct link to Update with a package manager")
If you installed 1Password CLI with a package manager, use the following commands to update your installation.
  * Mac
  * Linux


**Brew**
brew upgrade --cask 1password-cli
  * Apt
  * Yum
  * Alpine


sudo apt update && sudo apt install 1password-cli
sudo dnf check-update -y 1password-cli && sudo dnf install 1password-cli
apk add --update-cache 1password-cli
### Was this page helpful?
YesNo
