---
title: "Edit items with 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/item-edit/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - item management
  - vault management
  - ssh keys
keywords:
  - vault
  - item
  - field
  - op item
  - op vault
  - template
  - ssh
  - ssh key
related: []
---

# Edit items with 1Password CLI | 1Password Developer

On this page
# Edit items
To edit an existing item in your 1Password account, use the [`op item edit`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-edit) command.
You can [edit basic information about the item](https://developer.1password.com/docs/cli/item-edit/#edit-an-items-basic-information) with flags and use assignment statements to [edit an item's built-in and custom fields](https://developer.1password.com/docs/cli/item-edit/#edit-built-in-and-custom-fields). To edit sensitive values, [use a JSON template](https://developer.1password.com/docs/cli/item-edit/#edit-an-item-using-a-json-template).
You can't use `op item edit` to edit SSH keys. Learn more about [managing SSH keys](https://developer.1password.com/docs/cli/ssh-keys) with 1Password CLI.
## Requirements[​](https://developer.1password.com/docs/cli/item-edit/#requirements "Direct link to Requirements")
Before you can use 1Password CLI to edit items, you'll need to:
  * [Sign up for 1Password](https://1password.com/pricing/password-manager)
  * [Install 1Password CLI](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli)


If you want to follow along with the examples in this guide, [create the example items in the guide to creating items](https://developer.1password.com/docs/cli/item-create) first.
## Edit an item's basic information[​](https://developer.1password.com/docs/cli/item-edit/#edit-an-items-basic-information "Direct link to Edit an item's basic information")
To edit an item, use [`op item edit`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-edit) and specify the item by name, [unique identifier (ID)](https://developer.1password.com/docs/cli/reference#unique-identifiers-ids), or sharing link.
You can use flags to generate a new password and edit an item's title, vault, or tags. You can also change the website where 1Password suggests and fills a Login, Password, or API Credential item.
For example, to change the name of the example item `Netflix`, move it from the `Tutorial` vault to the `Private` vault, update its tags, edit its website, and generate a new random password:
  * Bash, Zsh, sh, fish
  * PowerShell


op item edit "Netflix" \
--title "Edited Netflix" \
--vault Private \
--tags tutorial \
--url https://www.netflix.com \
--generate-password='letters,digits,symbols,32'
op item edit "Netflix" `
--title "Edited Netflix" `
--vault Private `
--tags tutorial `
--url https://www.netflix.com `
--generate-password='letters,digits,symbols,32'
To change the example item name back to `Netflix` and move it back to the `Tutorial` vault:
  * Bash, Zsh, sh, fish
  * PowerShell


op item edit "Edited Netflix" \
--title "Netflix" \
--vault Tutorial
op item edit "Edited Netflix" `
--title "Netflix" `
--vault Tutorial
## Edit built-in and custom fields[​](https://developer.1password.com/docs/cli/item-edit/#edit-built-in-and-custom-fields "Direct link to Edit built-in and custom fields")
Command arguments can be visible to other processes on your machine. To edit sensitive values, use [an item JSON template](https://developer.1password.com/docs/cli/item-edit/#edit-an-item-using-a-json-template) instead.
The `op item edit` command can take a list of assignment statements as arguments to edit an item's [built-in and custom fields](https://developer.1password.com/docs/cli/item-fields).
[<section>.]<field>[[<fieldType>]]=<value>
  * section (Optional) The name of the section where the field is saved.
  * field The name of the field.
  * fieldType The type of field. If unspecified, the fieldType stays the same.
  * value The information you want to save in the field. If unspecified, the value stays the same.


For example, to change the subscription renewal date on the `HBO Max` item:
  * Bash, Zsh, sh, fish
  * PowerShell


op item edit "HBO Max" \
'Renewal Date=2023-5-15'
op item edit "HBO Max" `
'Renewal Date=2023-5-15'
### Delete a custom field[​](https://developer.1password.com/docs/cli/item-edit/#delete-a-custom-field "Direct link to Delete a custom field")
To delete a custom field, specify `[delete]` in place of the fieldType. If you remove all the fields in a section, the section is also removed. You can't delete empty fields, but you can set them to empty strings.
To use an assignment statement to delete the subscription renewal date on the example `HBO Max` item:
  * Bash, Zsh, sh, fish
  * PowerShell


op item edit "HBO Max" \
'Renewal Date[delete]=2023-5-15'
op item edit "HBO Max" `
'Renewal Date[delete]=2023-5-15'
## Edit an item using a JSON template[​](https://developer.1password.com/docs/cli/item-edit/#edit-an-item-using-a-json-template "Direct link to Edit an item using a JSON template")
JSON item templates do not support passkeys. If you use a JSON template to update an item that contains a passkey, the passkey will be overwritten. To fix this, you can [restore a previous version of the item](https://support.1password.com/item-history/).
To edit sensitive values on an item, use an [item JSON template](https://developer.1password.com/docs/cli/item-template-json).
  1. Get the JSON output for the item you want to edit and save it to a file.
op item get <item> --format json > newItem.json
If you prefer to start over, you can get a blank template for the item's category with [`op item template get`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-template-get).
  2. Edit the file.
  3. Use the `--template` flag to specify the path to the edited file and apply the changes to the item:
op item edit <item> --template=newItem.json
  4. Delete the file.


You can also edit an item using piped input:
cat newItem.json | op item edit <item>
To avoid collisions, you can't combine piped input and the `--template` flag in the same command.
## Next steps[​](https://developer.1password.com/docs/cli/item-edit/#next-steps "Direct link to Next steps")
If you created a Tutorial vault, you can delete the vault and the examples items you created:
op vault delete "Tutorial"
## Learn more[​](https://developer.1password.com/docs/cli/item-edit/#learn-more "Direct link to Learn more")
  * [`op item` reference documentation](https://developer.1password.com/docs/cli/reference/management-commands/item)
  * [Built-in and custom item fields](https://developer.1password.com/docs/cli/item-fields)
  * [Item JSON template](https://developer.1password.com/docs/cli/item-template-json)


### Was this page helpful?
YesNo
