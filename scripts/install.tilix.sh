#!/bash/bin

#!title: Install Tilix
#!description
# Install tilix (ex terminix) terminal emulator and get the latest dconf file
# from the repository to set it up properly
#!end-description
source ./utils

printBold 'Installing tilix...'
sudo apt-get -qq install tilix -y
printBold 'Fetching dconf...'
curl -L https://raw.githubusercontent.com/dinghino/linux-config/master/configs/tilix.dconf > ./tilix.dconf
dconf load /com/gexperts/Tilix < ./tilix.dconf
rm -rf ./tilix.dconf

