---
title: "1Password Developer"
source_url: "https://developer.1password.com/docs/cli/reference/management-commands/events-api/"
captured: 2025-12-15
category: concepts
relevance:
  - authentication
keywords:
  - item
related: []
---

# 1Password Developer

On this page
# events-api
Manage Events API integrations in your 1Password account. Requires a business account.
### Subcommands[​](https://developer.1password.com/docs/cli/reference/management-commands/events-api/#subcommands "Direct link to Subcommands")
  * [events-api create](https://developer.1password.com/docs/cli/reference/management-commands/events-api/#events-api-create): Set up an integration with the Events API


## events-api create[​](https://developer.1password.com/docs/cli/reference/management-commands/events-api/#events-api-create "Direct link to events-api create")
Create an Events API integration token.
op events-api create <name> [flags]
### Flags[​](https://developer.1password.com/docs/cli/reference/management-commands/events-api/#events-api-create-flags "Direct link to Flags")
--expires-in duration Set how the long the events-api token is valid for in
(s)econds, (m)inutes, (h)ours, (d)ays, and/or (w)eeks.
--features features Set the comma-separated list of features the integration
token can be used for. Options: `signinattempts`,
`itemusages`, `auditevents`.
1Password CLI prints the token when successful.
Requires a business account.
### Examples[​](https://developer.1password.com/docs/cli/reference/management-commands/events-api/#events-api-create-examples "Direct link to Examples")
Create an Events API integration to report sign-in attempts that expires in one hour:
op events-api create SigninEvents --features signinattempts --expires-in 1h
Create an Events API integration that reports all supported events that does not expire:
op events-api create AllEvents
### Was this page helpful?
YesNo
