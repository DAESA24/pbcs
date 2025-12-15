---
title: "item | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/item/"
captured: 2025-12-15
category: concepts
relevance:
  - secret retrieval
  - environment variables
  - authentication
  - vault management
  - security patterns
keywords:
  - vault
  - item
  - field
  - op read
  - op item
  - environment variable
  - service account
  - template
  - ssh
  - ssh key
related: []
---

# item | 1Password CLI | 1Password Developer

On this page
# item
Perform CRUD operations on the 1Password items in your vaults.
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#subcommands "Direct link to Subcommands")
  * [item create](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-create): Create an item
  * [item delete](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-delete): Delete or archive an item
  * [item edit](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-edit): Edit an item's details
  * [item get](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-get): Get an item's details
  * [item list](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-list): List items
  * [item move](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-move): Move an item between vaults
  * [item share](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-share): Share an item
  * [item template](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-template): Manage templates


## item create[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-create "Direct link to item create")
Create a new item.
op item create [ - ] [ <assignment>... ] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-create-flags "Direct link to Flags")
--category category Set the item's category.
--dry-run Test the command and output a preview of the resulting item.
--favorite Add item to favorites.
--generate-password[=recipe] Add a randomly-generated password to a Login or Password item.
--reveal Don't conceal sensitive fields.
--ssh-generate-key The type of SSH key to create: Ed25519 or RSA. For RSA,
specify 2048, 3072, or 4096 (default) bits. Possible values:
ed25519, rsa, rsa2048, rsa3072, rsa4096. (default Ed25519)
--tags tags Set the tags to the specified (comma-separated)
values.
--template string Specify the filepath to read an item template from.
--title title Set the item's title.
--url URL Set the website where 1Password suggests and fills a Login, Password, or API Credential item.
--vault vault Save the item in this vault. Default: Private.
Get a list of all item categories:
op item template list
Use assignment statements or an item category JSON template to save details in built-in or custom fields.
[Learn more about creating items.](https://developer.1password.com/docs/cli/item-create/)
[Learn more about item fields and fieldTypes.](https://developer.1password.com/docs/cli/item-fields/)
#### Generate a password[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#generate-a-password "Direct link to Generate a password")
Use the `--generate-password` option to set a random password for a Login or Password item. The default is 32-characters, and includes upper and lowercase letters, numbers, and symbols (`!@.-_*`).
You can specify the password length (between 1 and 64 characters) and the character types to use:
--generate-password='letters,digits,symbols,32'
#### Set additional fields with assignment statements[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#set-additional-fields-with-assignment-statements "Direct link to Set additional fields with assignment statements")
You can use assignment statements as command arguments to set built-in and custom fields.
[<section>.]<field>[[<fieldType>]]=<value>
Command arguments get logged in your command history, and can be visible to other processes on your machine. If you’re assigning sensitive values, use a JSON template instead.
For example, to create a text field named "host" within a section named "Database Credentials", with the value set to 33.166.240.221:
DatabaseCredentials.host[text]=33.166.240.221
The section name is optional unless multiple sections contain fields with the same name.
Use a backslash to escape periods, equal signs, or backslashes in section or field names. Don’t use backslashes to escape the value.
You can omit spaces in the section or field name, or refer to the field by its JSON short name (`name` or `n`).
#### Create an item using a json template[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#create-an-item-using-a-json-template "Direct link to Create an item using a json template")
Use an item JSON template to assign sensitive values to an item. If you combine a template with assignment statements, assignment statements take precedence.
  1. Save the appropriate item category template to a file:
op item template get --out-file login.json "Login"
  2. Edit the template.
  3. Create a new item using the `-—template` flag to specify the path to the edited template:
op item create --template=login.json
  4. After 1Password CLI creates the item, delete the edited template.
You can also create an item from standard input using an item JSON template.
Pass the `-` character as the first argument, followed by any assignment statements.
op item template get Login | op item create --vault personal -
You can’t use both piping and the `--template` flag in the same command, to avoid collisions.


### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-create-examples "Direct link to Examples")
Create a Login item with a random password and website set using flags and custom and built-in fields set with assignment statements, including a one-time password field and a file attachment:
op item create --category=login --title='My Example Item' --vault='Test' \
--url https://www.acme.com/login \
--generate-password=20,letters,digits \
username=jane@acme.com \
'Test Section 1.Test Field3[otp]=otpauth://totp/<website>:<user>?secret=<secret>&issuer=<issuer>' \
'FileName[file]=/path/to/your/file'
Create an item by duplicating an existing item from another vault and modifying it with assignment statements:
op item get "My Item" --format json | op item create --vault prod - \
username="My Username" password="My Password"
Duplicate all items in a vault in one account to a vault in another account:
op item list --vault test-vault --format json --account agilebits | \
op item get --format json --account agilebits - | \
op item create --account work -
## item delete[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-delete "Direct link to item delete")
Permanently delete an item.
op item delete [{ <itemName> | <itemID> | <shareLink> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-delete-flags "Direct link to Flags")
--archive Move the item to the Archive.
--vault string Look for the item in this vault.
Use the `--archive` option to move it to the Archive instead.
An item may be specified by its name, ID, or sharing link.
#### Specify items on standard input[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#specify-items-on-standard-input "Direct link to Specify items on standard input")
The command treats each line of information on standard input (stdin) as an object specifier. Run `op help` to learn more about how to specify objects.
The input can also be a list or array of JSON objects. The command will get an item for any object that has an ID. This is useful for passing information from one `op` command to another.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-delete-examples "Direct link to Examples")
Permanently delete an item:
op item delete "Defunct Login"
Move an item to the Archive:
op item delete "Defunct Login" --archive
## item edit[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-edit "Direct link to item edit")
Edit an item's details.
op item edit { <itemName> | <itemID> | <shareLink> } [ <assignment> ... ] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-edit-flags "Direct link to Flags")
--dry-run Perform a dry run of the command and output a preview
of the resulting item.
--favorite Whether this item is a favorite item. Options: true, false.
--generate-password[=recipe] Give the item a randomly generated password.
--reveal Don't conceal sensitive fields.
--tags tags Set the tags to the specified (comma-separated)
values. An empty value will remove all tags.
--template string Specify the filepath to read an item template from.
--title title Set the item's title.
--url URL Set the website where 1Password suggests and fills a Login, Password, or API Credential item.
--vault vault Edit the item in this vault.
Specify the item by its name, ID, or sharing link. Use flags to update the title, tags, or generate a new random password.
You can use assignment statements as command arguments to update built-in or custom fields. For sensitive values, use a template instead.
#### Edit an item using assignment statements[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#edit-an-item-using-assignment-statements "Direct link to Edit an item using assignment statements")
Caution: Command arguments can be visible to other processes on your machine.
[<section>.]<field>[[<fieldType>]]=<value>
To create a new field or section, specify a field or section name that doesn’t already exist on the item.
To edit an existing field, specify the current section and field name, then make changes to the fieldType or value. If you don’t specify a fieldType or value, it will stay the same.
To delete a custom field, specify `[delete]` in place of the fieldType. If a section no longer has any fields, the section will also be deleted. You can't delete built-in fields, but you can set them to empty strings. Learn more about assignment statements: `op item create –-help`.
[Learn more about available fields and fieldTypes.](https://developer.1password.com/docs/cli/item-fields)
#### Edit an item using a template[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#edit-an-item-using-a-template "Direct link to Edit an item using a template")
JSON item templates do not support passkeys. If you use a JSON template to update an item that contains a passkey, the passkey will be overwritten. To fix this, you can [restore a previous version of the item](https://support.1password.com/item-history/).
You can use a JSON template to edit an item, alone or in combination with command arguments. Field assignment statements overwrite values in the template.
  1. Get the item you want to edit in JSON format and save it to a file:
op item get oldLogin --format=json > updatedLogin.json
  2. Edit the file.
  3. Use the `--template` flag to specify the path to the edited file and edit the item:
op item edit oldLogin --template=updatedLogin.json
  4. Delete the file.
You can also edit an item using piped input:
cat updatedLogin.json | op item edit oldLogin


To avoid collisions, you can't combine piped input and the `--template` flag in the same command.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-edit-examples "Direct link to Examples")
Add a 32-character random password that includes upper- and lower-case letters, numbers, and symbols to an item:
op item edit 'My Example Item' --generate-password='letters,digits,symbols,32'
Edit a custom field's value without changing the fieldType:
op item edit 'My Example Item' 'field1=new value'
Edit a custom field's fieldType without changing the value:
op item edit 'My Example Item' 'field1[password]'
Edit a custom field's type and value:
op item edit 'My Example Item' 'field1[monthyear]=2021/09'
Add a new custom field to an item:
op item edit 'My Example Item' 'section2.field5[phone]=1-234-567-8910'
Remove an existing custom field:
op item edit 'My Example Item' 'section2.field5[delete]'
Set the built-in username field to an empty value:
op item edit 'My Example Item' 'username='
Edit an item using a template alongside command arguments and assignment statements:
op item edit oldLogin --vault Private 'username=Lucky' --template=updatedLogin.json
## item get[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-get "Direct link to item get")
Get details about an item. Specify the item by its name, ID, or sharing link.
op item get [{ <itemName> | <itemID> | <shareLink> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-get-flags "Direct link to Flags")
--fields strings Return data from specific fields. Use `label=` to get the field by name or `type=` to filter fields by type. Specify multiple in a comma-separated list.
--include-archive Include items in the Archive. Can also be set using
OP_INCLUDE_ARCHIVE environment variable.
--otp Output the primary one-time password for this item.
--reveal Don't conceal sensitive fields.
--share-link Get a shareable link for the item.
--vault vault Look for the item in this vault.
If you have multiple items with the same name, or if you’re concerned about API rate limits, specify the item by its ID or limit the scope of the search with the `--vault` flag.
[Learn more about IDs and caching.](https://developer.1password.com/docs/cli/reference)
To retrieve the contents of a specific field, use `op read` instead. When using service accounts, you must specify a vault with the `--vault` flag or through piped input.
#### Specify items on standard input[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#specify-items-on-standard-input-1 "Direct link to Specify items on standard input")
`op item get` treats each line of information on standard input (stdin) as an object specifier.
You can also input a list or array of JSON objects, and the command will get an item for any object that has an ID key. This is useful for passing information from one command to another.
#### Items in the archive[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#items-in-the-archive "Direct link to Items in the archive")
Items in the Archive are ignored by default. To get details for an item in the Archive, specify the item by ID or use the `--include-archive` option.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-get-examples "Direct link to Examples")
Get details for all items with a specified tag:
op item list --tags documentation --format json | op item get -
Get a CSV list of the username, and password for all logins in a vault:
op item list --categories Login --vault Staging --format json | op item get - --fields label=username,label=password
Get a JSON object of an item's username and password fields:
op item get Netflix --fields label=username,label=password --format json
Get a list of fields by type:
op item get Netflix --fields type=concealed
Get an item's one-time password:
op item get Google --otp
Retrieve a shareable link for the item referenced by ID:
op item get kiramv6tpjijkuci7fig4lndta --vault "Ops Secrets" --share-link
## item list[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-list "Direct link to item list")
List items.
op item list [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-list-flags "Direct link to Flags")
--categories categories Only list items in these categories (comma-separated).
--favorite Only list favorite items.
--include-archive Include items in the Archive. Can also be set using
OP_INCLUDE_ARCHIVE environment variable.
--long Output a more detailed item list.
--tags tags Only list items with these tags (comma-separated).
--vault vault Only list items in this vault.
Returns a list of all items the account has read access to by default. Use flags to filter results. Excludes items in the Archive by default.
Categories are:
  * API Credential
  * Bank Account
  * Credit Card
  * Database
  * Document
  * Driver License
  * Email Account
  * Identity
  * Login
  * Membership
  * Outdoor License
  * Passport
  * Password
  * Reward Program
  * Secure Note
  * Server
  * Social Security Number
  * Software License
  * Wireless Router


### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-list-examples "Direct link to Examples")
Get details for all items with a specified tag:
op item list --tags documentation --format=json | op item get -
Get a CSV list of the username, and password for all logins in a vault:
op item list --categories Login --vault Staging --format=json | op item get - --fields username,password
Selecting a tag `<tag>` will also return items with tags sub-nested to `<tag>`. For example: `<tag/subtag>`.
## item move[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-move "Direct link to item move")
Move an item between vaults.
Moving an item creates a copy of the item in the destination vault and deletes the item from the current vault. As a result, the item gets a new ID.
op item move [{ <itemName> | <itemID> | <shareLink> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-move-flags "Direct link to Flags")
--current-vault string Vault where the item is currently saved.
--destination-vault string The vault you want to move the item to.
--reveal Don't conceal sensitive fields.
To restore or permanently delete the original item, find the item in Recently Deleted in your 1Password app or on 1Password.com.
Moving an item between vaults may change who has access to the item.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-move-examples "Direct link to Examples")
Move an item from the Private vault to the Shared vault:
op item move "My Example Item" --current-vault Private --destination-vault Shared
## item share[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-share "Direct link to item share")
Share an item.
op item share { <itemName> | <itemID> } [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-share-flags "Direct link to Flags")
--emails strings Email addresses to share with.
--expires-in duration Expire link after the duration specified in (s)econds,
(m)inutes, (h)ours, (d)ays, and/or (w)eeks. (default 7d)
--vault string Look for the item in this vault.
--view-once Expire link after a single view.
You can securely share copies of passwords and other items you've saved in 1Password with anyone, even if they don't use 1Password.
When you share an item, you'll get a unique link that you can send to others.
Copy the URL, then send the link to the person or people you want to share the item copy with, like in an email or text message. Anyone with the link can view the item copy unless you specify addresses with the emails flag.
If you edit an item, your changes won't be shared until you share the item again. Note that file attachments and Document items cannot be shared.
## item template[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-template "Direct link to item template")
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-template-subcommands "Direct link to Subcommands")
  * [item template get](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-template-get): Get an item template
  * [item template list](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-template-list): Get a list of templates


## item template get[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-template-get "Direct link to item template get")
Return a template for an item type.
op item template get [{ <category> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-template-get-flags "Direct link to Flags")
--file-mode filemode Set filemode for the output file. It is ignored without the --out-file flag. (default 0600)
-f, --force Do not prompt for confirmation.
-o, --out-file string Write the template to a file instead of stdout.
You can create a new item with a template. Run `op item create --help` for more information.
Categories are:
  * API Credential
  * Bank Account
  * Credit Card
  * Database
  * Document
  * Driver License
  * Email Account
  * Identity
  * Login
  * Membership
  * Outdoor License
  * Passport
  * Password
  * Reward Program
  * Secure Note
  * Server
  * Social Security Number
  * Software License
  * Wireless Router


## item template list[​](https://developer.1password.com/docs/cli/reference/management-commands/item/#item-template-list "Direct link to item template list")
Lists available item type templates.
op item template list [flags]
Use `op item template get <category>` to get a template.
### Was this page helpful?
YesNo
