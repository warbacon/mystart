from mystart.lib import pacman, git
from mystart.lib.base import ModuleBase
from typing import final, override
import os


@final
class Neovim(ModuleBase):
    packages = [
        "curl",
        "gcc",
        "make",
        "neovim",
        "npm",
        "python",
        "ripgrep",
        "unzip",
        "wget",
        "wl-clipboard",
    ]

    @override
    def run(self) -> None:
        pacman.install_packages(self.packages)
        git.github_clone("warbacon/nvim-config", f"{os.getenv("HOME")}/.config/nvim")
