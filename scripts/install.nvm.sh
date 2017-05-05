#!/bin/bash
#!title: Install nvm
#!description
# Install NodeVersionManager for bash
#!end-description
source ./utils.sh

printBold 'Installing NVM 0.33.2 (Check for latest version)...'
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
