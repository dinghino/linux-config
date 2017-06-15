#!/bin/bash
#!~SAVE

#!title: Install Tilix
#!description
# Install tilix (ex terminix) terminal emulator and restore the dconf file
# to configure it nicely
#!end-description
source ./utils

printBold 'Installing tilix...'
sudo apt-get -qq install tilix -y
dconf load /com/gexperts/Tilix < ../configs/tilix.dconf

