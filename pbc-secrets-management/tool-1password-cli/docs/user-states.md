---
title: "User states | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/user-states/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
keywords:
  - 1password-cli
related: []
---

# User states | 1Password Developer

When you fetch information about users with [`op user list`](https://developer.1password.com/docs/cli/reference/management-commands/user#user-list) or [`op user get`](https://developer.1password.com/docs/cli/reference/management-commands/user#user-get), 1Password CLI returns each person's current account state.
User state | Description  
---|---  
`ACTIVE` | The user is active.  
`RECOVERY_STARTED` |  [Account recovery](https://developer.1password.com/docs/cli/recover-users) has been started for the user.  
`RECOVERY_ACCEPTED` | The user has created their new account password and is waiting to be [confirmed again by an administrator](https://support.1password.com/recovery#complete-recovery).  
`SUSPENDED` | The user is suspended.  
`TRANSFER_STARTED` | The user has been provisioned, but hasn't set up their account.  
`TRANSFER_SUSPENDED` | The user was provisioned and didn't set up their account before they were deprovisioned.  
### Was this page helpful?
YesNo
