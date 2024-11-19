import os
from mystart.lib import pacman, git

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


def run():
    pacman.install_packages(packages)
    git.github_clone("warbacon/config", f"{os.getenv("HOME")}/.config/nvim")
