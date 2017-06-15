#!/bin/bash

# Lazy launcher for the rule them all bootstrap cli.
# The script checks if python is installed on the system - as it should - and
# If not installs python 2.7, pip and runs the cli application.

function ensure() {
    local package=${1}
    if [ $(./scripts/apt.exists.sh "${package}") -eq 0 ]
    then
        echo -n "${package} not installed... install? [Y/n] "
        read $REPLY
        REPLY=${REPLY:-Y}  # default is Yes!
        if [[ $REPLY =~ ^[Yy]$ ]]
        then
            echo "Installing as sudo..."
            (sudo apt-get -y install $package)
            # NOTE that if the apt-get fails the program quits :v
        else
            echo "Quitting :("
            exit 1
        fi
    fi
}
ensure "python2.7"
ensure "python-pip"

python ./cli

echo
echo "Goodbye!"