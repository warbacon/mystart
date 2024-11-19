import os
from pathlib import Path
import shutil
from mystart.lib import git


def apply_configs(configs: str | list[str], repo: str = "warbacon/dotfiles"):
    if isinstance(configs, str):
        configs = [configs]

    dotfiles_dir = "/tmp/dotfiles"

    if not os.path.exists(dotfiles_dir):
        git.github_clone(repo, dotfiles_dir)

    for config in configs:
        config_path = f"{dotfiles_dir}/config/{config}"
        if Path(config_path).is_dir():
            try:
                shutil.copytree(
                    f"{dotfiles_dir}/config/{config}",
                    f"{os.getenv("HOME")}/.config/{config}",
                )
            except:
                print(f"Config '{config}' already applied.")
        elif Path(config_path).is_file():
            try:
                shutil.copy(config_path, f"{os.getenv("HOME")}/.config/{config}")
            except shutil.SameFileError:
                print(f"Config '{config}' already applied.")
