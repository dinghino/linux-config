#!/bin/bash
#!~SAVE

#!title: Install htop
#!description
# Graphic alternative to top and htop. Cool graphs, simpler interface and
# options but shows everything nice.
#
# =================================== NOTE ===================================
# vtop runs on a node.js environment. Installation of Node is not provided yet
# through these scripts. If working with Fish Shell there's a cool wrapper
# (NVM) that can be easily installed with the `install.nvm.sh` script.
# For further instructions on how to setup a node.js env with nvm see the
# relative script description.
#!end-description

if which npm > /dev/null; then
    npm install -g vtop
else
    print 'NPM Not found. Cannot install vtop.'
fi