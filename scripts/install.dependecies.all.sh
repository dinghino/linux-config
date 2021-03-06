#!/bin/bash

source ./utils.sh

# Add ppa repositories required
# TODO: Check distribution version and add optional ppa for python3.6
#       As of now this will assume 16.10+
printBold 'Adding repositories'
sudo add-apt-repository ppa:fish-shell/release-2 -y
sudo add-apt-repository ppa:webupd8team/terminix -y

printBold 'Updating...'
sudo apt-get -qq update
printBold 'Installing...'
# Install ALL the dependecies required by the rule-them-all-script
sudo apt-get -qq install xsel git curl vim unzip python3.6 python3-pip build-essential cmake python-dev python3-dev -y