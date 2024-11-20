from shutil import which
import subprocess
from mystart.lib import pacman


def clone(url: str, directory: str = ""):
    if which("git") is None:
        pacman.install_packages("git")

    command = ["git", "clone", url]

    if directory:
        command.append(directory)

    _ = subprocess.run(command, text=True)


def github_clone(repo: str, directory: str = ""):
    clone(f"https://github.com/{repo}", directory)
