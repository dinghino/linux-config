#!/bin/bash
#!~SAVE

#!title: Install Solaar
#!description
# Solaar is a linux manager for the Logitech Unifying technology and allows
# some degree of control and customization on Logitech devices that relies
# on that tech.
#!end-description


sudo add-apt-repository ppa:daniel.pavel/solaar
sudo apt-get update && sudo apt-get install solaar-gnome3