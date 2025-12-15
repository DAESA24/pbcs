---
title: "1Password Shell Plugins | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/"
captured: 2025-12-15
category: integrations
relevance:
  - authentication
  - vault management
  - security patterns
keywords:
  - vault
  - authentication
related: []
---

# 1Password Shell Plugins | 1Password Developer

On this page
# Use 1Password Shell Plugins to securely authenticate any CLI
With 1Password Shell Plugins, you can configure 1Password to securely authenticate third-party CLIs with your fingerprint, Apple Watch, or system authentication. Your CLI credentials are stored in your 1Password account, so you never have to manually enter your credentials or store them in plaintext.
You can [test shell plugins](https://developer.1password.com/docs/cli/shell-plugins/test/) or choose a shell plugin from the [list below](https://developer.1password.com/docs/cli/shell-plugins/#get-started) to get started.
Shell plugins are compatible with the following shells:
  * Bash
  * Zsh
  * fish


## Get started[​](https://developer.1password.com/docs/cli/shell-plugins/#get-started "Direct link to Get started")
[![](https://developer.1password.com/img/logos/akamai.png) Akamai](https://developer.1password.com/docs/cli/shell-plugins/akamai/)
[![](https://developer.1password.com/img/logos/argo-cd.svg) Argo CD](https://developer.1password.com/docs/cli/shell-plugins/argo-cd/)
[![](https://developer.1password.com/img/logos/axiom.svg) Axiom](https://developer.1password.com/docs/cli/shell-plugins/axiom)
[![](https://developer.1password.com/img/logos/aws.svg) AWS](https://developer.1password.com/docs/cli/shell-plugins/aws/)
[![](https://developer.1password.com/img/logos/aws.svg) AWS CDK Toolkit](https://developer.1password.com/docs/cli/shell-plugins/aws-cdk-toolkit/)
[![](https://developer.1password.com/img/logos/binance.svg) Binance](https://developer.1password.com/docs/cli/shell-plugins/binance)
[![](https://developer.1password.com/img/logos/cachix.png) Cachix](https://developer.1password.com/docs/cli/shell-plugins/cachix/)
[![](https://developer.1password.com/img/logos/cargo.png) Cargo](https://developer.1password.com/docs/cli/shell-plugins/cargo/)
[![](https://developer.1password.com/img/logos/circleci.svg) CircleCI](https://developer.1password.com/docs/cli/shell-plugins/circleci/)
[![](https://developer.1password.com/img/logos/civo.svg) Civo](https://developer.1password.com/docs/cli/shell-plugins/civo)
[![](https://developer.1password.com/img/logos/cloudflare.svg) Cloudflare Workers](https://developer.1password.com/docs/cli/shell-plugins/cloudflare-workers/)
[![](https://developer.1password.com/img/logos/crowdin.svg) Crowdin](https://developer.1password.com/docs/cli/shell-plugins/crowdin)
[![](https://developer.1password.com/img/logos/databricks.png) Databricks](https://developer.1password.com/docs/cli/shell-plugins/databricks/)
[![](https://developer.1password.com/img/logos/digitalocean.png) DigitalOcean](https://developer.1password.com/docs/cli/shell-plugins/digitalocean/)
[![](https://developer.1password.com/img/logos/datadog.svg) Dogshell](https://developer.1password.com/docs/cli/shell-plugins/datadog/)
[![](https://developer.1password.com/img/logos/fastly.png) Fastly](https://developer.1password.com/docs/cli/shell-plugins/fastly/)
[![](https://developer.1password.com/img/logos/flyio.svg) Flyctl](https://developer.1password.com/docs/cli/shell-plugins/flyctl)
[![](https://developer.1password.com/img/logos/fossa.png) FOSSA](https://developer.1password.com/docs/cli/shell-plugins/fossa/)
[![](https://developer.1password.com/img/logos/gitea.png) Gitea](https://developer.1password.com/docs/cli/shell-plugins/gitea/)
[![](https://developer.1password.com/img/logos/github.svg) GitHub](https://developer.1password.com/docs/cli/shell-plugins/github/)
[![](https://developer.1password.com/img/logos/gitlab.svg) GitLab](https://developer.1password.com/docs/cli/shell-plugins/gitlab/)
[![](https://developer.1password.com/img/logos/vault.svg) HashiCorp Vault](https://developer.1password.com/docs/cli/shell-plugins/hashicorp-vault/)
[![](https://developer.1password.com/img/logos/heroku.svg) Heroku](https://developer.1password.com/docs/cli/shell-plugins/heroku/)
[![](https://developer.1password.com/img/logos/hcloud.svg) Hetzner Cloud](https://developer.1password.com/docs/cli/shell-plugins/hetzner-cloud/)
[![](https://developer.1password.com/img/logos/homebrew.png) Homebrew](https://developer.1password.com/docs/cli/shell-plugins/homebrew/)
[![](https://developer.1password.com/img/logos/huggingface.svg) HuggingFace](https://developer.1password.com/docs/cli/shell-plugins/huggingface)
[![](https://developer.1password.com/img/logos/influxdb.png) InfluxDB](https://developer.1password.com/docs/cli/shell-plugins/influxdb)
[![](https://developer.1password.com/img/logos/kaggle.png) Kaggle](https://developer.1password.com/docs/cli/shell-plugins/kaggle)
[![](https://developer.1password.com/img/logos/lacework.png) Lacework](https://developer.1password.com/docs/cli/shell-plugins/lacework/)
[![](https://developer.1password.com/img/logos/forge.svg) Laravel Forge](https://developer.1password.com/docs/cli/shell-plugins/laravel-forge/)
[![](https://developer.1password.com/img/logos/vapor.svg) Laravel Vapor](https://developer.1password.com/docs/cli/shell-plugins/laravel-vapor/)
[![](https://developer.1password.com/img/logos/linode.svg) Linode](https://developer.1password.com/docs/cli/shell-plugins/linode/)
[![](https://developer.1password.com/img/logos/localstack.png) LocalStack](https://developer.1password.com/docs/cli/shell-plugins/localstack/)
[![](https://developer.1password.com/img/logos/mongodb.png) MongoDB Atlas](https://developer.1password.com/docs/cli/shell-plugins/mongodb-atlas)
[![](https://developer.1password.com/img/logos/mysql.svg) MySQL](https://developer.1password.com/docs/cli/shell-plugins/mysql/)
[![](https://developer.1password.com/img/logos/ngrok-light.svg) ngrok](https://developer.1password.com/docs/cli/shell-plugins/ngrok/)
[![](https://developer.1password.com/img/logos/oh-dear.png) Oh Dear](https://developer.1password.com/docs/cli/shell-plugins/oh-dear/)
[![](https://developer.1password.com/img/logos/okta.svg) Okta](https://developer.1password.com/docs/cli/shell-plugins/okta/)
[![](https://developer.1password.com/img/logos/openai-light.png) OpenAI](https://developer.1password.com/docs/cli/shell-plugins/openai/)
[![](https://developer.1password.com/img/logos/openai-light.png) OpenAI Evals](https://developer.1password.com/docs/cli/shell-plugins/openai-evals/)
[![](https://developer.1password.com/img/logos/pipedream.jpg) Pipedream](https://developer.1password.com/docs/cli/shell-plugins/pipedream)
[![](https://developer.1password.com/img/logos/postgresql.svg) PostgreSQL](https://developer.1password.com/docs/cli/shell-plugins/postgresql/)
[![](https://developer.1password.com/img/logos/pulumi-light.png) Pulumi](https://developer.1password.com/docs/cli/shell-plugins/pulumi/)
[![](https://developer.1password.com/img/logos/readme.png) ReadMe](https://developer.1password.com/docs/cli/shell-plugins/readme/)
[![](https://developer.1password.com/img/logos/sentry.svg) Sentry](https://developer.1password.com/docs/cli/shell-plugins/sentry/)
[![](https://developer.1password.com/img/logos/snowflake.png) Snowflake](https://developer.1password.com/docs/cli/shell-plugins/snowflake/)
[![](https://developer.1password.com/img/logos/snyk.svg) Snyk](https://developer.1password.com/docs/cli/shell-plugins/snyk/)
[![](https://developer.1password.com/img/logos/sourcegraph.svg) Sourcegraph](https://developer.1password.com/docs/cli/shell-plugins/sourcegraph/)
[![](https://developer.1password.com/img/logos/stripe.svg) Stripe](https://developer.1password.com/docs/cli/shell-plugins/stripe/)
[![](https://developer.1password.com/img/logos/terraform.svg) Terraform](https://developer.1password.com/docs/cli/shell-plugins/terraform/)
[![](https://developer.1password.com/img/logos/todoist.png) Todoist](https://developer.1password.com/docs/cli/shell-plugins/todoist)
[![](https://developer.1password.com/img/logos/treasure-data.png) Treasure Data](https://developer.1password.com/docs/cli/shell-plugins/treasure-data/)
[![](https://developer.1password.com/img/logos/tugboat.png) Tugboat](https://developer.1password.com/docs/cli/shell-plugins/tugboat/)
[![](https://developer.1password.com/img/logos/twilio.svg) Twilio](https://developer.1password.com/docs/cli/shell-plugins/twilio/)
[![](https://developer.1password.com/img/logos/upstash.png) Upstash](https://developer.1password.com/docs/cli/shell-plugins/upstash)
[![](https://developer.1password.com/img/logos/vercel.png) Vercel](https://developer.1password.com/docs/cli/shell-plugins/vercel/)
[![](https://developer.1password.com/img/logos/vertica.png) Vertica](https://developer.1password.com/docs/cli/shell-plugins/vertica)
[![](https://developer.1password.com/img/logos/vultr.svg) Vultr](https://developer.1password.com/docs/cli/shell-plugins/vultr/)
[![](https://developer.1password.com/img/logos/yugabyte.png) YugabyteDB](https://developer.1password.com/docs/cli/shell-plugins/yugabytedb/)
[![](https://developer.1password.com/img/logos/zapier.png) Zapier](https://developer.1password.com/docs/cli/shell-plugins/zapier)
[![](https://developer.1password.com/img/logos/zendesk-light.png) Zendesk](https://developer.1password.com/docs/cli/shell-plugins/zendesk/)
## Your favorite tool not listed?[​](https://developer.1password.com/docs/cli/shell-plugins/#your-favorite-tool-not-listed "Direct link to Your favorite tool not listed?")
Find out how to [build your own plugin](https://developer.1password.com/docs/cli/shell-plugins/contribute/).
### Was this page helpful?
YesNo
