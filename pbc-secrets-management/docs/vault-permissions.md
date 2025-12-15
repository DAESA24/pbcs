---
title: "About vault permissions | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/vault-permissions/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - item management
  - vault management
keywords:
  - vault
  - item
related: []
---

# About vault permissions | 1Password Developer

On this page
When using scripts to [grant or revoke vault permissions](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/), you must include any dependent permissions in the command.
The vault permissions available to you depend on your 1Password account type.
  * 1Password Business
  * 1Password Teams
  * 1Password Families


1Password Business includes the following permissions:
  * **view_items** : view items in a vault.
  * **create_items** : create items in a vault.
  * **edit_items** : edit items in a vault.
  * **archive_items** : archive items in a vault.
  * **delete_items** : delete items in a vault.
  * **view_and_copy_passwords** : view concealed passwords and copy them to the clipboard.
  * **view_item_history** : view and restore previous versions of items in the vault.
  * **import_items** : move or copy items into the vault.
  * **export_items** : save items in the vault to an unencrypted file that other apps can read.
  * **copy_and_share_items** : copy items between vaults, or share them outside of 1Password.
  * **print_items** : print the contents of items in the vault
  * **manage_vault** : allows a team member to grant and revoke access to the vault, change permissions for others, and delete the vault. Owners will always have permission to manage vaults.


1Password Business also includes the broader permissions available in 1Password Teams:
  * **allow_viewing** : view items in a vault, view concealed passwords and copy them to the clipboard. 
    * Includes the granular permissions: `view_items`, `view_and_copy_passwords`, `view_item_history`.
  * **allow_editing** : create, edit, move, print, copy, archive, and delete items in the vault. 
    * Includes the granular permissions: `create_items`, `edit_items`, `archive_items`, `delete_items`, `import_items`, `export_items`, `copy_and_share_items`, `print_items`.
  * **allow_managing** : grant and revoke access to the vault, change permissions for others, and delete the vault. Owners will always have permission to manage vaults. 
    * Includes the granular permission: `manage_vault`.


The vault permission `move_items` is automatically added when the permissions below are all added:
view_items, edit_items, archive_items, view_and_copy_passwords,
view_item_history, copy_and_share_items
In order to move an item, a user must have access to both the vault where an item is located and the destination vault.
**Permission dependencies**
In 1Password Business, all vault permissions have a hierarchical relationship in which narrower permissions require broader permissions to be granted alongside them. Permission dependencies are cumulative, so if a narrower permission is several levels down, it requires all of the broader permissions above it.
For example, to grant the narrower permission `delete_items` you must also grant the permissions `edit_items`, `view_and_copy_passwords`, and `view_items`.
Similarly, to revoke a broader permission like `view_items`, any narrower dependent permissions that have already been granted must be revoked alongside it.
![Vault permissions presented as a taxonomic tree](https://developer.1password.com/img/cli/vault-permissions.png)
permission | requirements  
---|---  
`create_items` | `view_items`  
`view_and_copy_passwords` | `view_items`  
`edit_items` |  `view_and_copy_passwords` , `view_items`  
`archive_items` |  `edit_items`, `view_and_copy_passwords`, `view_items`  
`delete_items` |  `edit_items`, `view_and_copy_passwords`, `view_items`  
`view_item_history` |  `view_and_copy_passwords`, `view_items`  
`import_items` |  `create_items`, `view_items`  
`export_items` |  `view_item_history`, `view_and_copy_passwords`, `view_items`  
`copy_and_share_items` |  `view_item_history`, `view_and_copy_passwords`, `view_items`  
`print_items` |  `view_item_history`, `view_and_copy_passwords`, `view_items`  
1Password Teams includes three permissions:
  * **allow_viewing** : view items in a vault, view concealed passwords and copy them to the clipboard. 
    * Includes the granular permissions: `view_items`, `view_and_copy_passwords`, `view_item_history`.
  * **allow_editing** : create, edit, move, print, copy, archive, and delete items in the vault. 
    * Includes the granular permissions: `create_items`, `edit_items`, `archive_items`, `delete_items`, `import_items`, `export_items`, `copy_and_share_items`, `print_items`.
  * **allow_managing** : grant and revoke access to the vault, change permissions for others, and delete the vault. Owners will always have permission to manage vaults. 
    * Includes the granular permission: `manage_vault`.


**Permission dependencies**
permission | requirements  
---|---  
`allow_editing` | `allow_viewing`  
`allow_managing` |   
To grant the permission `allow_editing`, you must also grant the broader permission `allow_viewing`. Similarly, to revoke `allow_viewing`, you must also revoke `allow_editing`.
1Password Families includes three permissions:
  * **allow_viewing** : view items in a vault, view concealed passwords and copy them to the clipboard. 
    * Includes the granular permissions: `view_items`, `view_and_copy_passwords`, `view_item_history`.
  * **allow_editing** : create, edit, move, print, copy, archive, and delete items in the vault. 
    * Includes the granular permissions: `create_items`, `edit_items`, `archive_items`, `delete_items`, `import_items`, `export_items`, `copy_and_share_items`, `print_items`.
  * **allow_managing** : grant and revoke access to the vault, change permissions for others, and delete the vault. Owners will always have permission to manage vaults. 
    * Includes the granular permission: `manage_vault`.


**Permission dependencies**
permission | requirements  
---|---  
`allow_editing` | `allow_viewing`  
`allow_managing` |   
To grant the permission `allow_editing`, you must also grant the broader permission `allow_viewing`. Similarly, to revoke `allow_viewing`, you must also revoke `allow_editing`.
## Learn more[​](https://developer.1password.com/docs/cli/vault-permissions/#learn-more "Direct link to Learn more")
  * [Grant and revoke vault permissions](https://developer.1password.com/docs/cli/grant-revoke-vault-permissions/)
  * [Work with vaults](https://developer.1password.com/docs/cli/reference/management-commands/vault/)


### Was this page helpful?
YesNo
