#!/bin/bash

# Menu functions to navigate through the application, allowing an easy to use installer
source ./installers.sh
clear
MAINMENU="Install Configure Status Quit"
INSTALLMENU="Dependecies Fonts Tilix VSCode Fish&Stuff Back Quit"

function quit {
    echo ByeBye
    exit
}

function mainmenu {
    echo System bootstrap to rule them all
    echo Select your option

    select opt in $MAINMENU;
    do
        if [ "$opt" = "Install" ]; then
            installmenu
        elif [ "$opt" = "Configure" ]; then
            clear
            echo "Configure stuff (Show menu)"
            mainmenu
        elif [ "$opt" = "Status" ]; then
            clear
            echo "Logging rule-them-all status"
            mainmenu
        elif [ "$opt" = "Quit" ]; then
            quit
        else
            clear
            echo "Command not recognized. Try again."
            mainmenu
        fi
    done
}

function installmenu {
    clear
    echo What do you need to install?
    echo

    select opt in $INSTALLMENU;
    do
        if [ "$opt" = "Dependecies" ]; then
            echo "Installing dependecies (List dependecies too)"
            setupRepositories
            installDependecies
            installmenu
        elif [ "$opt" = "Fonts" ]; then
            echo "Installing fonts (List fonts)"
            installFonts
            installmenu
        elif [ "$opt" = "Tilix" ]; then
            echo "Installing Tilix (no configure)"
            installTilix
            installmenu
        elif [ "$opt" = "VSCode" ]; then
            echo "Installing Visual Studio Code"
            installmenu
        elif [ "$opt" = "Fish&Stuff" ]; then
            echo "Installing Fish shell and OhMyFish"
            installFish
            installmenu
        elif [ "$opt" = Back ]; then
            mainmenu
        elif [ "$opt" = "Quit" ]; then
            quit
        else
            echo Command not recognized. Try Again.
            installmenu
        fi
    done
}

mainmenu

