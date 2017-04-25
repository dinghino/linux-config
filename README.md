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

If on `16.10+` python3.6 is on the universe repositories and there is no need to add the repo. For lower versions

    $ sudo add-apt-repository ppa:jonathonf/python-3.6

### Basic dependecies

    $ sudo apt-get update
    $ sudo apt-get install git curl vim python3.6 build-essential cmake python-dev python3-dev

### **N**ode **V**irtual **M**anager

    $ ~> git clone https://github.com/creationix/nvm.git ~/.nvm
    $ ~> cd ~/.nvm
    $ ~/.nvm> git checkout (git describe --abbrev=0 --tags)


### Fish shell and oh-my-fish

    $ sudo add-apt-repository ppa:fish-shell/release-2
    $ sudo apt-get update
    $ sudo apt-get install fish
    
    # Install oh-my-fish
    $ curl -L https://get.oh-my.fish | fish

### nvm fish wrapper

    $ ~> cd ~/.config/fish
    $ ~/.c/fish> git clone git://github.com/passcod/nvm-fish-wrapper.git nvm-wrapper

### virtualfish (virtualenvwrapper for fish)

then edit `~/.config/fish/config.fish` and add
> NOTE: This will be already in the `config.fish` that the scripts pull/adds

    source ~/.config/fish/nvm-wrapper/nvm.fish

### VIm configuration

    

## **TODO**

* [x] Complete the first stub of the readme!
* [ ] List all the stuff needed (and why)
  * [ ] Fish + oh-my-fish
  * [ ] virtualfish (python virtualenvwrapper for fish)
  * [ ] nvm (node virtual manager)
  * [ ] [nvm-fish-wrapper](https://github.com/passcod/nvm-fish-wrapper)
* [ ] Find all install instructions
* [ ] Define dependencies
* [ ] Logically decide the steps
* [ ] bash script or python?
