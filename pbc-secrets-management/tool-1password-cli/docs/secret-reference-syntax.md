---
title: "1Password CLI Secret Reference Syntax | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/secret-reference-syntax/"
captured: 2025-12-15
category: security
relevance:
  - secret retrieval
  - environment variables
  - script integration
  - vault management
  - security patterns
keywords:
  - op://
  - vault
  - item
  - field
  - secret reference
  - op read
  - op item
  - environment variable
  - template
  - ssh
related: []
---

# 1Password CLI Secret Reference Syntax | 1Password Developer

On this page
# Secret reference syntax
![An environment file using a plaintext secret and the same file using a secret reference.](https://developer.1password.com/img/cli/use-case-secret-reference.png)
Secret reference URIs point to where a secret is saved in your 1Password account using the names (or [unique identifiers](https://developer.1password.com/docs/cli/reference#unique-identifiers-ids)) of the vault, item, section, and field where the information is stored.
op://<vault-name>/<item-name>/[section-name/]<field-name>
Secret references remove the risk of exposing plaintext secrets in your code and reflect changes you make in your 1Password account, so when you run a script you get the latest value.
You can use secret references with:
### 1Password CLI
Load secrets into environment variables, configuration files, and scripts.
[Learn more ](https://developer.1password.com/docs/cli/secret-references/)
### 1Password SDKs
Programmatically access your secrets with Go, JavaScript, and Python.
[Learn more ](https://developer.1password.com/docs/sdks/)
### Secrets Automation
Use secret references to secure your secrets management workflows.
[Learn more ](https://developer.1password.com/docs/secrets-automation/)
### VS Code
Create, preview, and read secret references in your code.
[Learn more ](https://developer.1password.com/docs/vscode/)
### 1Password integrations
Securely access your secrets in Kubernetes, CircleCI, GitHub Actions, Jenkins, Terraform, Pulumi, Postman, and more.
[Learn more ](https://developer.1password.com/docs/vscode/)
## Get secret references[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#get-secret-references "Direct link to Get secret references")
### With the 1Password desktop app[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#with-the-1password-desktop-app "Direct link to With the 1Password desktop app")
To see the option to copy secret references in the 1Password desktop app, first turn on the [integration with 1Password CLI](https://developer.1password.com/docs/cli/app-integration). Then:
  1. Open the item where the secret you want to reference is stored.
  2. Select **Copy Secret Reference**.


![An item in 1Password with the Copy Secret Reference option selected.](https://developer.1password.com/img/cli/copy-secret-reference.png)
### With 1Password for VS Code[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#with-1password-for-vs-code "Direct link to With 1Password for VS Code")
You can use 1Password for VS Code to [insert secret references](https://developer.1password.com/docs/vscode#get-values) from 1Password as you edit your code. First, [install the extension](https://developer.1password.com/docs/vscode/). Then:
  1. Open the 
  2. Enter `1Password: Get from 1Password`.
  3. Enter the item name or ID.
  4. Select the field to use.


### With 1Password CLI[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#with-1password-cli "Direct link to With 1Password CLI")
To get a secret reference with 1Password CLI, run [`op item get`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get) with the `--format json` flag and include the `--fields` flag to specify a field label. Then use 
op item get GitHub --format json --fields username | jq .reference
See result...
"op://development/GitHub/username"
To get secret references for every field on an item, use [`op item get`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get) with the `--format json` flag without specifying a field.
Example JSON output
op item get GitHub --format json
Each field object will include a `reference` key that contains its secret reference. For the example `GitHub` item, the output looks like this:
"fields": [
{
"id": "username",
"type": "STRING",
"purpose": "USERNAME",
"label": "username",
"value": "wendy_appleseed@agilebits.com",
"reference": "op://development/GitHub/username"
},
{
"id": "password",
"type": "CONCEALED",
"purpose": "PASSWORD",
"label": "password",
"value": "GADbhK6MjNZrRftGMqto",
"entropy": 115.5291519165039,
"reference": "op://development/GitHub/password",
"password_details": {
"entropy": 115,
"generated": true,
"strength": "FANTASTIC"
}
},
{
"id": "notesPlain",
"type": "STRING",
"purpose": "NOTES",
"label": "notesPlain",
"reference": "op://development/GitHub/notesPlain"
},
{
"id": "5ni6bw735myujqe4elwbzuf2ee",
"section": {
"id": "hv46kvrohfj75q6g45km2uultq",
"label": "credentials"
},
## Syntax rules[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#syntax-rules "Direct link to Syntax rules")
### Supported characters[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#supported-characters "Direct link to Supported characters")
Secret references are case-insensitive and support the following characters:
  * alphanumeric characters (`a-z`, `A-Z`, `0-9`)
  * `-`, `_`, `.` and the whitespace character


If a secret reference includes a whitespace, enclose the secret reference in quotation marks. For example:
op read "op://development/aws/Access Keys/access_key_id"
Any part of a secret reference that includes an unsupported character must be referred to by its [unique identifier (ID)](https://developer.1password.com/docs/cli/reference#unique-identifiers-ids) instead of its name.
To get an ID, run [`op item get`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get) with the output set to JSON. For example, to get the ID for a custom text field named `test/`:
op item get PagerDuty --fields label=test/ --format json
See result...
{
"id": "hu4vwo3bjkawq2uw2fkn5pkjzu",
"section": {
"id": "add more"
},
"type": "STRING",
"label": "text/",
"value": "t",
"reference": "op://Management/PagerDuty/add more/hu4vwo3bjkawq2uw2fkn5pkjzu"
}
### File attachments[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#file-attachments "Direct link to File attachments")
To reference a file attachment, use the file name in place of a field name:
op://vault-name/item-name/[section-name/]file-name
### Externally-set variables[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#externally-set-variables "Direct link to Externally-set variables")
If you use different sets of secrets in different environments, you can include variables within secret references and then set the variable to switch between secrets.
For example, the `APP_ENV` variable in the example below can be set to `dev` to load development credentials or `prod` to load production credentials, assuming the credentials are stored in 1Password vaults named `dev` and `prod`.
app.env
MYSQL_DATABASE = "op://$APP_ENV/mysql/database"
MYSQL_USERNAME = "op://$APP_ENV/mysql/username"
MYSQL_PASSWORD = "op://$APP_ENV/mysql/password"
Learn how to use variables to switch between sets of secrets in [environment files](https://developer.1password.com/docs/cli/secrets-environment-variables#step-3-differentiate-between-environments) and [config files](https://developer.1password.com/docs/cli/secrets-config-files#step-3-differentiate-between-environments).
### Field and file metadata attributes[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#field-and-file-metadata-attributes "Direct link to Field and file metadata attributes")
You can use secret references with query parameters to get more information about an item.
#### Attribute parameter[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#attribute-parameter "Direct link to Attribute parameter")
To get information about item fields and file attachments, use the `attribute` (or `attr`) query parameter.
Fields
op://<vault>/<item>[/<section>]/<field-name>?attribute=<attribute-value>
File attachments
op://<vault>/<item>[/<section>]/<file-name>?attribute=<attribute-value>
Field attributes:
Attribute | Definition  
---|---  
`type` | The field's type  
`value` | The field's content  
`id` | The field's unique identifier  
`purpose` | The designation of a built-in field (can be "username", "password", or "notes")  
`otp` | Use with one-time password fields to generate a one-time password code  
File attachment attributes:
Attribute | Definition  
---|---  
`type` | The field's type  
`content` | The file attachment's content  
`size` | The size of the file attachment  
`id` | The file attachment's unique identifier  
`name` | The name of the file attachment  
For example, to retrieve an item's one-time password code:
op read "op://development/GitHub/Security/one-time password?attribute=otp"
See result...
359836
To retrieve a field's type:
op read "op://Personal/aws/access credentials/username?attribute=type"
See result...
string
To retrieve the name of a file attachment:
op read "op://app-infra/ssh/key.pem?attribute=name"
See result...
key.pem
#### SSH format parameter[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#ssh-format-parameter "Direct link to SSH format parameter")
To get an SSH private key in the OpenSSH format, include the `ssh-format` query parameter with the value `openssh` on a secret reference for the SSH key's `private key` field.
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
## Secret reference examples[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#secret-reference-examples "Direct link to Secret reference examples")
### A field inside a section[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#a-field-inside-a-section "Direct link to A field inside a section")
To create a secret reference that refers to the PagerDuty email field, which is within the Admin section, use:
op://Management/PagerDuty/Admin/email
  * Management refers to the vault where the item is saved
  * PagerDuty refers to the item
  * Admin refers to the section where the field is a part of
  * email refers to the field where the secret you want to reference is located


![PagerDuty 1Password item](https://developer.1password.com/img/cli/pagerduty-light.png)
### A field without a section[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#a-field-without-a-section "Direct link to A field without a section")
To create a secret reference for the Stripe publishable-key field, which is not part of a section, use:
op://dev/Stripe/publishable-key
  * dev refers to the vault where the item is saved
  * Stripe refers to the item
  * publishable-key refers to the field where the secret you want to reference is located


![Stripe 1Password item](https://developer.1password.com/img/cli/stripe-light.png)
## Learn more[​](https://developer.1password.com/docs/cli/secret-reference-syntax/#learn-more "Direct link to Learn more")
  * [Use secret references with 1Password CLI](https://developer.1password.com/docs/cli/secret-references/)
  * [Get started with 1Password SDKs](https://developer.1password.com/docs/sdks/)
  * [Load secrets into config files](https://developer.1password.com/docs/cli/secrets-config-files/)
  * [Load secrets into the environment](https://developer.1password.com/docs/cli/secrets-environment-variables/)
  * [Template syntax](https://developer.1password.com/docs/cli/secrets-template-syntax/)


### Was this page helpful?
YesNo
