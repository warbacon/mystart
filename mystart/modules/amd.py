from mystart.lib import pacman


packages = [
    "mesa",
    "rocm-smi-lib",
    "vulkan-radeon",
]


def run():
    pacman.install_packages(packages)
