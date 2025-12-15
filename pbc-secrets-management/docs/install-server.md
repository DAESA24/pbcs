---
title: "Install 1Password CLI on a server | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/install-server/"
captured: 2025-12-15
category: concepts
relevance:
  - general
keywords:
  - 1password-cli
related: []
---

# Install 1Password CLI on a server | 1Password Developer

# Install 1Password CLI on a server
There are several different ways to install 1Password CLI on a server.
To install `amd64` host, you can use this one-line command:
ARCH="amd64"; \
OP_VERSION="v$(curl https://app-updates.agilebits.com/check/1/0/CLI2/en/2.0.0/N -s | grep -Eo '[0-9]+\\.[0-9]+\\.[0-9]+')"; \
curl -sSfo op.zip \
https://cache.agilebits.com/dist/1P/op2/pkg/"$OP_VERSION"/op_linux_"$ARCH"_"$OP_VERSION".zip \
&& unzip -od /usr/local/bin/ op.zip \
&& rm op.zip
To install with Docker, you can use the 
docker pull 1password/op:2
If you want to add the CLI installation to your Dockerfile, then add this line:
Dockerfile
COPY --from=1password/op:2 /usr/local/bin/op /usr/local/bin/op
## Learn more[​](https://developer.1password.com/docs/cli/install-server/#learn-more "Direct link to Learn more")
  * [Install 1Password CLI on your machine](https://developer.1password.com/docs/cli/get-started#step-1-install-1password-cli)


### Was this page helpful?
YesNo
