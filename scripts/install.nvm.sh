#!/bin/bash

# Install NodeVersionManager for bash

source ./utils.sh

printBold 'Installing NVM 0.33.2 (Check for latest version)...'
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
