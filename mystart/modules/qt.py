from mystart.lib import pacman
from mystart.lib.personal import apply_configs

packages = [
    "qt5-wayland",
    "qt6-wayland",
    "breeze-icons",
    "qt5ct",
    "qt6ct",
]

configs = [
    "qt5ct",
    "qt6ct",
]


def run():
    pacman.install_packages(packages)
    apply_configs(configs)
