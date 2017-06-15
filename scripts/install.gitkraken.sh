#!/bin/bash
#!~SAVE

#!title: Install GitKraken
#!description
# The ultimate GIT manager.
#!end-description

source ./utils.sh

if [ $(./apt.exists.sh gconf2) == 0 ]; then
  printBold "Installing dependecy: gconf2"
  sudo apt-get --force-yes --yes install gconf2
fi

wget https://release.gitkraken.com/linux/gitkraken-amd64.deb
sudo dpkg -i gitkraken-amd64.deb
rm ./gitkraken-amd64.deb