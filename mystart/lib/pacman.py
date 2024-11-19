import subprocess


def install_packages(packages: str | list[str], asdeps: bool = False) -> None:
    if isinstance(packages, str):
        packages = [packages]

    command = ["sudo", "pacman", "-S", "--needed", "--noconfirm"]
    if asdeps:
        command.append("--asdeps")

    command += packages

    _ = subprocess.run(command, text=True)
