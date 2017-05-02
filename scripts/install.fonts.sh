#!/bin/bash

# Install some fonts that allows ligatures or are patched with icons and stuff.
# These fonts are used in some software configuration present in this bootstrap
# such as configs for tilix and visual studio code.
source ./utils.sh

# Install fonts
mkdir /tmp/fonts/
cd /tmp/fonts/
# Get the fonts needed
printBold '- Fetching Inconsolata...'
curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Inconsolata.zip >> ./inconsolata.zip
printBold '- Fetching Monofur...'
curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Monofur.zip >> ./monofur.zip
printBold '- Fetching Firacode...'
curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/FiraCode.zip >> ./firacode.zip
printBold '- Unpacking...'
sudo unzip '*.zip' -d ~/.local/share/fonts
printBold '- Updating font cache (reload terminal to use new fonts)'
sudo fc-cache -fv
printBold '- Cleaning up'
cd ..
rm -rf ./fonts