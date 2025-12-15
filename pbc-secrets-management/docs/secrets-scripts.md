---
title: "Load secrets into scripts | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/secrets-scripts/"
captured: 2025-12-15
category: security
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
  - field
  - secret reference
  - op read
  - op run
  - environment variable
  - service account
  - template
related: []
---

# Load secrets into scripts | 1Password Developer

On this page
You can use 1Password CLI to load secrets into your scripts, so that the credentials in your scripts are always in sync with the information in your 1Password account and your secrets are never exposed in plaintext.
You can use the following methods to load secrets into scripts, separately or in combination:
  1. [Use `op run` to load secrets into the environment.](https://developer.1password.com/docs/cli/secrets-scripts/#option-1-use-op-run-to-load-secrets-into-the-environment)
  2. [Use `op read` to read secrets.](https://developer.1password.com/docs/cli/secrets-scripts/#option-2-use-op-read-to-read-secrets)
  3. [Use `op inject` to load secrets into a config file.](https://developer.1password.com/docs/cli/secrets-scripts/#option-3-use-op-inject-to-load-secrets-into-a-config-file)
  4. [Use `op plugin run` to load secrets using a shell plugin.](https://developer.1password.com/docs/cli/secrets-scripts/#option-4-use-op-plugin-run-to-load-secrets-using-a-shell-plugin)


We recommend using [1Password Service Accounts](https://developer.1password.com/docs/service-accounts/) to follow the [principle of least privilege](https://developer.1password.com/docs/cli/best-practices/). Service accounts support restricting 1Password CLI to specific vaults, so that processes in your authorized terminal session can only access items required for a given purpose.
Service accounts are also useful if your personal account has SSO or MFA requirements.
## Requirements[​](https://developer.1password.com/docs/cli/secrets-scripts/#requirements "Direct link to Requirements")
Before you can use 1Password CLI to load secrets into your scripts, you'll need to:
  1. [Sign up for 1Password.](https://1password.com/pricing/password-manager)
  2. [Install 1Password CLI.](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli)
  3. Store the secrets you need for your script in your 1Password account.


## Option 1: Use `op run` to load secrets into the environment[​](https://developer.1password.com/docs/cli/secrets-scripts/#option-1-use-op-run-to-load-secrets-into-the-environment "Direct link to option-1-use-op-run-to-load-secrets-into-the-environment")
You can use an environment file with [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/) instead of plaintext secrets, then pass the secrets to your script at runtime using [`op run`](https://developer.1password.com/docs/cli/reference/commands/run/).
This method [allows you to easily change which set of secrets you use with each environment](https://developer.1password.com/docs/cli/secrets-environment-variables#step-3-differentiate-between-environments), so that DevOps engineers can use the script in production with one set of secrets while developers use the same script with different secrets on their local machine.
For example, if you supply an AWS command in your script with secrets using the `AWS_SECRET_ACCESS_KEY` and `AWS_ACCESS_KEY_ID` environment variables, and your credentials are saved in the fields `secret-key` and `access-key` on the `aws` item in the `prod` vault, your environment file might look like this:
yourscript.env
AWS_SECRET_ACCESS_KEY=op://prod/aws/secret-key
AWS_ACCESS_KEY_ID=op://prod/aws/access-key
To pass the secrets to the script, wrap the entire script in `op run` with the `--env-file` flag set to your environment file:
op run --env-file yourscript.env -- yourscript.sh
Learn more about [loading secrets into the environment](https://developer.1password.com/docs/cli/secrets-environment-variables/).
## Option 2: Use `op read` to read secrets[​](https://developer.1password.com/docs/cli/secrets-scripts/#option-2-use-op-read-to-read-secrets "Direct link to option-2-use-op-read-to-read-secrets")
You can use `op read` with secret references [directly in your script](https://developer.1password.com/docs/cli/secrets-scripts/#directly-in-your-script) or [with environment variables](https://developer.1password.com/docs/cli/secrets-scripts/#with-environment-variables).
### Directly in your script[​](https://developer.1password.com/docs/cli/secrets-scripts/#directly-in-your-script "Direct link to Directly in your script")
With this method, secrets are only passed to the single command that includes the secret reference.
For example, to replace your Docker username and password with [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/) in a command to log in to Docker:
yourscript.sh
#!/bin/bash
  

docker login -u "$(op read op://prod/docker/username)" -p "$(op read op://prod/docker/password)"
### With environment variables[​](https://developer.1password.com/docs/cli/secrets-scripts/#with-environment-variables "Direct link to With environment variables")
You can also include a command to set environment variables to `op read` and [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/) in your script.
For example, if you supply an AWS command in your script with secrets using the `AWS_SECRET_ACCESS_KEY` and `AWS_ACCESS_KEY_ID` environment variables, your script might look like this:
yourscript.sh
#!/bin/bash
  

export AWS_SECRET_ACCESS_KEY="$(op read op://prod/aws/secret-key)"
export AWS_ACCESS_KEY_ID="$(op read op://prod/aws/access-key-id)"
aws sts get-caller-identity
## Option 3: Use `op inject` to load secrets into a config file[​](https://developer.1password.com/docs/cli/secrets-scripts/#option-3-use-op-inject-to-load-secrets-into-a-config-file "Direct link to option-3-use-op-inject-to-load-secrets-into-a-config-file")
If your script uses a configuration file, you can template the config file with [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/), then use [`op inject`](https://developer.1password.com/docs/cli/reference/commands/inject/) to pass the config file with the resolved secrets to your script at runtime.
This allows you to check config files into source control and keep them in sync throughout developer workstations, CI, and production servers. And you can include template variables within the secret references to [load different sets of secrets for different environments](https://developer.1password.com/docs/cli/secrets-config-files#step-3-differentiate-between-environments).
[Learn how to load secrets into config files](https://developer.1password.com/docs/cli/secrets-config-files/).
## Option 4: Use `op plugin run` to load secrets using a shell plugin[​](https://developer.1password.com/docs/cli/secrets-scripts/#option-4-use-op-plugin-run-to-load-secrets-using-a-shell-plugin "Direct link to option-4-use-op-plugin-run-to-load-secrets-using-a-shell-plugin")
If your script runs interactively and each person using the script authenticates with their own personal token, you can minimize the configuration required in advance of using the script with a [1Password Shell Plugin](https://developer.1password.com/docs/cli/shell-plugins/). Shell plugins prompt each user to select their credentials when the script is executed.
Each person using the script will be prompted to configure when their credentials should be used to authenticate. To make sure the credentials they selected will also be used for future invocations of the script, they can configure their credentials as a global or directory default.
To use a shell plugin to authenticate an individual command, wrap the command in [`op plugin run`](https://developer.1password.com/docs/cli/reference/management-commands/plugin#plugin-run). For example, to use the AWS shell plugin to provide an AWS Access Key and Secret Key ID to the `sts get-caller-identity` command:
yourscript.sh
#!/bin/bash
  

op plugin run -- aws sts get-caller-identity
To use a shell plugin throughout a script, you can include an alias for the tool's executable command at the beginning of the script. For example, in this script, the AWS shell plugin would be used to supply secrets for every `aws` command in the script.
yourscript.sh
#!/bin/bash
  

alias aws="op plugin run -- aws"
aws sts get-caller-identity
If a shell plugin doesn't exist for the tool you're using, you can [build a new plugin](https://developer.1password.com/docs/cli/shell-plugins/contribute/).
## Learn more[​](https://developer.1password.com/docs/cli/secrets-scripts/#learn-more "Direct link to Learn more")
  * [Example CLI scripts](https://developer.1password.com/docs/cli/scripts/)
  * [Get started with secret references](https://developer.1password.com/docs/cli/secret-references/)
  * [Load secrets into the environment](https://developer.1password.com/docs/cli/secrets-environment-variables/)
  * [Load secrets into config files](https://developer.1password.com/docs/cli/secrets-config-files/)
  * [Use 1Password Shell Plugins to securely authenticate third-party CLIs](https://developer.1password.com/docs/cli/shell-plugins/)


### Was this page helpful?
YesNo
