---
title: "Item fields | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/item-fields/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - item management
  - security patterns
  - ssh keys
keywords:
  - item
  - field
  - op item
  - template
  - ssh
  - ssh key
related: []
---

# Item fields | 1Password Developer

[Skip to main content](https://developer.1password.com/docs/cli/item-fields/#__docusaurus_skipToContent_fallback)
On this page
When you [use 1Password CLI to create items](https://developer.1password.com/docs/cli/item-create/), you can customize your items with [built-in](https://developer.1password.com/docs/cli/item-fields/#built-in-fields) and [custom](https://developer.1password.com/docs/cli/item-fields/#custom-fields) fields.
Learn how to [add built-in and custom fields to your items](https://developer.1password.com/docs/cli/item-create#create-a-customized-item) with either assignment statements or a JSON template.
## Built-in fields[​](https://developer.1password.com/docs/cli/item-fields/#built-in-fields "Direct link to Built-in fields")
Each item category includes a set of default fields, some of which may be specific to the category. You can identify available built-in fields by looking at the [JSON template](https://developer.1password.com/docs/cli/item-template-json/) for the item category:
op item template get <category>
View all categories
  * API Credential
  * Bank Account
  * Credit Card
  * Crypto Wallet
  * Database
  * Document
  * Driver License
  * Email Account
  * Identity
  * Login
  * Medical Record
  * Membership
  * Outdoor License
  * Passport
  * Password
  * Reward Program
  * Secure Note
  * Server
  * Social Security Number
  * Software License
  * SSH Key
  * Wireless Router


For example, the built-in fields available on a Login item are `username`, `password`, and `notesPlain`.
View a Login item JSON template
{
"title": "",
"category": "LOGIN",
"fields": [
{
"id": "username",
"type": "STRING",
"purpose": "USERNAME",
"label": "username",
"value": ""
},
{
"id": "password",
"type": "CONCEALED",
"purpose": "PASSWORD",
"label": "password",
"password_details": {
"strength": "TERRIBLE"
},
"value": ""
},
{
"id": "notesPlain",
"type": "STRING",
"purpose": "NOTES",
"label": "notesPlain",
"value": ""
}
]
}
When you use [assignment statements](https://developer.1password.com/docs/cli/item-create#with-assignment-statements) to assign built-in fields, use the `id` from the JSON template as the `field` in the assignment statement. Don't include a fieldType for built-in fields.
For example, to add a note to a Login item using an assignment statement:
'notesPlain=This is a note.'
## Custom fields[​](https://developer.1password.com/docs/cli/item-fields/#custom-fields "Direct link to Custom fields")
Custom fields can be added to any item, regardless of the item's category. Use the `fieldType` with [assignment statements](https://developer.1password.com/docs/cli/item-create#with-assignment-statements) and the `type` with an [item JSON template](https://developer.1password.com/docs/cli/item-create#with-an-item-json-template). Available custom field types are:
`fieldType` | `type` | description  
---|---|---  
`password` | `CONCEALED` | A concealed password.  
`text` | `STRING` | A text string.  
`email` | `EMAIL` | An email address.  
`url` | `URL` | A web address to copy or open in your default web browser, not used for autofill behavior. Use the `--url` flag to set the website where 1Password suggests and fills a Login, Password, or API Credential item.  
`date` | `DATE` | A date with the format `YYYY-MM-DD`.  
`monthYear` | `MONTH_YEAR` | A date with the format `YYYYMM` or `YYYY/MM`.  
`phone` | `PHONE` | A phone number.  
`otp` | `OTP` | A one-time password. Accepts an   
`file` | N/A | A file attachment. Accepts the path to the file as the value. Can only be added with [assignment statements](https://developer.1password.com/docs/cli/item-create#with-assignment-statements).  
## Learn more[​](https://developer.1password.com/docs/cli/item-fields/#learn-more "Direct link to Learn more")
  * [`op item` reference documentation](https://developer.1password.com/docs/cli/reference/management-commands/item/)
  * [Create an item](https://developer.1password.com/docs/cli/item-create/)
  * [Item JSON template](https://developer.1password.com/docs/cli/item-template-json/)


### Was this page helpful?
YesNo
  * [Built-in fields](https://developer.1password.com/docs/cli/item-fields/#built-in-fields)
  * [Custom fields](https://developer.1password.com/docs/cli/item-fields/#custom-fields)
  * [Learn more](https://developer.1password.com/docs/cli/item-fields/#learn-more)


