#!/bin/bash

# Simple script that takes the name of a package as argument and returns 1
# if the package is installed or 0 otherwise
# Args:
#   $1: package to check
echo $(dpkg-query -W -f='${Status}' $1 2>/dev/null | grep -c "ok installed")