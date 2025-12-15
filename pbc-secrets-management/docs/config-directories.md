---
title: "How 1Password CLI detects configuration directories | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/config-directories/"
captured: 2025-12-15
category: concepts
relevance:
  - environment variables
keywords:
  - environment variable
related: []
---

# How 1Password CLI detects configuration directories | 1Password Developer

1Password CLI configuration directories default to:
  * `${XDG_CONFIG_HOME}/op` when `${XDG_CONFIG_HOME}` is set
  * `~/.config/op` when `${XDG_CONFIG_HOME}` is not set


1Password CLI detects the configuration directory to read or write to in this order of precedence:
  1. A directory specified with `--config`
  2. A directory set with the `OP_CONFIG_DIR` environment variable.
  3. `~/.op` (following 
  4. `${XDG_CONFIG_HOME}/.op`
  5. `~/.config/op` (following 
  6. `${XDG_CONFIG_HOME}/op`


### Was this page helpful?
YesNo
