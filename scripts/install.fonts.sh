#!/bin/bash
#!~SAVE

#!title: Install Nerd Fonts
#!description
# Install some fonts that allows ligatures or are patched with icons and stuff.
# These fonts are used in some software configuration present in this bootstrap
# such as configs for tilix and visual studio code.
# Installed fonts:
# * Inconsolata Nerd Font
# * Monofur Nerd Font
# * FiraCode
#!end-description
source ./utils.sh

# Install fonts
mkdir ./fonts/
# Get the fonts needed
printBold '- Fetching Inconsolata Nerd Font...'
curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Inconsolata.zip >> ./fonts/inconsolata.zip
printBold '- Fetching Monofur Nerd Font...'
curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Monofur.zip >> ./fonts/monofur.zip
printBold '- Fetching FuraCode Nerd Font...'
curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/FiraCode.zip >> ./fonts/furacode.zip
printBold '- Fetching Fira Code...'
curl -L https://github.com/tonsky/FiraCode/releases/download/1.204/FiraCode_1.204.zip >> ./fonts/firacode.zip
printBold '- Unpacking...'
sudo unzip './fonts/*.zip' -d ~/.local/share/fonts
printBold '- Updating font cache (reload terminal to use new fonts)'
sudo fc-cache -fv
printBold '- Cleaning up'
rm -rf ./fonts