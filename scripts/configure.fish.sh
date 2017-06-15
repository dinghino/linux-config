#!/usr/bin/fish
#!~SAVE

#!title: Fish shell - configure
#!description
# Install Oh My Fish, agnoster theme and setup fish as default shell
#!end-description
# curl -L https://get.oh-my.fish | fish


cp -rf ../configs/omf ~/.configs/

curl -L https://get.oh-my.fish > omf-install
chsh -s (which fish); fish omf-install -y; rm omf-install;
