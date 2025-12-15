---
title: "Item JSON template | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/item-template-json/"
captured: 2025-12-15
category: concepts
relevance:
  - secret retrieval
  - script integration
  - item management
  - vault management
keywords:
  - vault
  - item
  - field
  - op item
  - template
related: []
---

# Item JSON template | 1Password Developer

On this page
1Password CLI supports item JSON templates that you can use to take control of how you create items in 1Password. Item JSON templates allow you to [create an item with all of its details specified](https://developer.1password.com/docs/cli/item-create#with-an-item-json-template), including custom sections and fields.
Item templates are formatted similarly to the JSON output for [`op item get`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-get), so you can easily create new items based on existing items.
Each item category has its own template. You can get a list of all item categories with [`op item template list`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-template-list). And you can retrieve the template for an item category with [`op item template get <category>`](https://developer.1password.com/docs/cli/reference/management-commands/item#item-template-get).
## Item template keys[​](https://developer.1password.com/docs/cli/item-template-json/#item-template-keys "Direct link to Item template keys")
Item JSON templates have common language keys that allow you to identify how the fields in the template correspond to the item in 1Password.
{
"title": " ",
"category": " ",
"sections": [
{
"id": " ",
"label": " "
},
],
"fields": [
{
"id": " ",
"section": {
"id": " "
},
"type": " ",
"label": " ",
"value": " "
}
]
}
**Item**
Name | Description  
---|---  
title | The name of the item displayed in 1Password.  
category | The item's category.  
**Section**
Name | Description  
---|---  
id | The identifier for the section. If the item has multiple sections, each ID must be unique.  
label | The name of the section displayed in 1Password.  
To add a custom section, insert a section JSON object into the `sections` array.
View a section JSON object
{
"id": " ",
"label": " "
}
**Field**
Name | Description  
---|---  
id | The field's ID. Each ID should be unique. If left empty, 1Password will generate a random ID.  
section id | The ID of the section where the field is located. Only required if located in a custom section.  
type | The field's type. [Learn more about custom field types.](https://developer.1password.com/docs/cli/item-fields#custom-fields)  
label | The name of the field displayed in 1Password.  
value | The information saved in the field. Depending on its type, it can be a string, a secret, a number, or a date.  
To add a custom field to the template, insert a new field JSON object into the `fields` array.
View a field JSON object
{
"id": " ",
"section": {
"id": " "
},
"type": " ",
"label": " ",
"value": " "
}
## Example JSON representation[​](https://developer.1password.com/docs/cli/item-template-json/#example-json-representation "Direct link to Example JSON representation")
This is an item `mysql` in the 1Password app, and the same item represented in an item JSON template.
  * In the app
  * In the JSON template


![MySQL item in 1Password](https://developer.1password.com/img/cli/mysql-item.png)
{
"id": "4l3udxihvvuhszh2kxyjbblxl4",
"title": "mysql",
"version": 3,
"vault": {
"id": "uteieiwkhgv6hau7xkorejyvru"
},
"category": "DATABASE",
"last_edited_by": "IU2OKUBKAFGQPFPFZEG7X3NQ4U",
"created_at": "2021-11-25T14:50:14Z",
"updated_at": "2022-02-25T18:12:12Z",
"sections": [
{
"id": "g52gfotnw7nhnkgq477si2hmmi",
"label": "Database Owner"
}
],
"fields": [
{
"id": "notesPlain",
"type": "STRING",
"purpose": "NOTES",
"label": "notesPlain"
},
{
"id": "database_type",
"type": "MENU",
"label": "type",
"value": "mysql"
},
{
"id": "hostname",
"type": "STRING",
"label": "server",
"value": "http://localhost"
},
## Learn more[​](https://developer.1password.com/docs/cli/item-template-json/#learn-more "Direct link to Learn more")
  * [Create an item](https://developer.1password.com/docs/cli/item-create/)
  * [Work with items](https://developer.1password.com/docs/cli/reference/management-commands/item/)
  * [Work with vaults](https://developer.1password.com/docs/cli/reference/management-commands/vault/)


### Was this page helpful?
YesNo
