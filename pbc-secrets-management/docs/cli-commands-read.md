---
title: "1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/commands/read/"
captured: 2025-12-15
category: commands
relevance:
  - secret retrieval
  - vault management
  - ssh keys
keywords:
  - op://
  - vault
  - item
  - field
  - secret reference
  - op read
  - ssh
  - ssh key
related: []
---

# 1Password Developer

On this page
# read
Read the value of the field in 1Password specified by a secret reference.
[Learn more about secret references and query parameters.](https://developer.1password.com/docs/cli/secret-reference-syntax/)
op read <reference> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/commands/read/#flags "Direct link to Flags")
--file-mode filemode Set filemode for the output file. It is ignored without the --out-file flag. (default 0600)
-f, --force Do not prompt for confirmation.
-n, --no-newline Do not print a new line after the secret.
-o, --out-file string Write the secret to a file instead of stdout.
### Examples[​](https://developer.1password.com/docs/cli/reference/commands/read/#examples "Direct link to Examples")
Print the secret saved in the field `password`, on the item `db`, in the vault `app-prod`:
op read op://app-prod/db/password
Use a secret reference with a query parameter to retrieve a one-time password:
op read "op://app-prod/db/one-time password?attribute=otp"
Use a secret reference with a query parameter to get an SSH key's private key in the OpenSSH format:
op read "op://app-prod/ssh key/private key?ssh-format=openssh"
Save the SSH key found on the item `ssh` in the `server` vault as a new file `key.pem` on your computer:
op read --out-file ./key.pem op://app-prod/server/ssh/key.pem
Use `op read` in a command with secret references in place of plaintext secrets:
docker login -u $(op read op://prod/docker/username) -p $(op read op://prod/docker/password)
### Was this page helpful?
YesNo
