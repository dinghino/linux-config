#!/bin/bash
#!~SAVE

#!title: Configure VIm
#!description
# Vim: The power tool for everyone!
# The go-to terminal text editor. This script allows to setup a preset
# of configuration, plugins easily.
# If VIm is not present on the system it will install that too.
#!end-description

if [ $(./apt.exists.sh vim) == 0 ] then
    sudo apt-get install vim
fi

cp ../configs/.vimrc ~

curl -fLo ~/.vim/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

sudo vim -c :PlugInstall -c quitall