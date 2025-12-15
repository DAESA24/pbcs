---
title: "Use 1Password Shell Plugins with NixOS or home-manager | 1Password Developer"
source_url: "https://developer.1password.com/docs/cli/shell-plugins/nix/"
captured: 2025-12-15
category: integrations
relevance:
  - script integration
keywords:
  - 1password-cli
related: []
---

# Use 1Password Shell Plugins with NixOS or home-manager | 1Password Developer

# Configure shell plugins using Nix
If you're using Nix to manage your shell configuration, you can configure 1Password Shell Plugins natively within your Nix configuration.
  1. Add the 1Password Shell Plugins flake to your flake inputs:
{
description = "My NixOS system flake";
inputs = {
nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
# import the 1Password Shell Plugins Flake
_1password-shell-plugins.url = "github:1Password/shell-plugins";
# the rest of your flake inputs here
};
  

outputs = inputs@{ nixpkgs, ... }: {
# the rest of your flake here
}
}
  2. Somewhere in your flake output configuration, import and use the appropriate module:
     * NixOS without home-manager
     * Nix with home-manager
{
# import the NixOS module
imports = [ inputs._1password-shell-plugins.nixosModules.default ];
programs._1password-shell-plugins = {
# enable 1Password shell plugins for bash, zsh, and fish shell
enable = true;
# the specified packages as well as 1Password CLI will be
# automatically installed and configured to use shell plugins
plugins = with pkgs; [ gh awscli2 cachix ];
};
# this can also be `programs.bash` or `programs.fish`
programs.zsh = {
enable = true;
# the rest of your shell configuration here
};
}
{
# import the home-manager module
imports = [ inputs._1password-shell-plugins.hmModules.default ];
programs._1password-shell-plugins = {
# enable 1Password shell plugins for bash, zsh, and fish shell
enable = true;
# the specified packages as well as 1Password CLI will be
# automatically installed and configured to use shell plugins
plugins = with pkgs; [ gh awscli2 cachix ];
};
# this can also be `programs.bash` or `programs.fish`
programs.zsh = {
enable = true;
# the rest of your shell configuration here
};
}
  3. Apply the updated configuration:
     * NixOS (including home-manager as a NixOS module)
     * Nix with standalone home-manager
~/path/to/flake/directory/ should be the path to the directory containing your `flake.nix` file, and my-computer should be the name of the flake output to use as the system configuration.
  
  

sudo nixos-rebuild switch --flake "~/path/to/flake/directory/.#my-computer"
~/path/to/flake/directory/ should be the path to the directory containing your `flake.nix` file, and my-computer should be the name of the flake output to use as the system configuration.
  
  

home-manager switch --flake "~/path/to/flake/directory/.#my-computer"


### Was this page helpful?
YesNo
