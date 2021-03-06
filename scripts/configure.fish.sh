#!/usr/bin/fish

# Configuration script for fish shell
# Will install Oh My Fish, agnoster theme and setup fish as default shell

# curl -L https://get.oh-my.fish | fish

curl -L https://get.oh-my.fish > omf-install

fish omf-install -y; rm omf-install; omf install agnoster; chsh -s `which fish`; exit
