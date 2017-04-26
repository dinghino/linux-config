function notify {
        echo
        echo '=== ${1} ==='
        echo
}


notify 'Installing oh my fish...'
curl -L https://get.oh-my.fish | fish
omf install agnoster

cd ~/.config/fish

notify 'Installing NVM Fish wrapper...'
git clone git://github.com/passcod/nvm-fish-wrapper.git nvm-wrapper
echo "shource ~/.config/fish/nvm-wrapper/nfm.fish" >> ./config.fish

notify 'Installing VirtualFish...'
python3.6 -m pip install virtualfish
echo "eval(python3.6 -m virtualfish)" >> ./config.fish

notify 'Setting fish as default shell...'
sudo chsh -s `which fish`
