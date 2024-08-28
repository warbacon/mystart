#!/bin/bash

source ./util.sh

clone_repo https://github.com/warbacon/nvim-config ~/.config/nvim
install_packages neovim

dependencies=(
    curl
    fd
    nodejs-lts-iron
    npm
    python
    ripgrep
    unzip
    wget
    wl-clipboard
)

install_packages "${dependencies[@]}"
