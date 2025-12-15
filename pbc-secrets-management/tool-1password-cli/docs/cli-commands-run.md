---
title: "run | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/commands/run/"
captured: 2025-12-15
category: commands
relevance:
  - secret retrieval
  - environment variables
  - script integration
  - authentication
  - vault management
keywords:
  - op://
  - vault
  - item
  - secret reference
  - op run
  - environment variable
  - service account
  - session
related: []
---

# run | 1Password CLI | 1Password Developer

On this page
# run
Pass secrets as environment variables to an application or script.
op run -- <command> <command>... [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/commands/run/#flags "Direct link to Flags")
--env-file stringArray Enable Dotenv integration with specific Dotenv files to
parse. For example: --env-file=.env.
--no-masking Disable masking of secrets on stdout and stderr.
`op run` scans environment variables for secret references, loads the corresponding secrets from 1Password, then runs the provided command in a subprocess with the secrets made available as environment variables for the duration of the subprocess.
To limit which 1Password items processes in your authorized terminal session can access, move the items you want to use with `op run` to a separate vault and use the command with a service account that only has access to that vault.
[Learn more about service accounts.](https://developer.1password.com/docs/service-accounts/)
[Learn more about secret references.](https://developer.1password.com/docs/cli/secret-references/)
If the same environment variable name exists in both the shell and the environment file, the environment file takes precedence.
If the same environment variable name exists in multiple environment files, the last environment file takes precedence.
Secrets printed to stdout or stderr are concealed by default. Include the `--no-masking` flag to turn off masking.
### Examples[​](https://developer.1password.com/docs/cli/reference/commands/run/#examples "Direct link to Examples")
Print secret value:
export DB_PASSWORD="op://app-prod/db/password"
op run -- printenv DB_PASSWORD
<concealed by 1Password>
op run --no-masking -- printenv DB_PASSWORD
fX6nWkhANeyGE27SQGhYQ
Specify an environment file and use it:
echo "DB_PASSWORD=op://app-dev/db/password" > .env
op run --env-file="./.env" -- printenv DB_PASSWORD
password
Use variables in secret references to switch between different sets of secrets for different environments:
cat .env
DB_USERNAME = op://$APP_ENV/db/username
DB_PASSWORD = op://$APP_ENV/db/password
export APP_ENV="dev"
op run --env-file="./.env" -- printenv DB_PASSWORD
dev
export APP_ENV="prod"
op run --env-file="./.env" -- printenv DB_PASSWORD
prod
### Was this page helpful?
YesNo
