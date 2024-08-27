#!/bin/bash

source ./util.sh

clone_repo https://aur.archlinux.org/paru-bin.git /tmp/paru-bin \
    && cd /tmp/paru-bin || exit
makepkg -si
