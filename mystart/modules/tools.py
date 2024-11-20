from typing import final, override
from mystart.lib import pacman
from mystart.lib.base import ModuleBase
from mystart.lib.personal import apply_configs


@final
class Tools(ModuleBase):
    packages = [
        "base-devel",
        "btop",
        "curl",
        "dust",
        "eza",
        "fastfetch",
        "fd",
        "fish",
        "fzf",
        "git",
        "hyperfine",
        "jq",
        "lazygit",
        "less",
        "man-db",
        "man-pages",
        "man-pages-es",
        "mpv",
        "p7zip",
        "ripgrep",
        "starship",
        "tealdeer",
        "trash-cli",
        "wget",
    ]

    @override
    def run(self) -> None:
        pacman.install_packages(self.packages)
        apply_configs("starship.toml")
