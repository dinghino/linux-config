# Configuration program for linux system

This will be a simple program that will allow me to setup a clear linux install with all the stuff I usually need to install manually.

This would include `git`, `fish` shell, `powerline fonts`, `tilix`, `vim` with plugins, themes for everything, gui programs that can be easily fetched and installed by terminal etc.

The idea is to have a simple script - probably bash - that will do the wget or curl, launch the install script if needed, configure stuff in the system etc all by itself, allowing a _one command rule them all_ to ease up the system installation.

## Currently available

Current installation and configuration is available at at [this](https://gist.github.com/dinghino/0f081500fdbb98b9db85a4cb3d3330b9) gist, but is only for **VIm** setup on an already almost-configured system that relies on fish, python3.6 installed on the system, a configured terminal emulator (tilix/terminal) and nerd fonts (Inconsolata).

## Manual installation
Until a script is available I will put all the installation instructions here. This section will be moved probably somewhere else later on, but for ease it'll stay here for now.

> Note that all the commands are for a debian distribution (Currently running Ubuntu 17.04 + Gnome 3) and are meant to work from the terminal.
This section is a temporary storage for everything that will go into the script

### Basic dependecies

> **NOTE**
> If on `16.10+` python3.6 is on the universe repositories and there is no need to add the repo. For older versions please add the ppa repository for python3.6
>    ```
>    $ sudo add-apt-repository ppa:jonathonf/python-3.6 -y
>    ```

Basic dependecies and utility programs that are needed to setup the environment and work. Some of those could be
installed by default on the system

    $ sudo apt-get update
    $ sudo apt-get install git curl vim unzip python3.6 build-essential cmake python-dev python3-dev -y

#### Fonts
Also both `fish shell` and vim plugins require a patched font to properly work.

My choices are on `Inconsolata` and `Monofur` fonts, both available from [this awesome repository](https://github.com/ryanoasis/nerd-fonts)

With `Visual Studio Code` synced config `Fira Code` is the default editor font and needs to be installed to correclty text and font ligatures. (Solution study underway).
More on Fira Code can be found [here](https://github.com/tonsky/FiraCode).

To install from command line just those two fonts:
 
    mkdir /tmp/fonts/
    cd /tmp/fonts
    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Inconsolata.zip
    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Monofur.zip
    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/FiraCode.zip

    # unzip the fonts inside the default fonts folder
    sudo unzip '*.zip' -d ~/.local/share/fonts
    sudo fc-cache -fv
    
    # cleanup
    cd ..
    rm -rf ./fonts

**After installing the fonts edit your terminal profile to use one of them**

### **N**ode **V**ersion **M**anager

* [Repository](https://github.com/creationix/nvm)

NVM Allows handling different versions of `nodejs` and relative npm easily

    $ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash

Will install `nvm` and configure it for bash

### Fish shell and oh-my-fish

* [Fish shell website](https://fishshell.com/)
* [Oh my fish repository](https://github.com/oh-my-fish/oh-my-fish)
```
$ sudo add-apt-repository ppa:fish-shell/release-2 -y
$ sudo apt-get update
$ sudo apt-get install fish -y

# Install oh-my-fish and set agnoster theme
$ curl -L https://get.oh-my.fish | fish
$ omf install agnoster  # download and set agnoster theme

# Set fish as default shell
$ chsh -s `which fish`
```
If everything has been set properly the terminal should display correctly and fish be your default shell.

### nvm fish wrapper
Allows using nvm inside fish
* [Repository](https://github.com/passcod/nvm-fish-wrapper)
* [Documentation]()
```b
$ ~> cd ~/.config/fish
$ ~/.c/fish> git clone git://github.com/passcod/nvm-fish-wrapper.git nvm-wrapper
```

then edit `~/.config/fish/config.fish` and add
> NOTE: This will be already in the `config.fish` that the scripts pull/adds

    source ~/.config/fish/nvm-wrapper/nvm.fish

### Virtualfish (virtualenvwrapper for fish)

Fish wrapper for python virtualenvwrapper. 
* [Repository](https://github.com/adambrenecki/virtualfish)
* [Documentation](http://virtualfish.readthedocs.org/en/latest/)

To install 
* `pip install virtualfish` with the system default python (2.7)
* `python3.6 -m pip install virtualfish` to set the default python as python3.6

Edit `~/.config/fish/config.fish` and put

`eval (<python> -m virtualfish)` where `<python>` is your python version (`python` or `python3.6`)

Restart the sell and call `vf` to use it.


### VIm configuration

For now see [this gist](https://gist.github.com/dinghino/0f081500fdbb98b9db85a4cb3d3330b9) to properly setup vim


### Tilix

Tilix is an alternative terminal emulator that allows window splitting, tabs etc, previously known as `terminix`
* [Repository](https://github.com/gnunn1/tilix)

```bash
sudo add-apt-repository ppa:webupd8team/terminix -y
sudo apt update
sudo apt install tilix
```
## **TODO**

* [x] Complete the first stub of the readme!
* [ ] List all the stuff needed
  * [x] Patched fonts instructions
  * [x] Fish + oh-my-fish
  * [x] virtualfish (python virtualenvwrapper for fish)
  * [x] nvm (node virtual manager)
  * [x] [nvm-fish-wrapper](https://github.com/passcod/nvm-fish-wrapper)
  * [x] VirtualFish (python virtualenvwrapper)
  * [x] tilix terminal emulator (ex terminix)
  * [x] Vim config instructions
  * [ ] Instructions for VSCode
    * [ ] add/configure extensions (sync-settings) from cli
* [ ] Autoconfigure terminal profiles
* [ ] Instructions on git setup (Github | Bitbucket ) && auto authenticate
* [x] Define dependencies
* [ ] setup microscript to fetch various `config`s from gists and set them up
* [ ] Logically decide the steps
* [ ] Simple bash script to do everything (regardless of options)


## NOTE
Section for various stuff and links that needs to be put _upstairs_

* [Gnome keyring for git](https://askubuntu.com/questions/773455/what-is-the-correct-way-to-use-git-with-gnome-keyring-and-https-repos)
