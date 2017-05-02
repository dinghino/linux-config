source ./utils.sh

CWD=$PWD

function setupRepositories {
    # Add ppa repositories required
    # TODO: Check distribution version and add optional ppa for python3.6
    #       As of now this will assume 16.10+
    printBold 'Adding repositories'
    sudo add-apt-repository ppa:fish-shell/release-2 -y
    sudo add-apt-repository ppa:webupd8team/terminix -y
    printBold 'Updating...'
    sudo apt-get update
}
function installDependecies {
    printBold 'Installing...'
    # Install ALL the dependecies required by the rule-them-all-script
    sudo apt-get install xsel git curl vim unzip python3.6 python3-pip build-essential cmake python-dev python3-dev -y
}
function installFonts {
    # Install fonts
    mkdir /tmp/fonts/
    cd /tmp/fonts/
    # Get the fonts needed
    printBold '- Fetching Inconsolata...'
    curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Inconsolata.zip >> ./inconsolata.zip
    printBold '- Fetching Monofur...'
    curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/Monofur.zip >> ./monofur.zip
    printBold '- Fetching Firacode...'
    curl -L https://github.com/ryanoasis/nerd-fonts/releases/download/v1.0.0/FiraCode.zip >> ./firacode.zip
    printBold '- Unpacking...'
    sudo unzip '*.zip' -d ~/.local/share/fonts
    printBold '- Updating font cache (reload terminal to use new fonts)'
    sudo fc-cache -fv
    printBold '- Cleaning up'
    cd ..
    rm -rf ./fonts
}
function installTilix {
    printBold 'Fetching...'
    sudo apt-get install tilix -y
    printBold 'Restoring profile'
    # FIXME: This should do something! ?_?
    cd $CWD
    dconf load /com/gexeperts/Tilix/ < ./configs/tilix.dconf
}
function installNVM {
    printBold "- Fetching nvm..."
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
}
function installFish {
    printBold 'Installing fish...'
    sudo apt-get install fish -y

    printBold 'Installing NVM Fish wrapper...'
    git clone git://github.com/passcod/nvm-fish-wrapper.git ~/.config/fish/nvm-wrapper

    printBold 'Installing VirtualFish...'
    python3.6 -m pip install virtualfish

    printBold "- Updating config.fish..."
    # NOTE: Add the source for nvm fish wrapper - This will be already present in the
    # config.fish present in the repo once its there
    echo "eval (python3.6 -m virtualfish)" >> ~/.config/fish/config.fish
    echo source ~/.config/fish/nvm-wrapper/nvm.fish >> ~/.config/fish/config.fish
    printBold 'Setting fish as default shell'
    chsh -s `which fish`
    printBold 'Installing oh my fish...'
    cd $CWD
    fish ./scripts/configure.fish.sh
}
function configureVIM {
    printBold '- Fetching .vimrc file...'
    curl -L https://raw.githubusercontent.com/dinghino/linux-config/master/configs/.vimrc >> ~/.vimrc
    printBold '- Installing Plug...'
    curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    printBold '- Installing plugins... may take a while'
    vim -c :PlugInstall -c quitall
}
