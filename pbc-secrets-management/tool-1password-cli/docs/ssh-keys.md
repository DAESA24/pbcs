---
title: "Manage SSH keys | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/ssh-keys/"
captured: 2025-12-15
category: concepts
relevance:
  - secret retrieval
  - authentication
  - vault management
  - ssh keys
keywords:
  - op://
  - vault
  - item
  - field
  - secret reference
  - op read
  - op item
  - ssh
  - ssh key
related: []
---

# Manage SSH keys | 1Password Developer

On this page
## Requirements[​](https://developer.1password.com/docs/cli/ssh-keys/#requirements "Direct link to Requirements")
Before you can use 1Password CLI to manage your SSH keys, you'll need to:
  * [Sign up for 1Password](https://1password.com/pricing/password-manager).
  * [Install 1Password CLI](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli) (`2.20.0` or later).


## Generate an SSH key[​](https://developer.1password.com/docs/cli/ssh-keys/#generate-an-ssh-key "Direct link to Generate an SSH key")
You can use [`op item create`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-create) with the `ssh` item category to generate a new SSH key. To import an existing SSH key, [use the 1Password desktop app](https://developer.1password.com/docs/ssh/manage-keys#import-an-ssh-key).
op item create --category ssh --title "My SSH Key"
1Password CLI generates an SSH key and saves it as a new item in your built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault, then prints the key to stdout with the private key redacted. The item includes the key type, private key, public key, and its fingerprint.
By default, 1Password CLI creates an Ed25519 key. To create an RSA key instead, use the `--ssh-generate-key` flag to specify `RSA`. Include the number of bits to specify a custom size: 2048, 3072 or 4096 (default).
For example, to generate a 2048-bit RSA key:
op item create --category ssh --title "RSA SSH Key" --ssh-generate-key RSA,2048
## Get a private key[​](https://developer.1password.com/docs/cli/ssh-keys/#get-a-private-key "Direct link to Get a private key")
To get an SSH key's private key, use [`op read`](https://developer.1password.com/docs/cli/reference/commands/read/) with a [secret reference](https://developer.1password.com/docs/cli/secret-reference-syntax/) for the item's `private key` field. Include the `ssh-format` query parameter with `openssh` to get the private key in the OpenSSH format.
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
## Learn more[​](https://developer.1password.com/docs/cli/ssh-keys/#learn-more "Direct link to Learn more")
  * [Supported SSH key types](https://developer.1password.com/docs/ssh/manage-keys#supported-ssh-key-types)
  * [Use 1Password for SSH & Git](https://developer.1password.com/docs/ssh/)
  * [Manage your SSH keys in the 1Password app](https://developer.1password.com/docs/ssh/manage-keys/)
  * [Sign your Git commits with SSH](https://developer.1password.com/docs/ssh/git-commit-signing/)


### Was this page helpful?
YesNo
