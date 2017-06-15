#!/bin/bash
#!~SAVE

#!title: Fish shell - install
#!description
# Install fish shell and set as default shell, without any configuration
# or extensions. Those can be added through the config.fish.sh script.
#!end-description
# curl -L https://get.oh-my.fish | fish

cp ../configs/config.fish ~/.config/fish/

sudo apt-add-repository ppa:fish-shell/release-2
sudo apt-get update
sudo apt-get install fish

# make default shell
chsh -s /usr/bin/fish