# Installation | Buzz

- **Source:** https://chidiwilliams.github.io/buzz/docs/installation
- **Status:** 200
- **Validation:** PASS

---

[Skip to main content](https://chidiwilliams.github.io/buzz/docs/installation#__docusaurus_skipToContent_fallback)
On this page
To install Buzz, download the latest version for your operating system. Buzz is available on **Mac** (Intel and Apple silicon), **Windows** , and **Linux**.
### macOS[​](https://chidiwilliams.github.io/buzz/docs/installation#macos "Direct link to macOS")
Download the `.dmg` from the 
### Windows[​](https://chidiwilliams.github.io/buzz/docs/installation#windows "Direct link to Windows")
Get the installation files from the 
App is not signed, you will get a warning when you install it. Select `More info` -> `Run anyway`.
## Linux[​](https://chidiwilliams.github.io/buzz/docs/installation#linux "Direct link to Linux")
Buzz is available as a 
To install flatpak, run:
```
flatpak install flathub io.github.chidiwilliams.Buzz  

```

To install snap, run:
```
sudoapt-getinstall libportaudio2 libcanberra-gtk-module libcanberra-gtk3-module  
sudo snap install buzz  
sudo snap connect buzz:password-manager-service  

```

## PyPI[​](https://chidiwilliams.github.io/buzz/docs/installation#pypi "Direct link to PyPI")
```
pip install buzz-captions  
python -m buzz  

```

On Linux install system dependencies you may be missing
```
sudo apt-get install --no-install-recommends libyaml-dev libtbb-dev libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 libxcb-shape0 libxcb-cursor0 libportaudio2 gettext libpulse0 ffmpeg  

```

On versions prior to Ubuntu 24.04 install `sudo apt-get install --no-install-recommends libegl1-mesa`
  * [macOS](https://chidiwilliams.github.io/buzz/docs/installation#macos)
  * [Windows](https://chidiwilliams.github.io/buzz/docs/installation#windows)
  * [Linux](https://chidiwilliams.github.io/buzz/docs/installation#linux)
  * [PyPI](https://chidiwilliams.github.io/buzz/docs/installation#pypi)


