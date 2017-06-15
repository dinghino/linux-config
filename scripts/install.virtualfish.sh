#!/usr/bin/fish
#!~SAVE

#!title: Install Fish shell - virtualfish
#!description
# VirtualFish works as virtualenwrapper, but for fish shell.
# This scripts installs the wrapper for python 3.6 if available on the system,
# else it uses python 2.7.
# To use virtual fish
#!end-description

source ./utils.sh

if which python3.6 > /dev/null
    python3.6 -m pip install virtualfish
    eval (python3.6 -m virtualfish)
else
    pip install virtualfish
    eval (python -m virtualfish)
end
