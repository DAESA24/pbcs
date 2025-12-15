---
title: "document | 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/document/"
captured: 2025-12-15
category: concepts
relevance:
  - environment variables
  - authentication
  - vault management
keywords:
  - vault
  - item
  - environment variable
related: []
---

# document | 1Password CLI | 1Password Developer

On this page
# document
Perform CRUD operations on Document items in your vaults.
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#subcommands "Direct link to Subcommands")
  * [document create](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-create): Create a document item
  * [document delete](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-delete): Delete or archive a document item
  * [document edit](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-edit): Edit a document item
  * [document get](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-get): Download a document
  * [document list](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-list): Get a list of documents


## document create[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-create "Direct link to document create")
Create a document item and receive a JSON object that contains the item's ID.
op document create [{ <file> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-create-flags "Direct link to Flags")
--file-name name Set the file's name.
--tags tags Set the tags to the specified (comma-separated) values.
--title title Set the document item's title.
--vault vault Save the document in this vault. Default: Private.
By default, the document is saved in your built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault. Specify a different vault with the `--vault` option.
#### Create a file from standard input[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#create-a-file-from-standard-input "Direct link to Create a file from standard input")
To create the file contents from standard input (stdin), enter a hyphen (`-`) instead of a path. You can use the `--file-name` option to change the name of the file.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-create-examples "Direct link to Examples")
Create a document by specifying the file path:
op document create "../demos/videos/demo.mkv" --title "2020-06-21 Demo Video"
Create a document from standard input:
cat auth.log.* | op document create - --title "Authlogs 2020-06" --file-name "auth.log.2020.06"
## document delete[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-delete "Direct link to document delete")
Permanently delete a document. Specify the document to delete by its name or ID. Use the `--archive` option to move it to the Archive instead.
op document delete [{ <itemName> | <itemID> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-delete-flags "Direct link to Flags")
--archive Move the document to the Archive.
--vault vault Delete the document in this vault.
#### Specify items on standard input[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#specify-items-on-standard-input "Direct link to Specify items on standard input")
The command treats each line of information on standard input (stdin) as an object specifier. Run `op help` to learn more about how to specify objects.
You can also input a list or array of JSON objects. The command will get an item for any object that has an ID. This is useful for passing information from one `op` command to another.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-delete-examples "Direct link to Examples")
Permanently delete a document:
op document delete "2019 Contracts"
Move a document to the Archive:
op document delete "2019 Contracts" --archive
## document edit[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-edit "Direct link to document edit")
Edit a document item. Specify the document item to edit by its name or ID.
op document edit { <itemName> | <itemID> } [{ <file> | - }] [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-edit-flags "Direct link to Flags")
--file-name name Set the file's name.
--tags tags Set the tags to the specified (comma-separated) values. An empty
value removes all tags.
--title title Set the document item's title.
--vault vault Look up document in this vault.
Replaces the file contents of a Document item with the provided file or with the information on standard input (stdin).
#### Update a file from standard input[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#update-a-file-from-standard-input "Direct link to Update a file from standard input")
To update the file contents from standard input (stdin), enter a hyphen (`-`) instead of a path. You can use the `--file-name` option to change the name of the file.
## document get[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-get "Direct link to document get")
Download a document and print the contents. Specify the document by its name or ID.
op document get { <itemName> | <itemID> } [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-get-flags "Direct link to Flags")
--file-mode filemode Set filemode for the output file. It is ignored without the --out-file flag. (default 0600)
--force Forcibly print an unintelligible document to an interactive terminal. If --out-file is specified, save the document to a file without prompting for confirmation.
--include-archive Include document items in the Archive. Can also be set using OP_INCLUDE_ARCHIVE environment variable.
-o, --out-file path Save the document to the file path instead of stdout.
--vault vault Look for the document in this vault.
Prints to standard output (stdout) by default. To print to a file, use the `--out-file path/to/file.ext` flag.
#### Save to a file[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#save-to-a-file "Direct link to Save to a file")
Use the `--out-file` option to have `op` save the document. This may be useful in some shells as a way to preserve the file's original encoding.
The `--out-file` option won't overwrite an existing file. The destination path must be an empty file or not exist.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-get-examples "Direct link to Examples")
Save a document to a file called `secret-plans.text`:
op document get "Top Secret Plan B" --out-file=../documents/secret-plans.text
## document list[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-list "Direct link to document list")
List documents.
op document list [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/document/#document-list-flags "Direct link to Flags")
--include-archive Include document items in the Archive. Can also be set using
OP_INCLUDE_ARCHIVE environment variable.
--vault vault Only list documents in this vault.
Returns a list of all documents the account has read access to by default. Excludes items in the Archive by default.
### Was this page helpful?
YesNo
