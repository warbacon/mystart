from mystart.lib import aur, pacman
from mystart.lib.base import ModuleBase
from mystart.lib.personal import apply_configs
from typing import final, override


@final
class Fonts(ModuleBase):
    aur_fonts = ["ttf-inter"]
    fonts = ["ttf-jetbrains-mono", "ttf-nerd-fonts-symbols"]

    @override
    def run(self) -> None:
        aur.install_packages(self.aur_fonts)
        pacman.install_packages(self.fonts)
        apply_configs("fontconfig")
