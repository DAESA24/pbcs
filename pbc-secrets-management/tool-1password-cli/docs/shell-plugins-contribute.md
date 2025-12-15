---
title: "Build your own shell plugins (beta) | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/contribute/"
captured: 2025-12-15
category: integrations
relevance:
  - environment variables
  - script integration
  - authentication
  - vault management
keywords:
  - item
  - field
  - environment variable
  - template
  - authentication
related: []
---

# Build your own shell plugins (beta) | 1Password Developer

On this page
If you don't see your favorite command-line tool [listed in the 1Password Shell Plugin registry](https://developer.1password.com/docs/cli/shell-plugins/), you can write your own plugin.
1Password CLI allows you to build and test shell plugins locally, so you can add support for authenticating your favorite CLI using a credential you saved in 1Password.
If you want to make your plugin available to others, you can 
## Requirements[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#requirements "Direct link to Requirements")
  * [Sign up for 1Password](https://1password.com/pricing/password-manager).
  * Install and sign in to 1Password for [Mac](https://1password.com/downloads/mac) or [Linux](https://1password.com/downloads/linux).
  * Install [1Password CLI](https://developer.1password.com/docs/cli/get-started/) and turn on the [desktop app integration](https://developer.1password.com/docs/cli/get-started#step-2-turn-on-the-1password-desktop-app-integration).
  * Install 
  * Install 
  * Install 


## Concepts[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#concepts "Direct link to Concepts")
A 1Password Shell Plugin should describe the following:
  * The **credential** offered by a platform
  * The CLI or **executable** offered by a platform
  * How the credential should be **provisioned** for the respective CLI to authenticate
  * Which commands for the respective CLI **need authentication**
  * How credentials stored on the local filesystem can be **imported** into 1Password


Shell plugins are written in Go and consist of a set of Go structs in a package that together make up the plugin for a certain platform, service, or product. Don't worry if you're not a Go expert – there are 
## Step 1: Use the plugin template[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#step-1-use-the-plugin-template "Direct link to Step 1: Use the plugin template")
First, clone or fork the 
To get started with those, use the following Makefile command:
make new-plugin
You'll be prompted to enter the following information:
  * **Plugin name:** Lowercase identifier for the platform, e.g. `aws`, `github`, `digitalocean`, `azure`. This will also be used as the name of the Go package.
  * **Plaform display name:** The display name of the platform, e.g `AWS`, `GitHub`, `DigitalOcean`, `Azure`.
  * **Credential name:** The credentials the platform offers, e.g. `Personal Access Token`, `API Key`, `Auth Token`.
  * **Executable name:** The command to invoke, e.g. `aws`, `gh`, `doctl`, `az`.


After filling in the form, you'll see a Go package created in the `plugins` directory, with separate files for the plugin, credential, and executable. For example:
plugins/
├── aws/
│ ├── plugin.go
│ ├── access_key.go
│ └── aws.go
├── digitalocean/
│ ├── plugin.go
│ ├── personal_access_token.go
│ └── doctl.go
├── github/
│ ├── plugin.go
│ ├── personal_access_token.go
│ └── gh.go
└── heroku/
├── plugin.go
├── api_key.go
└── heroku.go
To save you some time, the generated files will be stubbed out with information that's derived from the Makefile prompts on a best-effort basis. It contains _TODO_ comments in the code to steer you in the direction of what to change or validate for correctness.
## Step 2: Edit the plugin definition[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#step-2-edit-the-plugin-definition "Direct link to Step 2: Edit the plugin definition")
The `plugin.go` file contains basic information about the plugin and the platform it represents, including which credential types and executables make up the plugin.
## Step 3: Edit the credential definition[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#step-3-edit-the-credential-definition "Direct link to Step 3: Edit the credential definition")
The credential definition file describes the schema of the credential, how the credential should get provisioned to executables, and how the credential can be imported into 1Password.
### Credential information and schema[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#credential-information-and-schema "Direct link to Credential information and schema")
The first section of the credential definition is where you can add information about the credential:
  * The **name** of the credential, as the platform calls it.
  * The **documentation URL** provided by the platform that describes the credential. _(optional)_
  * The **management URL** on the platform where the credential can be created and revoked. This is usually a URL to the dashboard, console, or authentication settings of the platform. _(optional)_


The next section is where you define the schema of the credential. This is segmented into fields. Many credentials consist of just a single secret field, but you can add more fields to add more details to the 1Password item that are related to authentication, even if the fields are not secret.
Examples of additional fields are: the host, username, account ID, and all other things that are needed to authenticate and make sense to include in the 1Password item for the credential type. All fields you declare here will also show up in the end user's 1Password item.
Here's what you can specify per **field** :
  * The **field name** , titlecased. _(required)_
  * A short **description** of the field. This supports markdown. _(required)_
  * Whether the field is **optional**. Defaults to false.
  * Whether the field is **secret** , and should be concealed in the 1Password GUI. Defaults to not secret.  
Note: The credential schema is expected to contain at least 1 secret field.
  * What the actual credential **value is composed of**. The length, character set, and whether it contains a fixed prefix.


### Provisioner[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#provisioner "Direct link to Provisioner")
The credential definition also specifies how the credential is usually provisioned to exectuables, in order for them to use the credential for authentication.
Provisioners are in essence hooks that get executed before the executable is run by 1Password CLI, and after the executable exits in case any cleanup is needed. In those hooks, provisioners can do all the setup required for the executable to authenticate, including setting environment variables, creating files, adding command-line arguments, or even generating temporary credentials. After the executable exits, there should be no trace of the credentials on the user's filesystem.
The SDK provides a few common provisioners out of the box, so in most cases you don't have to care about the provisioning internals.
  * Environment variables
  * Files
  * Other


We currently recommend using environment variables as your provisioning method.
Environment variables are the most ubiquitous way to provision secrets. They only live in memory, and almost every CLI allows you to authenticate with them.
Here's how you can use the environment variable provisioner provided by the SDK:
provision.EnvVars(map[string]sdk.FieldName{
"AWS_ACCESS_KEY_ID": fieldname.AccessKeyID,
"AWS_SECRET_ACCESS_KEY": fieldname.SecretAccessKey,
})
Specify the 1Password field name and the environment variable name it should be placed in.
To figure out what environment variable the underlying CLI reads, here are a few tips:
  * Search the platform's CLI documentation website for a getting started guide, authentication guide, or CLI reference docs.
  * Look at the CLI's help text or manpage.
  * If the CLI or the underlying SDK it uses is open source, scan the source code to see if it accepts environment variables for authentication.


Some CLIs only support reading credentials from files on disk. In that case, you can use the file provisioner provided by the SDK. The file provisioner takes care of creating the file in a temporary directory and deleting it afterwards.
For security purposes, the file created by the file provisioner can only be read **once** by the executable. If that limitation does not work for your use case, you can file an 
Here are a few examples on how you can use the file provisioner to provision a temporary JSON file and pass the generated path to the executable:
Create a file provisioner and pass output path as --config-file
provision.TempFile(configFile,
provision.Filename("config.json"),
provision.AddArgs("--config-file", "{{ .Path }}"),
)
Create a file provisioner and set output path as CONFIG_FILE_PATH
provision.TempFile(configFile,
provision.Filename("config.json"),
provision.SetPathAsEnvVar("CONFIG_FILE_PATH"),
)
Create a file provisioner and pass output path as Java property
provision.TempFile(configFile,
provision.Filename("config.json"),
provision.AddArgs(`-Dconfig.path="{{ .Path }}"`),
)
Code to generate JSON file contents
func configFile(in sdk.ProvisionInput) ([]byte, error) {
config := Config{
Token: in.ItemFields[fieldname.Token]
}
  

contents, err := json.Marshal(config)
if err != nil {
return nil, err
}
  

return []byte(contents), nil
}
  

type Config struct {
Token string `json:"token"`
}
If the standard provisioners included in the SDK are not enough to authenticate the executable, you can also write your own provisioner. You can do so by implementing the 
A good example of a custom provisioner is the 
### Importer[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#importer "Direct link to Importer")
The credential definition also lets you specify importers. Importers are responsible for scanning the user's environment and file system for any occurrences of the needed credentials. 1Password CLI will run the importer and prompt the user to import their credentials one by one into 1Password.
It's very common for CLIs to write authentication data to disk, most commonly in a hidden config file in your home directory. This is not always documented by the CLI, so here are some tips to figure out if such a config file exists:
  * Check the platform's documentation for mentions of config files.
  * See if the CLI offers a `login`, `auth`, `configure`, or `setup` command that covers authentication. If it does, it's pretty likely there's a credential being stored in your home directory after completing such a flow.
  * If the CLI is open source, check the source code to see if such a file exists.
  * Look at your own home directory or `~/.config` directory to see if there are files related to the platform. Here's an example command to find local `aws` configuration files:


find ~/.* -maxdepth 3 -path "*aws*"
The SDK provides helper functions to load files, parse files, and scan environment variables to make writing an importer for your credential type easier.
  * `~/.aws/credentials`)
  * `~/.circleci/cli.yml`)
  * `~/.netrc`)


