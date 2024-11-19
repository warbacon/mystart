from mystart.lib import aur, pacman
from mystart.lib.personal import apply_configs


aur_fonts = ["ttf-inter"]

fonts = ["ttf-jetbrains-mono", "ttf-nerd-fonts-symbols"]


def run():
    aur.install_packages(aur_fonts)
    pacman.install_packages(fonts)
    apply_configs("fontconfig")
