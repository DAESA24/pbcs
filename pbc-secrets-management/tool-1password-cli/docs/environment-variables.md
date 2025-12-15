---
title: "1Password CLI environment variables | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/environment-variables/"
captured: 2025-12-15
category: integrations
relevance:
  - secret retrieval
  - environment variables
  - script integration
  - authentication
  - vault management
keywords:
  - vault
  - item
  - op run
  - op item
  - environment variable
  - service account
  - biometric
  - session
related: []
---

# 1Password CLI environment variables | 1Password Developer

You can use the following environment variables with 1Password CLI:
Environment variable | Description  
---|---  
`OP_ACCOUNT` | Specifies a default 1Password account to execute commands. Accepts an [account sign-in address or ID](https://developer.1password.com/docs/cli/use-multiple-accounts#find-an-account-sign-in-address-or-id). An account specified with the `--account` flag takes precedence.  
`OP_BIOMETRIC_UNLOCK_ENABLED` | Toggles the [1Password app integration](https://developer.1password.com/docs/cli/app-integration#optional-set-the-biometric-unlock-environment-variable) on or off. Options: `true`, `false`.  
`OP_CACHE` | Toggles the option to [store and use cached information](https://developer.1password.com/docs/cli/reference#cache-item-and-vault-information) on or off. Options: `true`, `false`. Default: `true`.  
`OP_CONFIG_DIR` | Specifies a [configuration directory](https://developer.1password.com/docs/cli/config-directories) to read and write to. A directory specified with the `--config` flag takes precedence.  
`OP_CONNECT_HOST` | Sets a [Connect server instance host URL](https://developer.1password.com/docs/connect/cli/) to use with 1Password CLI.  
`OP_CONNECT_TOKEN` | Sets a [Connect server token](https://developer.1password.com/docs/connect/cli/) to use with 1Password CLI.  
`OP_DEBUG` | Toggles debug mode on or off. Options: `true`, `false`. Default: `false`.  
`OP_FORMAT` | Sets the output format for 1Password CLI commands. Options: `human-readable`, `json`. Default: `human-readable`.  
`OP_INCLUDE_ARCHIVE` | Allows items in the archive to be retrieved with [`op item get`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get) and [`op document get`](https://developer.1password.com/docs/cli/reference/management-commands/document#document-get) commands. Options: `true`, `false`. Default: `false`.  
`OP_ISO_TIMESTAMPS` | Toggles the option to format timestamps according to ISO 8601 and RFC 3339 standards on or off. Options: `true`, `false`. Default: `false`.  
`OP_RUN_NO_MASKING` | Toggles masking off for the output of [`op run`](https://developer.1password.com/docs/cli/reference/commands/run).  
`OP_SESSION` | Stores a session token when you [sign in to 1Password CLI manually](https://developer.1password.com/docs/cli/sign-in-manually).  
`OP_SERVICE_ACCOUNT_TOKEN` | Configures 1Password CLI to [authenticate with a service account](https://developer.1password.com/docs/service-accounts/use-with-1password-cli).  
### Was this page helpful?
YesNo