If you already have a shell plugin configured for a tool, and you want to generate an example configuration tile to test an importer, reference the tool by its full path rather than by its name. This makes sure you invoke the the tool without the plugin.
## Step 4: Edit the executable definition[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#step-4-edit-the-executable-definition "Direct link to Step 4: Edit the executable definition")
The last thing the plugin is responsible for is to define the CLI or executable that you'd like 1Password to handle authentication for. This is the final piece that glues everything together.
The executable definition describes the following:
  * The **command** that should get executed by the 1Password CLI.
  * The display **name** of the CLI, as the platform calls it.
  * The **documentation URL** provided by the platform that describes the executable. _(optional)_
  * When the executable **needs authentication**. For example, many CLIs don't require authentication when the `--help` or `--version` flags are present.
  * The **credentials** that the executable uses.


  * `aws`)
  * `gh`)
  * `heroku`)


## Step 5: Build and test your plugin locally[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#step-5-build-and-test-your-plugin-locally "Direct link to Step 5: Build and test your plugin locally")
To see if you've properly filled out the plugin, credential, and executable defintions, you can run the following Makefile command to validate the definitions:
make <plugin-name>/validate
If that succeeds, it's now time to locally build and test your plugin! You can do so using the following command:
make <plugin-name>/build
The build artifact will be placed in `~/.op/plugins/local`. It should show up in `op` if you run the following command:
op plugin list
To see it in action, you can use the `op plugin init` command:
op plugin init <plugin-executable>
## [​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#-submit-a-pr "Direct link to -submit-a-pr")
While you're free to keep on using the plugin locally, we'd encourage you to submit a PR on the 
Before doing so, be sure to read the 
If you feel that the SDK does not serve your use case well, reach out to us by creating an [Developer Slack workspace](https://developer.1password.com/joinslack) to tell us about your plugin proposal. We can advise you on the most suitable approach for your use case.
## Learn more[​](https://developer.1password.com/docs/cli/shell-plugins/contribute/#learn-more "Direct link to Learn more")
  * [Shell plugins troubleshooting](https://developer.1password.com/docs/cli/shell-plugins/troubleshooting/)
  * [Join our Developer Slack workspace](https://developer.1password.com/joinslack)


### Was this page helpful?
YesNo
