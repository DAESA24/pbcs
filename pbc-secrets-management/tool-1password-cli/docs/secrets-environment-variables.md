---
title: "Load secrets into the environment | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/secrets-environment-variables/"
captured: 2025-12-15
category: security
relevance:
  - secret retrieval
  - environment variables
  - authentication
  - vault management
  - security patterns
keywords:
  - op://
  - vault
  - item
  - field
  - secret reference
  - op run
  - op item
  - environment variable
  - service account
  - template
related: []
---

# Load secrets into the environment | 1Password Developer

On this page
With 1Password CLI, you can provision [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/) as environment variables to simplify the process of creating multiple configurations for different environments. Secret references allow you to edit your secrets in 1Password without having to make any changes to your configuration settings or put any plaintext secrets in code.
After you've set your environment variables to secret references, you can use [`op run`](https://developer.1password.com/docs/cli/reference/commands/run/) to provision an app with the secrets it requires.
Many applications that follow the popular 
We recommend using [1Password Service Accounts](https://developer.1password.com/docs/service-accounts/) to follow the [principle of least privilege](https://developer.1password.com/docs/cli/best-practices/). Service accounts support restricting 1Password CLI to specific vaults, so that processes in your authorized terminal session can only access items required for a given purpose.
You should assume that processes on your computer can access the environment of other processes run by the same user. Be aware of this when supplying secrets through environment variables.
## Requirements[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#requirements "Direct link to Requirements")
Before you can load secrets into the environment, you'll need to:
  1. [Sign up for 1Password.](https://1password.com/pricing/password-manager)
  2. [Install 1Password CLI.](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli)
  3. Store the secrets you want to provision in your 1Password account.


## Step 1: Get secret references[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#step-1-get-secret-references "Direct link to Step 1: Get secret references")
You can get secret references in several ways:
  * [With the 1Password desktop app](https://developer.1password.com/docs/cli/secret-reference-syntax#with-the-1password-desktop-app): Copy secret references from the app.
  * [With 1Password for VSCode](https://developer.1password.com/docs/vscode#get-values): Insert secret references from 1Password as you edit code.
  * [With 1Password CLI](https://developer.1password.com/docs/cli/secret-reference-syntax#with-1password-cli): Get secret references for one or multiple fields with `op item get`.
  * Use the [secret reference syntax rules](https://developer.1password.com/docs/cli/secret-reference-syntax#syntax-rules) to write secret references manually.


## Step 2: Pass the secrets to the application[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#step-2-pass-the-secrets-to-the-application "Direct link to Step 2: Pass the secrets to the application")
To provision an app with the secrets it needs, map the secret references to the appropriate environment variables, then use `op run` to pass the secrets to the application.
There are two ways to do this:
### Export environment variables[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#export-environment-variables "Direct link to Export environment variables")
You can individually export environment variables as [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/) from the command line.
  1. Export the necessary environment variables:
     * Bash, Zsh, sh
     * fish
     * PowerShell
export GITHUB_TOKEN=op://development/GitHub/credentials/personal_token
set -x GITHUB_TOKEN op://development/GitHub/credentials/personal_token
$Env:GITHUB_TOKEN = "op://development/GitHub/credentials/personal_token"
  2. Run `op run --` with your command for starting the app:
op run -- gh


### Use environment (`.env`) files[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#use-environment-env-files "Direct link to use-environment-env-files")
Environment files allow you to define multiple (secret) environment variables with `KEY=VALUE` statements separated by a newline. These files have the `.env` extension.
You can check environment files into source control and use the same environment everywhere. For example, if you use environment files for your test secrets, you can run your tests both locally and in CI without having to provision the secrets separately.
prod.env
AWS_ACCESS_KEY_ID="op://development/aws/Access Keys/access_key_id"
AWS_SECRET_ACCESS_KEY="op://development/aws/Access Keys/secret_access_key"
To use environment files with `op run`, specify the path to the environment file with the flag `--env-file`:
op run --env-file="./prod.env" -- aws
Environment file syntax rules
The `.env` file parsing engine follows the following rules:
  * Environment variables are defined as `KEY=VALUE` statements separated by a newline.
  * Variables can span multiple lines if they are enclosed in either `'` or `"`:
MY_VAR = "this is on the first line
and this is on the second line"
  * Empty lines are skipped.
  * Lines beginning with `#` are treated as comments. Comments can also be placed inline after `KEY=VALUE` statements.
  * Empty values become empty strings. For example, `EMPTY=` will set the environment variable `EMPTY` to the empty string.
  * If a value is surrounded by single or double quotes, these quotes do not end up in the evaluated value. So `KEY="VALUE"` and `KEY='VALUE'` both evaluate to `KEY` and `VALUE`.
  * Occurrences of `$VAR_NAME` or `${VAR_NAME}` are replaced with their respective value from the environment.
  * A variable defined in a .env file can be referred to later in the same file:
SOME_VAR = value
OTHER_VAR = ${SOME_VAR}
  * Special characters can be escaped with `\`. For example, `MY_VAR = "\$SOME_VAR that is not actually replaced."` results in the following value for MY_VAR: `$SOME_VAR that is not actually replaced.`.
  * Inner quotes are maintained, so `JSON={"foo":"bar"}` evaluates to `JSON` and `{"foo":"bar"}`.
  * Variables do not get replaced in values that are enclosed in single quotes. So `KEY='$SOME_VAR'` evaluates to `KEY` and `$SOME_VAR`.
  * Template syntax can be used in the `VALUE` to inject secrets. The `KEY` can only contain template variables.
  * Template parsing is performed after `.env` file parsing, so you cannot use the former to construct the latter.
  * Leading and trailing whitespace of both `KEY` and `VALUE` segments are ignored, so `KEY = VALUE` is parsed the same as `KEY=VALUE`.
  * Single and double quoted values maintain both leading and trailing whitespace, so `KEY=" some value "` evaluates to `KEY` and ` some value `.
  * These files should use UTF-8 character encoding.


### Expand variables in a subshell[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#expand-variables-in-a-subshell "Direct link to Expand variables in a subshell")
When you reference a variable like `$MY_VAR` in the same command where you call `op run`, your shell expands `$MY_VAR` before `op run` can substitute the secret reference. For example, a command like the following **will not** resolve the secret from 1Password:
MY_VAR=op://vault/item/field op run --no-masking -- echo "$MY_VAR"
To make sure `op run` substitutes the secret before the variable expands, run the command to expand the variable in a subshell:
MY_VAR=op://vault/item/field op run --no-masking -- sh -c 'echo "$MY_VAR"'
See result...
skdjfs7dyrwhk4jhref
## Step 3: Differentiate between environments[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#step-3-differentiate-between-environments "Direct link to Step 3: Differentiate between environments")
If you have different sets of secrets for different environments, you can use a single environment file to pass the appropriate secrets to the application.
To do this, make sure you structure your 1Password secrets in the same way across all your environments. For example: `dev/mysql/password` and `prod/mysql/password`.
Then, include an externally set variable (`$VARIABLE_NAME`) in place of the vault name for each secret in your environment file. This will allow you to specify which set of secrets you use with each environment.
For example, in the following `.env` file, `$APP_ENV` is the externally set environment variable:
app.env
MYSQL_DATABASE = "op://$APP_ENV/mysql/database"
MYSQL_USERNAME = "op://$APP_ENV/mysql/username"
MYSQL_PASSWORD = "op://$APP_ENV/mysql/password"
To use the set of secrets from the `dev` vault to deploy an app in the development environment:
  * Bash, Zsh, sh, fish
  * PowerShell


APP_ENV=dev op run --env-file="./app.env" -- myapp deploy
  1. Set the `$APP_ENV` variable:
$ENV:APP_ENV = "dev"
  2. Run `op run` with the environment file:
op run --env-file="./app.env" -- myapp deploy


## Next step: Run in production[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#next-step-run-in-production "Direct link to Next step: Run in production")
Now that the application works with the right configuration locally, you can [use 1Password CLI with a 1Password Connect Server](https://developer.1password.com/docs/connect/cli/) to provision secrets in production environments. You can also [set up 1Password CLI in CI](https://developer.1password.com/docs/connect/cli#continuous-integration-ci-environments), and define your secret references alongside other configurations.
## Learn more[​](https://developer.1password.com/docs/cli/secrets-environment-variables/#learn-more "Direct link to Learn more")
  * [Use 1Password Connect Server with 1Password CLI](https://developer.1password.com/docs/connect/cli#continuous-integration-ci-environments)
  * [Load secrets into config files](https://developer.1password.com/docs/cli/secrets-config-files/)
  * [Secret reference syntax](https://developer.1password.com/docs/cli/secret-reference-syntax/)
  * [Template syntax](https://developer.1password.com/docs/cli/secrets-template-syntax/)


### Was this page helpful?
YesNo
