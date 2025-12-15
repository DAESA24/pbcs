---
title: "1Password CLI Template Syntax | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/secrets-template-syntax/"
captured: 2025-12-15
category: security
relevance:
  - secret retrieval
  - environment variables
  - vault management
keywords:
  - op://
  - vault
  - item
  - field
  - secret reference
  - environment variable
  - template
related: []
---

# 1Password CLI Template Syntax | 1Password Developer

On this page
# Template syntax
You can create a templated config file that contains [secret references](https://developer.1password.com/docs/cli/secret-reference-syntax/), then [use op inject](https://developer.1password.com/docs/cli/secrets-config-files/) to receive a resolved config file that contains the actual secrets.
Here's an example of a template file with enclosed secret references in place of the plaintext secrets:
config.yml.tpl
database:
host: localhost
port: 5432
username: {{ op://prod/database/username }}
password: {{ op://prod/database/password }}
## Secret references[​](https://developer.1password.com/docs/cli/secrets-template-syntax/#secret-references "Direct link to Secret references")
Secret references included in template files can be formatted as either [unenclosed secret references](https://developer.1password.com/docs/cli/secrets-template-syntax/#unenclosed-secret-references) or [enclosed secret references](https://developer.1password.com/docs/cli/secrets-template-syntax/#enclosed-secret-references).
### Unenclosed secret references[​](https://developer.1password.com/docs/cli/secrets-template-syntax/#unenclosed-secret-references "Direct link to Unenclosed secret references")
op://test-app/database/password
An unenclosed secret reference is a string that:
  * Begins with `op://` and is not preceded by any of the characters from: `alphanumeric`, `-`, `+` , `\`, `.`.
  * Ends with either the end of the template, or the first encountered character outside the following set: `alphanumeric`, `-`, `?`, `_`, `.`.


Examples of good and bad unenclosed secret references:
op://prod/docker-credentials/username
op://d3v/stripe.keys/s3ct10n/public_key
op://h?ack/1Password!/for"real
(contains special characters that are not supported by the syntax)
op://{vault}/[item]/(section)/field
(contains special characters that are not supported by the syntax)
### Enclosed secret references[​](https://developer.1password.com/docs/cli/secrets-template-syntax/#enclosed-secret-references "Direct link to Enclosed secret references")
{{ op://test-app/database/password }}
An enclosed secret reference is defined as any string that satisifies all of the following:
  * Begins with two closed braces `{{`
  * Ends with the two closed braces `}}`
  * Contains a valid unenclosed secret reference between the two pairs of braces, possibly padded with spaces


Examples of good and bad enclosed secret references:
{{op://prod/docker-credentials/username}}
{{ op://d3v/stripe.keys/s3ct10n/public_key }}
{{op://h?ack/1Password!/for"real}}
(the secret reference contains unsupported characters)
### Special characters[​](https://developer.1password.com/docs/cli/secrets-template-syntax/#special-characters "Direct link to Special characters")
If you need to escape special characters in your template, you can use curly braces and double quotes:
{{ "{{ test op://prod/docker-credentials/username }}" }}
will be resolved to
{{ test op://prod/docker-credentials/username }}
If the content contains double quotes, they must be escaped with `\`:
{{ "{{ test \"test\" test }}" }}
will be resolved to
{{ test "test" test }}
## Variables[​](https://developer.1password.com/docs/cli/secrets-template-syntax/#variables "Direct link to Variables")
The template syntax also supports variable tags:
  * `$var` (unenclosed variables)
  * `${var}` (enclosed variables)


When resolving an unenclosed variable of the form `$FOO`, it is replaced with the value of the environment variable named `FOO`.
When resolving an enclosed variable of the form `${FOO}`, any whitespace at the beginning or end of `FOO` is discarded and the reference is replaced with the value of the environment variable named `FOO`.
Variable names are case-insensitive, cannot start with a number, and can only contain letters, numbers, and underscores.
Examples of good and bad unenclosed variables:
$my_var
$mY_2nd_vAr
$2nd_var
(starts with a number)
$var-?notvar!
(contains unsupported special characters)
Examples of good and bad enclosed variables:
${my_var}
${ mY_2nd_vAr }
${my_var\\}
(the closing brace is escaped)
### Default values[​](https://developer.1password.com/docs/cli/secrets-template-syntax/#default-values "Direct link to Default values")
To set a default value for a template variable, use this syntax:
`${VAR_NAME:-<default-value>}`
The default value will be used when the variable can't be found in the environment.
For example, `op://${VAULT:-dev}/docker/password` evaluates to `op://dev/docker/password` when the `VAULT` environment variable isn't set. If `VAULT` is set to `prod` instead, it will evaluate to `op://prod/docker/password`.
## Learn more[​](https://developer.1password.com/docs/cli/secrets-template-syntax/#learn-more "Direct link to Learn more")
  * [Load secrets into config files](https://developer.1password.com/docs/cli/secrets-config-files/)
  * [Load secrets into the environment](https://developer.1password.com/docs/cli/secrets-environment-variables/)
  * [Secret reference syntax](https://developer.1password.com/docs/cli/secret-reference-syntax/)


### Was this page helpful?
YesNo
