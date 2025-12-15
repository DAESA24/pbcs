---
title: "Create items with 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/item-create/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - authentication
  - item management
  - vault management
keywords:
  - vault
  - item
  - field
  - op item
  - op vault
  - template
related: []
---

# Create items with 1Password CLI | 1Password Developer

On this page
# Create items
To create a new item in your 1Password account and assign information to it, use the [`op item create`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-create) command.
You can [specify basic information about the item](https://developer.1password.com/docs/cli/item-create/#create-an-item) with flags and use assignment statements to [assign built-in and custom fields](https://developer.1password.com/docs/cli/item-create/#create-a-customized-item). To assign sensitive values, [use a JSON template](https://developer.1password.com/docs/cli/item-create/#with-an-item-json-template).
## Requirements[​](https://developer.1password.com/docs/cli/item-create/#requirements "Direct link to Requirements")
Before you can use 1Password CLI to create items, you'll need to:
  * [Sign up for 1Password](https://1password.com/pricing/password-manager)
  * [Install 1Password CLI](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli)


If you want to follow along with the examples in this guide, [sign in to your account](https://developer.1password.com/docs/cli/get-started#step-3-enter-any-command-to-sign-in) then create a new vault named `Tutorial` where the example items will be saved:
op vault create Tutorial
## Create an item[​](https://developer.1password.com/docs/cli/item-create/#create-an-item "Direct link to Create an item")
To create a new item, use [`op item create`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-create) and specify basic information about the item with flags.
For example, to create a Login item named `Netflix` in the `Tutorial` vault:
  * Bash, Zsh, sh, fish
  * PowerShell


op item create \
--category login \
--title "Netflix" \
--vault Tutorial \
--url 'https://www.netflix.com/login' \
--generate-password='letters,digits,symbols,32' \
--tags tutorial,entertainment
op item create `
--category login `
--title "Netflix" `
--vault Tutorial `
--url 'https://www.netflix.com/login' `
--generate-password='letters,digits,symbols,32' `
--tags tutorial,entertainment
Here's what each of the above flags does:
--category Sets the [item category](https://support.1password.com/item-categories/), in this case a Login item. Use `op item template list` to get a list of available categories. The category value is case-insensitive and ignores whitespace characters. For example, the `Social Security Number` category can also be specified as `socialsecuritynumber`.
--title Gives the item a name so that you can easily identify it. If unspecified, 1Password CLI selects a default name. For example, `Untitled Login item`.
--vault Specifies which [vault](https://support.1password.com/create-share-vaults/) the item should be created in. If unspecified, the item will be created in your built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault. The name of this vault varies depending on your account type.
--url Sets the website where 1Password suggests and fills a Login, Password, or API Credential item.
--generate-password Generates a strong password for Login and Password category items. You can specify a password recipe, as shown in the example. If left unspecified, a default recipe will be used to generate a 32-character password consisting of letters, digits, and symbols.
--tags Adds [tags](https://support.1password.com/favorites-tags/) to the item using a comma-separated list.
## Create a customized item[​](https://developer.1password.com/docs/cli/item-create/#create-a-customized-item "Direct link to Create a customized item")
Each item category has its own set of built-in fields that you can use to save more information to the item. You can also create custom fields to save additional details about the item.
Learn more about [built-in and custom fields](https://developer.1password.com/docs/cli/item-fields/).
You can assign built-in and custom fields to your item in two ways:
  * [With assignment statements](https://developer.1password.com/docs/cli/item-create/#with-assignment-statements)
  * [With an item JSON template](https://developer.1password.com/docs/cli/item-create/#with-an-item-json-template)


### With assignment statements[​](https://developer.1password.com/docs/cli/item-create/#with-assignment-statements "Direct link to With assignment statements")
Command arguments can be visible to other processes on your machine. If you're assigning sensitive values, use [an item JSON template](https://developer.1password.com/docs/cli/item-create/#with-an-item-json-template) instead.
The [`op item create`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-create) command can take a list of assignment statements as arguments to create fields on an item.
Assignment statements are formatted like this:
[<section>.]<field>[[<fieldType>]]=<value>
  * section (Optional) The name of the section where you want to create the field.
  * field The name of the field you want to create.
  * fieldType The type of field you want to create. If unspecified, `fieldType` will default to `password`.
  * value The information you want to save in the field.


For built-in fields, the field name should match the [built-in field `id`](https://developer.1password.com/docs/cli/item-fields#built-in-fields) in the item category template. Don't include a fieldType for built-in fields.
For custom fields, the fieldType should match the [custom field `type`](https://developer.1password.com/docs/cli/item-fields#custom-fields) you want to create. The field name can be anything you want.
If you need to use periods, equal signs, or backslashes in the name of a section or field, use a backslash character to escape them. Don't use backslashes to escape the value.
Here's an example of an assignment statement for the built-in field username on a Login item, set to 
'username=john.doe@acme.org'
And here's an example of an assignment statement for a custom field type titled date, which is set to 2022-12-31, in a field named Renewal Date within a section titled Subscription Info:
'Subscription Info.Renewal Date[date]=2022-12-31'
To add both of the above assignment statements to a new item, `HBO Max`, in the `Tutorial` vault:
  * Bash, Zsh, sh, fish
  * PowerShell


op item create \
--category login \
--title "HBO Max" \
--vault Tutorial \
--url 'https://www.hbomax.com' \
--generate-password='letters,digits,symbols,32' \
--tags tutorial,entertainment \
'username=john.doe@acme.org' \
'Subscription Info.Renewal Date[date]=2022-12-31'
op item create `
--category login `
--title "HBO Max" `
--vault Tutorial `
--url 'https://www.hbomax.com' `
--generate-password='letters,digits,symbols,32' `
--tags tutorial,entertainment `
'username=john.doe@acme.org' `
'Subscription Info.Renewal Date[date]=2022-12-31'
### With an item JSON template[​](https://developer.1password.com/docs/cli/item-create/#with-an-item-json-template "Direct link to With an item JSON template")
To assign sensitive values, fill out an item JSON template for the category of item you want to create. If you combine field assignment statements with a template, the assignment statements overwrite the template's values.
To see a list of available templates, run [`op item template list`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-template-list). To get a template for a category, run [`op item template get <category>`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-template-get).
For example, to create a new Login item using a template:
  1. Get the template for a Login item and save it in your current directory:
op item template get --out-file=login.json "Login"
  2. Edit [the template file](https://developer.1password.com/docs/cli/item-template-json/) to add your information.
  3. Create the item using the `--template` flag to specify the path to the template file:
op item create --template=login.json
This example template file creates a Login item named `Hulu` in a vault [specified by its ID](https://developer.1password.com/docs/cli/reference#unique-identifiers-ids). It specifies values for built-in `username`, `password`, and `notesPlain` fields. It also adds a custom `date` field.
Example Login template
login.json
{
"title": "Hulu",
"vault": {
"id": "sor33rgjjcg2xykftymcmqm5am"
},
"category": "LOGIN",
"fields": [
{
"id": "username",
"type": "STRING",
"purpose": "USERNAME",
"label": "username",
"value": "wendy.appleseed@gmail.com"
},
{
"id": "password",
"type": "CONCEALED",
"purpose": "PASSWORD",
"label": "password",
"password_details": {
"strength": ""
},
"value": "Dp2WxXfwN7VFJojENfEHLEBJmAGAxup@"
},
{
"id": "notesPlain",
"type": "STRING",
"purpose": "NOTES",
"label": "notesPlain",
"value": "This is Wendy's Hulu account."
},
{
"id": "date",
"type": "date",
"label": "Subscription renewal date",
"value": "2023-04-05"
  4. Delete the edited template file from your computer.


You can also create an item from standard input using a template:
op item template get Login | op item create --vault Tutorial -
## Create an item from an existing item[​](https://developer.1password.com/docs/cli/item-create/#create-an-item-from-an-existing-item "Direct link to Create an item from an existing item")
You can create a new item from an existing item by piping the item JSON from standard input.
For example, to create a new item based on the `HBO Max` item you created in the assignment statement section, with a new title, username, and password:
op item get "HBO Max" --format json | op item create --vault Tutorial --title "Wendy's HBO Max" - 'username=wendy.appleseed@acme.org' 'password=Dp2WxXfwN7VFJojENfEHLEBJmAGAxup@'
## Add a one-time password to an item[​](https://developer.1password.com/docs/cli/item-create/#add-a-one-time-password-to-an-item "Direct link to Add a one-time password to an item")
You can attach a [one-time password](https://support.1password.com/one-time-passwords/) to an item using a custom field [assignment statement](https://developer.1password.com/docs/cli/item-create/#with-assignment-statements). The `fieldType` should be `otp` and the `value` should be the 
  * Bash, Zsh, sh, fish
  * PowerShell


op item create \
--category login \
--title='My OTP Example' \
--vault Tutorial \
--url 'https://www.acme.com/login' \
--generate-password='letters,digits,symbols,32' \
--tags tutorial,entertainment \
'Test Section 1.Test Field3[otp]=otpauth://totp/<website>:<user>?secret=<secret>&issuer=<issuer>'
op item create `
--category login `
--title='My OTP Example' `
--vault Tutorial `
--url 'https://www.acme.com/login' `
--generate-password='letters,digits,symbols,32' `
--tags tutorial,entertainment `
'Test Section 1.Test Field3[otp]=otpauth://totp/<website>:<user>?secret=<secret>&issuer=<issuer>'
## Attach a file to an item[​](https://developer.1password.com/docs/cli/item-create/#attach-a-file-to-an-item "Direct link to Attach a file to an item")
You can attach a file to an item using a custom field [assignment statement](https://developer.1password.com/docs/cli/item-create/#with-assignment-statements). The `field` should be the name the file will have in 1Password, the `fieldType` should be `file`, and the `value` should be the path to the file.
myFileName[file]=/path/to/your/file
The file in the above example will be named `myFileName`. To preserve the original file name, you can omit the `field`:
[file]=/path/to/your/file
Here's what an example `PlayStation Store` login would look like with the file `/wendyappleseed/documents/receipt.png` attached, named `JanuaryReceipt`.
  * Bash, Zsh, sh, fish
  * PowerShell


op item create \
--category login \
--title "PlayStation Store" \
--vault Tutorial \
--url 'https://store.playstation.com/' \
--generate-password='letters,digits,symbols,32' \
--tags tutorial,entertainment \
'JanuaryReceipt[file]=/wendyappleseed/documents/receipt.png'
op item create `
--category login `
--title "PlayStation Store" `
--vault Tutorial `
--url 'https://store.playstation.com/' `
--generate-password='letters,digits,symbols,32' `
--tags tutorial,entertainment `
'JanuaryReceipt[file]=/wendyappleseed/documents/receipt.png'
## Next steps[​](https://developer.1password.com/docs/cli/item-create/#next-steps "Direct link to Next steps")
If you want to continue learning about item management, keep the example items you created and move on to the [edit items](https://developer.1password.com/docs/cli/item-edit) tutorial.
If you created a Tutorial vault and don't want to continue on, you can delete the vault and the examples items you created by running:
op vault delete "Tutorial"
## Learn more[​](https://developer.1password.com/docs/cli/item-create/#learn-more "Direct link to Learn more")
  * [`op item create` reference documentation](https://developer.1password.com/docs/cli/reference/management-commands/item#item-create)
  * [Built-in and custom item fields](https://developer.1password.com/docs/cli/item-fields)
  * [Item JSON template](https://developer.1password.com/docs/cli/item-template-json)


### Was this page helpful?
YesNo
