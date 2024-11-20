from mystart.lib import pacman
from shutil import which
import subprocess


def gsettings_set(path: str, key: str, value: str):
    if which("gsettings") is None:
        pacman.install_packages("glib2")
    _ = subprocess.run(["gsettings", "set", path, key, value])
