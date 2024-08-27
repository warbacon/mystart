#!/bin/bash

command_exists() {
    command -v "$@" >/dev/null 2>&1
}

install_packages() {
    if command_exists paru; then
        paru -S "$@" --noconfirm --needed
    else
        sudo pacman -S "$@" --noconfirm --needed
    fi
}

clone_repo() {
    if ! command_exists git; then
        install_packages git
    fi

    if [[ ! -d $2 ]]; then
        git clone "$@"
    fi
}
