---
title: "Get started with 1Password CLI | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/get-started/"
captured: 2025-12-15
category: concepts
relevance:
  - environment variables
  - script integration
  - authentication
  - vault management
  - security patterns
keywords:
  - vault
  - item
  - op vault
  - op signin
  - environment variable
  - authentication
related: []
---

# Get started with 1Password CLI | 1Password Developer

On this page
1Password CLI brings 1Password to your terminal. Learn how to install the CLI, then integrate it with your 1Password app and sign in with Touch ID, Windows Hello, or another system authentication option.
## Step 1: Install 1Password CLI[​](https://developer.1password.com/docs/cli/get-started/#step-1-install-1password-cli "Direct link to Step 1: Install 1Password CLI")
Requirements
  * Mac
  * Windows
  * Linux


  * [1Password subscription](https://1password.com/pricing/password-manager)
  * [1Password for Mac](https://1password.com/downloads/mac)*
  * macOS Big Sur 11.0.0 or later


Supported shells: Bash, Zsh, sh, fish
*Required to integrate 1Password CLI with the 1Password app.
  * [1Password subscription](https://1password.com/pricing/password-manager)
  * [1Password for Windows](https://1password.com/downloads/windows)


Supported shells: PowerShell
  * [1Password subscription](https://1password.com/pricing/password-manager)
  * [1Password for Linux](https://1password.com/downloads/linux)*
  * A PolKit authentication agent running*


Supported shells: Bash, Zsh, sh, fish
*Required to integrate 1Password CLI with the 1Password app.
  * Mac
  * Windows
  * Linux


  * homebrew
  * Manual


  1. To install 1Password CLI with 
brew install 1password-cli
  2. Check that 1Password CLI installed successfully:
op --version

The 
To manually install 1Password CLI on macOS:
  1. Download   
Learn how to [verify its authenticity](https://developer.1password.com/docs/cli/verify/).
  2.      * **Package file** : Open `op.pkg` and install 1Password CLI in the default location (`usr/local/bin`).
     * **ZIP file** : Open `op.zip` and unzip the file, then move `op` to `usr/local/bin`.
  3. Check that 1Password CLI was installed successfully:
op --version


  * winget
  * Manual


  1. To install 1Password CLI with winget:
winget install 1password-cli
  2. Check that 1Password CLI installed successfully:
op --version


To manually install 1Password CLI on Windows:
  1. Download `op.exe`.  
Learn how to [verify its authenticity](https://developer.1password.com/docs/cli/verify/).
  2. Open PowerShell **as an administrator**.
  3. Create a folder to move `op.exe` into. For example, `C:\Program Files\1Password CLI`.
mkdir "C:\Program Files\1Password CLI"
  4. Move the `op.exe` file to the new folder.
mv ".\op.exe" "C:\Program Files\1Password CLI"
  5. Add the folder containing the `op.exe` file to your PATH.
**Windows 10 and later**
    1. Search for **Advanced System Settings** in the Start menu.
    2. Select **Environment Variables**.
    3. In the System Variables section, select the **PATH** environment variable and select **Edit**.
    4. In the prompt, select **New** and add the directory where `op.exe` is located.
    5. Sign out and back in to Windows for the change to take effect.
  6. Check that 1Password CLI installed successfully:
op --version


If you'd rather install 1Password CLI with a single block of commands, run the following in PowerShell as administrator:
$arch = (Get-CimInstance Win32_OperatingSystem).OSArchitecture
switch ($arch) {
'64-bit' { $opArch = 'amd64'; break }
'32-bit' { $opArch = '386'; break }
Default { Write-Error "Sorry, your operating system architecture '$arch' is unsupported" -ErrorAction Stop }
}
$installDir = Join-Path -Path $env:ProgramFiles -ChildPath '1Password CLI'
Invoke-WebRequest -Uri "https://cache.agilebits.com/dist/1P/op2/pkg/v2.32.0/op_windows_$($opArch)_v2.32.0.zip" -OutFile op.zip
Expand-Archive -Path op.zip -DestinationPath $installDir -Force
$envMachinePath = [System.Environment]::GetEnvironmentVariable('PATH','machine')
if ($envMachinePath -split ';' -notcontains $installDir){
[Environment]::SetEnvironmentVariable('PATH', "$envMachinePath;$installDir", 'Machine')
}
Remove-Item -Path op.zip
If your Windows operating system uses a language other than English, you'll need to manually set `$arch` in the first line. To do this, replace `$arch = (Get-CimInstance Win32_OperatingSystem).OSArchitecture` with `$arch = "64-bit"` or `$arch = "32-bit"`.
  * APT
  * YUM
  * Alpine
  * NixOS
  * Manual


To install 1Password CLI using APT on Debian- and Ubuntu-based distributions:
  1. Run the following command:
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg && \
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/$(dpkg --print-architecture) stable main" | \
sudo tee /etc/apt/sources.list.d/1password.list && \
sudo mkdir -p /etc/debsig/policies/AC2D62742012EA22/ && \
curl -sS https://downloads.1password.com/linux/debian/debsig/1password.pol | \
sudo tee /etc/debsig/policies/AC2D62742012EA22/1password.pol && \
sudo mkdir -p /usr/share/debsig/keyrings/AC2D62742012EA22 && \
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
sudo gpg --dearmor --output /usr/share/debsig/keyrings/AC2D62742012EA22/debsig.gpg && \
sudo apt update && sudo apt install 1password-cli
See a step-by-step version of the script
    1. Add the key for the 1Password `apt` repository:
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg
    2. Add the 1Password `apt` repository:
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/$(dpkg --print-architecture) stable main" |
sudo tee /etc/apt/sources.list.d/1password.list
    3. Add the debsig-verify policy:
sudo mkdir -p /etc/debsig/policies/AC2D62742012EA22/
curl -sS https://downloads.1password.com/linux/debian/debsig/1password.pol | \
sudo tee /etc/debsig/policies/AC2D62742012EA22/1password.pol && \
sudo mkdir -p /usr/share/debsig/keyrings/AC2D62742012EA22 && \
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
sudo gpg --dearmor --output /usr/share/debsig/keyrings/AC2D62742012EA22/debsig.gpg
    4. Install 1Password CLI:
sudo apt update && sudo apt install 1password-cli
  2. Check that 1Password CLI installed successfully:
op --version


Alternatively, download the latest 1Password CLI `.deb` package directly from one of the following links:
  * [amd64](https://downloads.1password.com/linux/debian/amd64/stable/1password-cli-amd64-latest.deb)
  * [386](https://downloads.1password.com/linux/debian/386/stable/1password-cli-386-latest.deb)
  * [arm](https://downloads.1password.com/linux/debian/arm/stable/1password-cli-arm-latest.deb)
  * [arm64](https://downloads.1password.com/linux/debian/arm64/stable/1password-cli-arm64-latest.deb)


To install 1Password CLI using YUM on RPM-based distributions:
  1. Run the following commands:
sudo rpm --import https://downloads.1password.com/linux/keys/1password.asc
sudo sh -c 'echo -e "[1password]\nname=1Password Stable Channel\nbaseurl=https://downloads.1password.com/linux/rpm/stable/\$basearch\nenabled=1\ngpgcheck=1\nrepo_gpgcheck=1\ngpgkey=\"https://downloads.1password.com/linux/keys/1password.asc\"" > /etc/yum.repos.d/1password.repo'
sudo dnf check-update -y 1password-cli && sudo dnf install 1password-cli
The above script is comprised of the following steps
    1. Import the public key:
sudo rpm --import https://downloads.1password.com/linux/keys/1password.asc
    2. Configure the repository information:
sudo sh -c 'echo -e "[1password]\nname=1Password Stable Channel\nbaseurl=https://downloads.1password.com/linux/rpm/stable/\$basearch\nenabled=1\ngpgcheck=1\nrepo_gpgcheck=1\ngpgkey=\"https://downloads.1password.com/linux/keys/1password.asc\"" > /etc/yum.repos.d/1password.repo'
    3. Install 1Password CLI:
sudo dnf check-update -y 1password-cli && sudo dnf install 1password-cli
  2. Check that 1Password CLI installed successfully:
op --version


Alternatively, download the latest 1Password CLI `.rpm` package directly from one of the following links:
  * [x86_64](https://downloads.1password.com/linux/rpm/stable/x86_64/1password-cli-latest.x86_64.rpm)
  * [i386](https://downloads.1password.com/linux/rpm/stable/i386/1password-cli-latest.i386.rpm)
  * [aarch64](https://downloads.1password.com/linux/rpm/stable/aarch64/1password-cli-latest.aarch64.rpm)
  * [armv7l](https://downloads.1password.com/linux/rpm/stable/armv7l/1password-cli-latest.armv7l.rpm)


To install 1Password CLI on Alpine x86_64 distributions:
  1. Run the following commands:
echo https://downloads.1password.com/linux/alpinelinux/stable/ >> /etc/apk/repositories
wget https://downloads.1password.com/linux/keys/alpinelinux/support@1password.com-61ddfc31.rsa.pub -P /etc/apk/keys
apk update && apk add 1password-cli
The above script is comprised of the following steps
    1. Add Password CLI to your list of repositories:
echo https://downloads.1password.com/linux/alpinelinux/stable/ >> /etc/apk/repositories
    2. Add the public key to validate the APK to your keys directory:
wget https://downloads.1password.com/linux/keys/alpinelinux/support@1password.com-61ddfc31.rsa.pub -P /etc/apk/keys
    3. Install 1Password CLI:
apk update && apk add 1password-cli
  2. Check that 1Password CLI installed successfully:
op --version


The Nix package is available from the NixOS open source community.
To install 1Password CLI on your NixOS system:
  1. Add 1Password to your `/etc/nixos/configuration.nix` file, or `flake.nix` if you're using a flake. For example, the following snippet includes 1Password CLI and the 1Password app:
# NixOS has built-in modules to enable 1Password
# along with some pre-packaged configuration to make
# it work nicely. You can search what options exist
# in NixOS at https://search.nixos.org/options
  

# Enables the 1Password CLI
programs._1password = { enable = true; };
  

# Enables the 1Password desktop app
programs._1password-gui = {
enable = true;
# this makes system auth etc. work properly
polkitPolicyOwners = [ "<your-linux-username>" ];
};
  2. After you make changes to your configuration file, apply them:
     * If you added 1Password to `/etc.nixos/configuration.nix`, run:
sudo nixos-rebuild switch
     * If you added 1Password to `flake.nix`, replace `<flake-directory-path>` with the directory your flake is in and `<output-name>` with the name of the flake output containing your system configuration, then run the command.
sudo nixos-rebuild switch --flake <flake-directory-path>.#<output-name>
  3. Check that 1Password CLI installed successfully:
op --version


Learn more about 
To install 1Password CLI on Linux without a package manager:
ARCH="<choose between 386/amd64/arm/arm64>" && \
wget "https://cache.agilebits.com/dist/1P/op2/pkg/v2.32.0/op_linux_${ARCH}_v2.32.0.zip" -O op.zip && \
unzip -d op op.zip && \
sudo mv op/op /usr/local/bin/ && \
rm -r op.zip op && \
sudo groupadd -f onepassword-cli && \
sudo chgrp onepassword-cli /usr/local/bin/op && \
sudo chmod g+s /usr/local/bin/op
Or follow the extended guide
  1. Download the 
gpg --keyserver keyserver.ubuntu.com --receive-keys 3FEF9748469ADBE15DA7CA80AC2D62742012EA22
gpg --verify op.sig op
  2. Move `op` to `/usr/local/bin`, or another directory in your `$PATH`.
  3. Check that 1Password CLI installed successfully:
op --version
  4. Create the `onepassword-cli` group if it doesn't yet exist:
sudo groupadd onepassword-cli
  5. Set the correct permissions on the `op` binary:
sudo chgrp onepassword-cli /usr/local/bin/op && \
sudo chmod g+s /usr/local/bin/op


## Step 2: Turn on the 1Password desktop app integration[​](https://developer.1password.com/docs/cli/get-started/#step-2-turn-on-the-1password-desktop-app-integration "Direct link to Step 2: Turn on the 1Password desktop app integration")
  * Mac
  * Windows
  * Linux


  1. Open and unlock the [1Password app](https://1password.com/downloads/).
  2. Select your account or collection at the top of the sidebar.
  3. Navigate to **Settings** >
  4. Select **Integrate with 1Password CLI**.
  5. If you want to authenticate 1Password CLI with your fingerprint, turn on **[Touch ID](https://support.1password.com/touch-id-mac/)** in the app.


![The 1Password Developer settings pane with the Integrate with 1Password CLI option selected.](https://developer.1password.com/img/cli/developer-settings-light.png)
  1. Open and unlock the [1Password app](https://1password.com/downloads/).
  2. Select your account or collection at the top of the sidebar.
  3. Turn on **[Windows Hello](https://support.1password.com/windows-hello/)** in the app.
  4. Navigate to **Settings** >
  5. Select **Integrate with 1Password CLI**.


![The 1Password Developer settings pane with the Integrate with 1Password CLI option selected.](https://developer.1password.com/img/cli/developer-settings-windows-light.png)
  1. Open and unlock the [1Password app](https://1password.com/downloads/).
  2. Select your account or collection at the top of the sidebar.
  3. Navigate to **Settings** >
  4. Turn on **[Unlock using system authentication](https://support.1password.com/system-authentication-linux/)**.
  5. Navigate to **Settings** >
  6. Select **Integrate with 1Password CLI**.


![The 1Password Developer settings pane with the Integrate with 1Password CLI option selected.](https://developer.1password.com/img/cli/developer-settings-linux.png)
[Learn more about the 1Password desktop app integration.](https://developer.1password.com/docs/cli/app-integration/)
## Step 3: Enter any command to sign in[​](https://developer.1password.com/docs/cli/get-started/#step-3-enter-any-command-to-sign-in "Direct link to Step 3: Enter any command to sign in")
After you've turned on the app integration, enter any command and you'll be prompted to authenticate. For example, run this command to see all the vaults in your account:
op vault list
#### If you have multiple accounts[​](https://developer.1password.com/docs/cli/get-started/#if-you-have-multiple-accounts "Direct link to If you have multiple accounts")
If you've added multiple 1Password accounts to your desktop app, you can use [`op signin`](https://developer.1password.com/docs/cli/reference/commands/signin/) to select an account to sign in to with 1Password CLI. Use the arrow keys to choose from the list of all accounts added to your 1Password app.
op signin
See result...
Select account [Use arrows to move, type to filter]
> ACME Corp (acme.1password.com)
AgileBits (agilebits.1password.com)
Add another account
[Learn more about using multiple accounts with 1Password CLI.](https://developer.1password.com/docs/cli/use-multiple-accounts/)
## Next steps[​](https://developer.1password.com/docs/cli/get-started/#next-steps "Direct link to Next steps")
  1. [Get started with basic 1Password CLI commands.](https://developer.1password.com/docs/cli/reference/)
  2. [Set up 1Password Shell Plugins to handle authentication for your other command-line tools.](https://developer.1password.com/docs/cli/shell-plugins/)
  3. [Learn how to securely load secrets from your 1Password account without putting any plaintext secrets in code.](https://developer.1password.com/docs/cli/secret-references/)


## Learn more[​](https://developer.1password.com/docs/cli/get-started/#learn-more "Direct link to Learn more")
  * [1Password app integration troubleshooting](https://developer.1password.com/docs/cli/app-integration#troubleshooting)
  * [1Password app integration security](https://developer.1password.com/docs/cli/app-integration-security/)
  * [How 1Password CLI detects configuration directories](https://developer.1password.com/docs/cli/config-directories)


### Was this page helpful?
YesNo
