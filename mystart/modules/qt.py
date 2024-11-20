from mystart.lib import pacman
from mystart.lib.base import ModuleBase
from mystart.lib.personal import apply_configs
from typing import final, override


@final
class Qt(ModuleBase):
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

    @override
    def run(self) -> None:
        pacman.install_packages(self.packages)
        apply_configs(self.configs)
