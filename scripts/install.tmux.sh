#!/bin/bash
#!~SAVE

#!title: Install tmux
#!description
# Terminal MUltipleX for unix shell. There is a ready-to-use config file inside
# the configs/ folder. file should go inside your home/ (~) folder.
#!end-description
cp -rf ../configs/.tmux.conf ~
sudo apt-get install tmux