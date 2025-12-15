---
title: "1Password app integration security | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/app-integration-security/"
captured: 2025-12-15
category: security
relevance:
  - environment variables
  - script integration
  - authentication
  - vault management
keywords:
  - biometric
  - authentication
  - session
related: []
---

# 1Password app integration security | 1Password Developer

**New!** You can now access secrets from [1Password Environments](https://developer.1password.com/docs/environments) on your device with a new [local .env file destination](https://developer.1password.com/docs/environments/local-env-file).
On this page
## Security model[​](https://developer.1password.com/docs/cli/app-integration-security/#security-model "Direct link to Security model")
[Integrating 1Password CLI with the 1Password app](https://developer.1password.com/docs/cli/app-integration/) allows you to use accounts you've added to the 1Password desktop app with 1Password CLI. Every time you use 1Password CLI in a new terminal window or tab, you'll be asked to authorize with biometrics. This authorization establishes a 10-minute session that automatically refreshes on each use.
1Password accounts can only be accessed through 1Password CLI after the user provides explicit biometric authorization and authorization is limited to an single account at a time. The user is shown a prompt containing the 1Password account display name (for example, `AgileBits` or `Wendy Appleseed's Family`) and the process being authorized (for example, `iTerm2` or `Terminal`). The user must confirm the prompt for 1Password CLI to be granted access to the requested account details.
Authorizing use of 1Password CLI while the 1Password app is locked will result in the 1Password app unlocking. When the 1Password app is locked, all prior authorization is revoked. Any new invocation of 1Password CLI will require new authorization. If a process is running at the moment authorization is revoked or expires, it will be able to finish its task and exit.
## Authorization model[​](https://developer.1password.com/docs/cli/app-integration-security/#authorization-model "Direct link to Authorization model")
Authorization in 1Password CLI occurs on a per-account basis. If you sign in to multiple accounts, each account must be authorized separately.
Authorization expires after 10 minutes of inactivity in the terminal session. There's a hard limit of 12 hours, after which you must reauthorize.
Each time you use a 1Password CLI command in a new terminal window or tab, you'll need to authorize your account again:
  * On macOS and Linux, authorization is confined to a terminal session but extends to sub-shell processes in that window.
  * On Windows, commands executed in a sub-shell require separate authorization.


## Accepted risks[​](https://developer.1password.com/docs/cli/app-integration-security/#accepted-risks "Direct link to Accepted risks")
  * A user or application with root/administrator level privileges on the same system may be able to circumvent one or more security measures and could obtain access to 1Password accounts through 1Password CLI without authorization if (and only if) the 1Password app is unlocked.
  * Applications that are granted accessibility permissions on macOS may be able to circumvent the authorization prompt.


## Technical design[​](https://developer.1password.com/docs/cli/app-integration-security/#technical-design "Direct link to Technical design")
### Session credentials[​](https://developer.1password.com/docs/cli/app-integration-security/#session-credentials "Direct link to Session credentials")
Session credentials are used to identify the terminal window or application where 1Password CLI is invoked. The goal is to restrict the granted authorization to a single terminal. If a user authorizes `account X` in one terminal window, using `account y` in another terminal window requires another approval from the user. These credentials don't consist of any sensitive or secret information.
  * Mac
  * Linux
  * Windows


The session credential for macOS is an ID that's based on the current `tty`, plus the start time. This way every session credential is unique, even after an ID gets reused.
The session credential for Linux is an ID that's based on the current `tty`, plus the start time. This way every session credential is unique, even after an ID gets reused.
The session credential for Windows is an ID that's based on the PID of the process that invokes 1Password CLI, plus the start time. This way every session credential is unique, even after an ID gets reused.
### How does 1Password CLI communicate with the 1Password app?[​](https://developer.1password.com/docs/cli/app-integration-security/#how-does-1password-cli-communicate-with-the-1password-app "Direct link to How does 1Password CLI communicate with the 1Password app?")
1Password CLI uses inter-process communication to reach out to the 1Password app to obtain access to the accounts stored in the app.
  * Mac
  * Linux
  * Windows


The `NSXPCConnection` XPC API is used for IPC. The 1Password app sets up a service (`1Password Browser Helper`) that acts as an XPC server. Both 1Password CLI and the 1Password app connect to this server. Authenticity of both is confirmed by verifying the code signature. The `1Password Browser Helper` acts as a message relay between the 1Password app and 1Password CLI.
1Password CLI connects to a Unix socket opened by the 1Password app. The socket is owned by the current user/group, allowing any process started by this user to connect to it. 1Password CLI is owned by the `onepassword-cli` group and has the `set-gid` bit set on Linux. The 1Password app verifies the authenticity of 1Password CLI by checking if the GID of the process connecting on the unix socket is equal to that of the `onepassword-cli` group. If the GID doesn't match, the connection is reset before any messages are accepted.
1Password CLI connects to a named pipe opened by the 1Password app. The app verifies the authenticity of the process connecting on the named pipe by verifying the Authenticode signature of the process's executable. 1Password CLI verifies the 1Password app's authenticity in the same way.
### Authorization prompts[​](https://developer.1password.com/docs/cli/app-integration-security/#authorization-prompts "Direct link to Authorization prompts")
The user is prompted for authorization to confirm that they actually want to allow an account to be accessible through 1Password CLI.
  * Mac
  * Linux
  * Windows


On macOS the OS's default biometrics prompt is used to request authorization, if available. Either TouchID or an Apple Watch can be used to confirm this prompt. If biometrics are not available a prompt confirming the user's device password is used instead.
On Linux, PolKit is used to spawn a prompt that includes an authentication challenge for the user (commonly fingerprint or the user's OS password).
On Windows, Windows Hello is used to spawn a prompt that includes an authentication challenge for the user (commonly fingerprint, face, or the user's OS password). Without Windows Hello, biometrics cannot be used with 1Password CLI.
### Was this page helpful?
YesNo
