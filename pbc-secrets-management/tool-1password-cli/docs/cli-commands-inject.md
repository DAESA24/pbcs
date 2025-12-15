---
title: "inject | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/commands/inject/"
captured: 2025-12-15
category: commands
relevance:
  - secret retrieval
  - environment variables
keywords:
  - op://
  - secret reference
  - template
related: []
---

# inject | 1Password CLI | 1Password Developer

On this page
# inject
Inject secrets into a file templated with secret references.
op inject [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/commands/inject/#flags "Direct link to Flags")
--file-mode filemode Set filemode for the output file. It is ignored without the --out-file flag. (default 0600)
-f, --force Do not prompt for confirmation.
-i, --in-file string The filename of a template file to inject.
-o, --out-file string Write the injected template to a file instead of stdout.
[Learn more about secret references.](https://developer.1password.com/docs/cli/secret-references)
You can pass in a config file templated with secret references and receive a config file with the actual secrets substituted. Make sure to delete the resolved file when you no longer need it.
[Learn more about loading secrets into config files.](https://developer.1password.com/docs/cli/secrets-config-files)
### Examples[​](https://developer.1password.com/docs/cli/reference/commands/inject/#examples "Direct link to Examples")
Inject secrets into a config template from stdin:
echo "db_password: {{ op://app-prod/db/password }}" | op inject
db_password: fX6nWkhANeyGE27SQGhYQ
Inject secrets into a config template file:
cat config.yml.tpl
db_password: {{ op://app-prod/db/password }}
op inject -i config.yml.tpl -o config.yml && cat config.yml
db_password: fX6nWkhANeyGE27SQGhYQ
Multiple secrets can be concatenated:
echo "db_url: postgres://{{ op://lcl/db/user }}:{{ op://lcl/db/pw }}@{{ op://lcl/db/host }}:{{ op://lcl/db/port }}/{{ op://my-app-prd/db/db }}" | op inject
db_url: postgres://admin:admin@127.0.0.1:5432/my-app"
Use variables in secret references to switch between different sets of secrets for different environments:
echo "db_password: op://$env/db/password" | env=prod op inject
db_password: fX6nWkhANeyGE27SQGhYQ
### Was this page helpful?
YesNo
