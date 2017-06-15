#!/bin/bash
#!~SAVE

#!title: Install VS Code
#!description
# Visual Studio Code - generic IDE developed by microsoft.
# Recommended basic plugin is `Settings Sync` that allows syncing your settings
# (and installed plugins) through a GitHub gist
#!end-description

curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

sudo apt-get update
sudo apt-get install code # or code-insiders