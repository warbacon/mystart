#!/bin/bash

source ./util.sh

packages=(
    "hyprland"
    "kitty"
    "rofi-wayland"
    "waybar"
    "xdg-user-dirs"
    "xdg-desktop-portal-gtk"
    "xdg-desktop-portal-hyprland"
)

./setup_gtk.sh

install_packages "${packages[@]}"

xdg-user-dirs-update
