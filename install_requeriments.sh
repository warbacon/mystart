#!/bin/bash

sudo pacman -S ansible-core

ansible-galaxy collection install -r requirements.yml
