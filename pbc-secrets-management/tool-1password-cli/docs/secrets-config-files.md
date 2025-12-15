---
title: "Load Secrets Into Config Files | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/secrets-config-files/"
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
  - op item
  - environment variable
  - service account
related: []
---

# Load Secrets Into Config Files | 1Password Developer

On this page
# Load secrets into config files
With 1Password CLI, you can use [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/) to automatically load secrets into configuration files from your 1Password account without putting any plaintext secrets in code. This allows you to check config files into source control and keep them in sync throughout developer workstations, CI, and production servers, which is otherwise manual and error-prone work.
We recommend using [1Password Service Accounts](https://developer.1password.com/docs/service-accounts/) to follow the [principle of least privilege](https://developer.1password.com/docs/cli/best-practices/). Service accounts support restricting 1Password CLI to specific vaults, so that processes in your authorized terminal session can only access items required for a given purpose.
## Requirements[​](https://developer.1password.com/docs/cli/secrets-config-files/#requirements "Direct link to Requirements")
Before you can use 1Password to secure your config files, you'll need to:
  1. [Sign up for 1Password.](https://1password.com/pricing/password-manager)
  2. [Install 1Password CLI.](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli)
  3. Store the secrets you want to provision in your 1Password account.


## Step 1: Get secret references[​](https://developer.1password.com/docs/cli/secrets-config-files/#step-1-get-secret-references "Direct link to Step 1: Get secret references")
You can get secret references in several ways:
  * [With the 1Password desktop app](https://developer.1password.com/docs/cli/secret-reference-syntax#with-the-1password-desktop-app): Copy secret references from the app.
  * [With 1Password for VSCode](https://developer.1password.com/docs/vscode#get-values): Insert secret references from 1Password as you edit code.
  * [With 1Password CLI](https://developer.1password.com/docs/cli/secret-reference-syntax#with-1password-cli): Get secret references for one or multiple fields with `op item get`.
  * Use the [secret reference syntax rules](https://developer.1password.com/docs/cli/secret-reference-syntax#syntax-rules) to write secret references manually.


## Step 2: Use secret references in your config file[​](https://developer.1password.com/docs/cli/secrets-config-files/#step-2-use-secret-references-in-your-config-file "Direct link to Step 2: Use secret references in your config file")
Replace the plaintext secrets in your config file with the appropriate secret references, following the [template syntax](https://developer.1password.com/docs/cli/secrets-template-syntax/).
For example, if you start with a config file that looks like this:
config.yml
database:
host: http://localhost
port: 5432
username: mysql-user
password: piG1rX5P1QMF6J5k7u7sNb
And you saved the `username` and `password` secrets on the `mysql` item in the `prod` vault, you would end up with this templated config file:
config.yml.tpl
database:
host: http://localhost
port: 5432
username: op://prod/mysql/username
password: op://prod/mysql/password
## Step 2: Inject the secrets[​](https://developer.1password.com/docs/cli/secrets-config-files/#step-2-inject-the-secrets "Direct link to Step 2: Inject the secrets")
To load secrets from the config file and provision them at runtime, use `op inject` to inject the secrets directly into your production environment. For example:
op inject -i config.yml.tpl -o config.yml
In the output file, `config.yml`, you'll see the secret references replaced with the plaintext secrets they reference.
The config file template is stored together with the code in source control, so that every developer can see the structure of the file.
Make sure to delete the resolved config file when you no longer need it.
## Step 3: Differentiate between environments[​](https://developer.1password.com/docs/cli/secrets-config-files/#step-3-differentiate-between-environments "Direct link to Step 3: Differentiate between environments")
We highly recommend you organize your 1Password items in the same way across all of your environments. For example: `app/dev/db/password` and `app/prod/db/password`.
If you do this, you can use variables in your template file to switch to a different set of secrets. You can have variables for your environment, stage, region, or anything else. For example:
config.yml.tpl
database:
host: http://localhost
port: 5432
username: op://$APP_ENV/mysql/username
password: op://$APP_ENV/mysql/password
You can then set the `APP_ENV` variable when you inject into the template, using the [Template Syntax](https://developer.1password.com/docs/cli/secrets-template-syntax/):
  * Bash, Zsh, sh, fish
  * PowerShell


APP_ENV=prod op inject -i config.yml.tpl -o config.yml
  1. Set `APP_ENV` to `prod`:
$Env:APP_ENV = "prod"
  2. Inject the secrets:
op inject -i config.yml.tpl -o config.yml


This allows you to use the same template file, stored in source control next to your application, for all your deployments.
## Optional: Use `op inject` in production[​](https://developer.1password.com/docs/cli/secrets-config-files/#optional-use-op-inject-in-production "Direct link to optional-use-op-inject-in-production")
Now that the application works with the right configuration locally, you can use 1Password CLI to provision secrets in production environments.
To do this, you'll first need to:
  1. [Install 1Password CLI 2 in your production environment.](https://developer.1password.com/docs/cli/install-server/)
  2. [Set up a Secrets Automation workflow](https://developer.1password.com/docs/connect/).
  3. [Deploy 1Password Connect Server](https://developer.1password.com/docs/connect/get-started#step-2-deploy-a-1password-connect-server) and make it accessible to your production environment.


To use 1Password CLI with a Connect server, set the `OP_CONNECT_HOST` and `OP_CONNECT_TOKEN` environment variables to your Connect instance's credentials in your production environment.
You can now move your secrets to config files and have them readily accessible with `op inject`.
The following commands can be used with a Connect server:
  * `op run`
  * `op inject`
  * `op read`
  * `op item get`


## Learn more[​](https://developer.1password.com/docs/cli/secrets-config-files/#learn-more "Direct link to Learn more")
  * [Load secrets into the environment](https://developer.1password.com/docs/cli/secrets-environment-variables/)
  * [Secret reference syntax](https://developer.1password.com/docs/cli/secret-reference-syntax/)
  * [Template syntax](https://developer.1password.com/docs/cli/secrets-template-syntax/)


### Was this page helpful?
YesNo
