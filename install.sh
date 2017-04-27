#!/bin/bash

# Ubuntu bootstrapper for python3.6/node.js environment
# written by Daniele Calcinai Apr - 2017
# Github repository: https://github.com/dinghino/linux-config

# Print out a readable header telling what is happening.
# Will be most probably refactored in something more cool

# Store the current directory so that we can get back here
CWD=$PWD
source ./scripts/installers.sh
# TODO: Interactive mode with menus

#############################
#    Install dependecies    #
#############################
notify ='Installing dependecies...'
setupRepositories
installDependecies

#############################
#       Required fonts      #
#############################
notify 'Installing fonts...'
installFonts

#############################
#       Tilix emulator      #
#############################
notify 'Installing tilix...'
installTilix

#############################
#       NVM Install         #
#############################
notify 'Installing Node Version Manager...'
installNVM

##############################
#   Installing Fish shell    #
#       and utilities        #
##############################
notify 'Installing fish shell...'
installFish

##############################
#     VIM Configuration      #
##############################
notify 'Configuring VIm...'
configureVIM

notify 'Installation completed.'
printBold 'Now you should...'
printBold '- activate virtualfish. type `vf` from `fish shell`'
printBold '- validate fish theme. explore them with `omf theme`'
printBold '- ensure themes for terminals are set. Use a patched font.'
printBold "- Use tilix! That's awesome"

