---
title: "1Password Developer"
source_url: "https://developer.1password.com/docs/cli/secret-references/"
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

# 1Password Developer

On this page
With 1Password CLI, you can use [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax) to securely load information saved in 1Password into environment variables, configuration files, and scripts without exposing any secrets in plaintext.
A secret reference URI includes the names (or [unique identifiers](https://developer.1password.com/docs/cli/reference#unique-identifiers-ids)) of the vault, item, section, and field where a secret is stored in your 1Password account:
op://<vault-name>/<item-name>/[section-name/]<field-name>
To replace secret references with the secrets they refer to at runtime, use [`op read`](https://developer.1password.com/docs/cli/secret-references/#with-op-read), [`op run`](https://developer.1password.com/docs/cli/secret-references/#with-op-run), or [`op inject`](https://developer.1password.com/docs/cli/secret-references/#with-op-inject).
We recommend using [1Password Service Accounts](https://developer.1password.com/docs/service-accounts/) to follow the [principle of least privilege](https://developer.1password.com/docs/cli/best-practices/). Service accounts support restricting 1Password CLI to specific vaults, so that processes in your authorized terminal session can only access items required for a given purpose.
## Requirements[​](https://developer.1password.com/docs/cli/secret-references/#requirements "Direct link to Requirements")
Before you can use secret references to securely load your secrets with 1Password CLI, you'll need to:
  1. [Sign up for 1Password.](https://1password.com/pricing/password-manager)
  2. [Install 1Password CLI.](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli)
  3. Save the secrets you want to reference in your 1Password account.


## Step 1: Get secret references[​](https://developer.1password.com/docs/cli/secret-references/#step-1-get-secret-references "Direct link to Step 1: Get secret references")
You can get secret references in several ways:
  * [With the 1Password desktop app](https://developer.1password.com/docs/cli/secret-reference-syntax#with-the-1password-desktop-app): Copy secret references from the app.
  * [With 1Password for VS Code](https://developer.1password.com/docs/vscode#get-values): Insert secret references from 1Password as you edit code.
  * [With 1Password CLI](https://developer.1password.com/docs/cli/secret-reference-syntax#with-1password-cli): Get secret references for one or multiple fields with `op item get`.
  * [With the secret reference syntax](https://developer.1password.com/docs/cli/secret-reference-syntax#syntax-rules): Write secret references manually.


## Step 2: Replace plaintext secrets with secret references[​](https://developer.1password.com/docs/cli/secret-references/#step-2-replace-plaintext-secrets-with-secret-references "Direct link to Step 2: Replace plaintext secrets with secret references")
After you create secret references, use them in place of plaintext secrets in your code.
The example below shows a GitHub environment file with a secret reference pointing to where the GitHub Personal Access Token is stored in 1Password rather than a plaintext token.
![An environment file using a plaintext secret and the same file using a secret reference.](https://developer.1password.com/img/cli/use-case-secret-reference.png)
## Step 3: Resolve secret references[​](https://developer.1password.com/docs/cli/secret-references/#step-3-resolve-secret-references "Direct link to Step 3: Resolve secret references")
There are three ways you can replace secret references with the actual secrets they reference at runtime:
  * [Use `op read` to write secrets to `stdout` or to a file.](https://developer.1password.com/docs/cli/secret-references/#with-op-read)
  * [Use `op run` to pass secrets as environment variables to a process.](https://developer.1password.com/docs/cli/secret-references/#with-op-run)
  * [Use `op inject` to inject secrets into configuration files or scripts.](https://developer.1password.com/docs/cli/secret-references/#with-op-inject)


### With `op read`[​](https://developer.1password.com/docs/cli/secret-references/#with-op-read "Direct link to with-op-read")
You can use [`op read`](https://developer.1password.com/docs/cli/reference/commands/read/) with a secret reference to print the secret to `stdout`.
op read op://development/GitHub/credentials/personal_token
See result...
ghp_WzgPAEutsFRZH9uxWYtw
To write the secret to a file instead of `stdout`, include the `--out-file` flag (or `-o`) with the path to the new file. For example, to create a file `token.txt` that contains the GitHub personal access token:
op read --out-file token.txt op://development/GitHub/credentials/personal_token
token.txt
ghp_WzgPAEutsFRZH9uxWYtw
You can also use `op read` with secret references to [load secrets into scripts](https://developer.1password.com/docs/cli/secrets-scripts/). For example, to use secret references in place of your Docker username and password with the `docker login` command:
myscript.sh
#!/bin/bash
  

docker login -u "$(op read op://prod/docker/username)" -p "$(op read op://prod/docker/password)"
#### Query parameters[​](https://developer.1password.com/docs/cli/secret-references/#query-parameters "Direct link to Query parameters")
You can use secret references with [query parameters](https://developer.1password.com/docs/cli/secret-reference-syntax#field-and-file-metadata-attributes) to get more information about an item.
To get information about item fields or file attachments, include the `attribute` (or `attr`) query parameter with the attribute you want to get.
op://<vault>/<item>[/<section>]/<field>?attribute=<attribute-value>
You can query the following attributes for fields: `type`, `value`, `title`, `id`, `purpose`, `otp`
And the following attributes for file attachments: `content`, `size`, `id`, `name`, `type`.
For example, to retrieve a one-time password from the one-time password field on a GitHub item:
op read "op://development/GitHub/Security/one-time password?attribute=otp"
See result...
359836
To get an SSH key's private key in the OpenSSH format, include the `ssh-format` query parameter with the value `openssh` on a secret reference for the SSH key's `private key` field.
op read "op://Private/ssh keys/ssh key/private key?ssh-format=openssh"
See result...
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABD3rRrf8J
ruD0CxZTYfpbTYAAAAEAAAAAEAAAAzAAAAC3NzaC1lZDI1NTE5AAAAIJ5B/GnxX6t9jMwQ
G7QE7r5daJLkMKTZhNZhWfvzK2y+AAAAkLgQAivYu/+12/YrZhK5keIAZf4ZgsZsZ2JI2q
qbx23PqgO93oGy1iCxXe3kngQL4cM6lwOZPsZPKCinkN6KxEr6RnXqFRHJbMpOiGeZhTuD
rjeo77HqFdxDqDeckB77XCKL0Ew28H5JlM/WO31XR3Z4VBAgTe+BQLjrFV8WU5UX38hpBJ
PMJyRsK72ZUDDaGQ==
-----END OPENSSH PRIVATE KEY-----
Learn more about [securely loading secrets into scripts](https://developer.1password.com/docs/cli/secrets-scripts/).
### With `op run`[​](https://developer.1password.com/docs/cli/secret-references/#with-op-run "Direct link to with-op-run")
You can set environment variables to secret references, then use [`op run`](https://developer.1password.com/docs/cli/reference/commands/run/) to pass secrets to an application or script at runtime.
`op run` scans environment variables for secret references, loads the corresponding values from 1Password, then runs the provided command in a subprocess with the secrets made available as environment variables for the duration of the subprocess.
When you reference a variable like `$MY_VAR` in the **same command** where you call `op run`, your shell expands `$MY_VAR` before `op run` can substitute the secret reference. To make sure `op run` substitutes the secret before the variable expands, you can either:
  * **Export the variable** as a secret reference before calling `op run`, or
  * Set the variable in the same command as `op run`, then **run the command to expand the variable in a subshell**. For example:
MY_VAR=op://vault/item/field op run --no-masking -- sh -c 'echo "$MY_VAR"'


#### Pass the secrets to an application or script[​](https://developer.1password.com/docs/cli/secret-references/#pass-the-secrets-to-an-application-or-script "Direct link to Pass the secrets to an application or script")
To pass secrets to your script or application at runtime, wrap the command with `op run`.
For example, here's a Node.js app that needs credentials to connect to a database:
$ node app.js
[INFO] Launching Node.js app...
[ERROR] Missing credentials DB_USER and DB_PASSWORD
[INFO] Exiting with code 1
You can set the `DB_USER` and `DB_PASSWORD` environment variables to secret references:
  * Bash, Zsh, sh
  * fish
  * PowerShell


export DB_USER="op://app-dev/db/user"
export DB_PASSWORD="op://app-dev/db/password"
set -x DB_USER="op://app-dev/db/user"
set -x DB_PASSWORD="op://app-dev/db/password"
$Env:DB_USER = "DB_USER=op://app-dev/db/user"
$Env:DB_PASSWORD = "DB_PASSWORD=op://app-dev/db/password"
Then use `op run` to pass the secrets to the `node app.js` command:
op run -- node app.js
[INFO] Launching Node.js app...
[DEBUG] ✔ Connected to db as user 'mydbuser' with password '<concealed by 1Password>'
#### Use with environment files[​](https://developer.1password.com/docs/cli/secret-references/#use-with-environment-files "Direct link to Use with environment files")
You can also use `op run` with environment files. To do this, use secret references instead of plaintext secrets in your environment file:
node.env
DB_USER="op://app-dev/db/user"
DB_PASSWORD="op://app-dev/db/password"
Then use `op run` with the `--env-file` flag:
op run --env-file="./node.env" -- node app.js
#### Print a secret with or without masking[​](https://developer.1password.com/docs/cli/secret-references/#print-a-secret-with-or-without-masking "Direct link to Print a secret with or without masking")
If a subprocess used with `op run` prints a secret to `stdout`, the secret will be concealed by default. You can include the `--no-masking` flag to print the value.
  * Bash, Zsh, sh
  * fish
  * PowerShell


To export an example environment variable `DB_PASSWORD` to a secret reference:
export DB_PASSWORD=op://app-prod/db/password
Use `op run` with the `printenv` command to print the concealed secret:
op run -- printenv DB_PASSWORD
See result...
<concealed by 1Password>
Include the `--no-masking` flag to print the actual secret:
op run --no-masking -- printenv DB_PASSWORD
See result...
fX6nWkhANeyGE27SQGhYQ
To export an example environment variable `DB_PASSWORD` to a secret reference:
set -x DB_PASSWORD=op://app-prod/db/password
Use `op run` with the `printenv` command to print the concealed secret:
op run -- printenv DB_PASSWORD
See result...
<concealed by 1Password>
Include the `--no-masking` flag to print the actual secret:
op run --no-masking -- printenv DB_PASSWORD
See result...
fX6nWkhANeyGE27SQGhYQ
To export an example environment variable `DB_PASSWORD` to a secret reference:
$Env:DB_PASSWORD = "DB_PASSWORD=op://app-prod/db/password"
To print the concealed secret:
op run -- powershell -c '$env:DB_PASSWORD'
See result...
<concealed by 1Password>
Include the `--no-masking` flag to print the actual secret:
op run --no-masking -- powershell -c '$env:DB_PASSWORD'
See result...
fX6nWkhANeyGE27SQGhYQ
Learn more about [loading secrets into the environment](https://developer.1password.com/docs/cli/secrets-environment-variables/) with `op run`, including how to use template variables to switch between different sets of secrets for different environments.
### With `op inject`[​](https://developer.1password.com/docs/cli/secret-references/#with-op-inject "Direct link to with-op-inject")
You can use [`op inject`](https://developer.1password.com/docs/cli/reference/commands/inject/) to replace secret references in a script or file with the secrets they reference.
By default, `op inject` accepts input on `stdin` and outputs on `stdout`. You can use the `--in-file` flag (or `-i`) to read the input from a file instead, and the `--out-file` flag (or `-o`) to specify where the ouput should be written.
To use `op inject` to resolve a secret in a simple command:
echo "here is my GitHub token: op://development/GitHub/credentials/personal_token" | op inject
See result...
here is my GitHub token: ghp_WzgPAEutsFRZH9uxWYtw
To write the output to a file `token.txt` in the current directory:
echo "here is my GitHub token: op://development/GitHub/credentials/personal_token" >> token.txt | op inject --out-file token.txt
token.txt
here is my GitHub token: ghp_WzgPAEutsFRZH9uxWYtw
#### Use with configuration files[​](https://developer.1password.com/docs/cli/secret-references/#use-with-configuration-files "Direct link to Use with configuration files")
You can use `op inject` to pass in a configuration file templated with secret references and output a configuration file that contains resolved secrets. Configuration files that use secret references instead of plaintext secrets can be safely checked into Git.
config.yml.tpl
database:
host: http://localhost
port: 5432
username: op://prod/mysql/username
password: op://prod/mysql/password
op inject --in-file config.yml.tpl --out-file config.yml
Learn more about [loading secrets into configuration files](https://developer.1password.com/docs/cli/secrets-config-files/) with `op inject`, including how to use template variables to switch between different sets of secrets for different environments.
## Learn more[​](https://developer.1password.com/docs/cli/secret-references/#learn-more "Direct link to Learn more")
  * [Secret reference syntax](https://developer.1password.com/docs/cli/secret-reference-syntax/)
  * [Load secrets into the environment](https://developer.1password.com/docs/cli/secrets-environment-variables/)
  * [Load secrets into config files](https://developer.1password.com/docs/cli/secrets-config-files/)
  * [Load secrets into scripts](https://developer.1password.com/docs/cli/secrets-scripts/)
  * [Use service accounts with 1Password CLI](https://developer.1password.com/docs/service-accounts/use-with-1password-cli)


### Was this page helpful?
YesNo
