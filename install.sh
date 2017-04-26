#!/bin/bash

# Ubuntu bootstrapper for python3.6/node.js environment
# written by Daniele Calcinai Apr - 2017
# Github repository: https://github.com/dinghino/linux-config

# Print out a readable header telling what is happening.
# Will be most probably refactored in something more cool
function notify {
    echo
    echo '======================================'
    echo  >  $1
    echo '======================================'
    echo
}

# Store the current directory so that we can get back here
CWD=$PWD

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
sudo unzip '*.zip' -d ~/.local/share/fonts
sudo fc-cache -fv
cd ..
rm -rf ./fonts

#############################
#       Tilix emulator      #
#############################
notify 'Installing tilix...'
sudo apt-get install tilix -y
dconf load /com/gexeperts/Terminix/ < ./configs/tilix.dconf

#############################
#       NVM Install         #
#############################
notify 'Installing Node Version Manager...'
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash

# TODO: This dump of stuff inside config.fish will be removed, and the file
# Will be recovered from the repo every time

##############################
#     VIM Configuration      #
##############################

notify 'Configuring VIm...'
notify '  Installing Vundle...'
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
notify '  Updating .vimrc file...'
wget https://raw.githubusercontent.com/dinghino/linux-config/master/configs/.vimrc -d ~/.vimrc
notify '  Installing plugins...'
vim +PluginInstall +qall
notify '  Compiling YouCompleteMe plugin...\nit may take a while.'
cd ~/.vim/bundle/YouCompleteMe
sudo python3.6 -m ./install --clang-completer --tern-completer

##############################
#   Installing Fish shell    #
#       and utilities        #
##############################

notify 'Installing fish shell...'
sudo apt-get install fish -y
notify 'Installing NVM Fish wrapper...'
cd ~/.config/fish
git clone git://github.com/passcod/nvm-fish-wrapper.git nvm-wrapper
# Add the source for nvm fish wrapper
echo source ~/.config/fish/nvm-wrapper/nvm.fish >> ./config.fish

# OhMyFish

notify 'Installing Oh-My-Fish...'
curl -L https://get.oh-my.fish
# Create config.fish if it does not exists
if [ ! -f ./config.fish ];then
        touch ./config.fish
fi

notify 'Installing VirtualFish...'
python3.6 -m pip install virtualfish
echo "eval(python3.6 -m virtualfish)" >> ./config.fish


##############################
#     Finalize Fish setup    #
##############################

notify 'Finalizing fish installation...'
fish
omf install agnoster
notify 'Setting fish as default shell...'
sudo chsh -s `which fish`
##############################
#     VIM Configuration      #
##############################
notify 'Configuring VIm...'
notify '  Fetching .vimrc file...'
curl -L https://raw.githubusercontent.com/dinghino/linux-config/master/configs/.vimrc >> ~/.vimrc
notify '  Installing Plug...'
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
notify '  Installing plugins...'
vim -c :PlugInstall -c quitall
