from mystart.lib import pacman
from mystart.lib.base import ModuleBase
from typing import final, override


@final
class AMD(ModuleBase):
    packages = [
        "mesa",
        "rocm-smi-lib",
        "vulkan-radeon",
    ]

    @override
    def run(self) -> None:
        pacman.install_packages(self.packages)
