import subprocess
from shutil import which

from . import pacman


def gsettings_set(path: str, key: str, value: str):
    if which("gsettings") is None:
        pacman.install_packages("glib2")
    _ = subprocess.run(["gsettings", "set", path, key, value])
