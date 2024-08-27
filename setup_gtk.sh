#!/bin/bash

source ./util.sh

if ! command_exists paru; then
    ./paru.sh
fi

install_packages ttf-inter

gsettings set org.gnome.desktop.interface color-scheme prefer-dark
gsettings set org.gnome.desktop.interface font-name "Inter 11"
gsettings set org.gnome.desktop.wm.preferences button-layout :

if [[ ! -d "$HOME/.config/gtk-3.0" ]]; then
    mkdir -p "$HOME/.config/gtk-3.0"
fi

if [[ ! -f "$HOME/.config/gtk-3.0/settings.ini" ]]; then
    echo -e "[Settings]\ngtk-application-prefer-dark-theme = true" >"$HOME/.config/gtk-3.0/settings.ini"
fi
