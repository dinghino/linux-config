BOLD=$(tput bold)
NORMAL=$(tput sgr0)

function notify {
    echo $BOLD
    echo '============================================='
    echo  " ${1}"
    echo '============================================='
    echo $NORMAL
}
function setupRepositories {
    # Add ppa repositories required
    # TODO: Check distribution version and add optional ppa for python3.6
    #       As of now this will assume 16.10+
    sudo add-apt-repository ppa:fish-shell/release-2 -y
    sudo add-apt-repository ppa:webupd8team/terminix -y
    sudo apt-get update
}
function installDependecies {
    # Install ALL the dependecies required by the rule-them-all-script
    sudo apt-get install xsel git curl vim unzip python3.6 build-essential cmake python-dev python3-dev -y
}
function installFonts {
    # Install fonts
    mkdir /tmp/fonts/
    cd /tmp/fonts/
    # Get the fonts needed
    echo "${BOLD}- Fetching Inconsolata...${NORMAL}"
    curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Inconsolata.zip >> ./inconsolata.zip
    echo "${BOLD}- Fetching Monofur...${NORMAL}"
    curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Monofur.zip >> ./monofur.zip
    echo "${BOLD}- Fetching Firacode...${NORMAL}"
    curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/FiraCode.zip >> ./firacode.zip

    sudo unzip '*.zip' -d ~/.local/share/fonts
    sudo fc-cache -fv
    cd ..
    rm -rf ./fonts
}
function installTilix {
    sudo apt-get install tilix -y
    # FIXME: This should do something! ?_?
    dconf load /com/gexeperts/Tilix/ < ./configs/tilix.dconf
}
function installNVM {
    echo "${BOLD}- Fetching nvm...${NORMAL}"
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
}
function installFish {
    sudo apt-get install fish -y

    notify 'Installing NVM Fish wrapper...'
    git clone git://github.com/passcod/nvm-fish-wrapper.git ~/.config/fish/nvm-wrapper

    notify 'Installing VirtualFish...'
    python3.6 -m pip install virtualfish

    echo "- ${BOLD} Updating config.fish...${NORMAL}"
    # NOTE: Add the source for nvm fish wrapper - This will be already present in the 
    # config.fish present in the repo once its there
    echo "eval(python3.6 -m virtualfish)" >> ~/.config/fish/config.fish
    echo source ~/.config/fish/nvm-wrapper/nvm.fish >> ~/.config/fish/config.fish

    notify 'Installing OhMyFish and Agnoster theme...'
    curl -L https://get.oh-my.fish | fish | omf install agnoster | exit
}
function configureVIM {
    notify '  Fetching .vimrc file...'
    curl -L https://raw.githubusercontent.com/dinghino/linux-config/master/configs/.vimrc >> ~/.vimrc
    notify '  Installing Plug...'
    curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    notify '  Installing plugins... may take a while'
    vim -c :PlugInstall -c quitall
}