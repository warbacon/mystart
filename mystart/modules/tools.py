from mystart.lib import pacman
from mystart.lib.personal import apply_configs


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


def run():
    pacman.install_packages(packages)
    apply_configs("starship.toml")
