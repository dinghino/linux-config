#!/bin/bash
#!~SAVE

#!title: Install IPython 2/3
#!description
# This scripts installs the IPython interpreter in full for both python 2.7
# and, if present, python3.6
#!end-description

source ./utils.sh

printBold 'Installing IPython for python 2.7...'
sudo pip install ipython[all]

if [ $(./apt.exists.sh pip3) == 1 ]; then
    printBold 'Installing IPython for python 3...'
    sudo pip3 install ipython[all]
fi
