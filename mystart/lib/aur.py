from shutil import which
import subprocess
from mystart.lib import git


def install_paru():
    if which("paru") is None:
        git.clone("https://aur.archlinux.org/paru-bin.git", "/tmp/paru-bin")
        _ = subprocess.run(["makepkg", "-si"], text=True, cwd="/tmp/paru-bin")


def install_packages(packages: str | list[str], asdeps: bool = False) -> None:
    install_paru()

    if isinstance(packages, str):
        packages = [packages]

    command = ["paru", "-Sa", "--needed", "--noconfirm"]
    if asdeps:
        command.append("--asdeps")

    command += packages

    _ = subprocess.run(command, text=True)
