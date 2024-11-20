from mystart.lib import pacman, aur
from mystart.lib.base import ModuleBase
from mystart.lib.personal import apply_configs
from mystart.lib.system import gsettings_set
from typing import final, override
import subprocess


@final
class Hyprland(ModuleBase):
    packages = [
        "brightnessctl",
        "dunst",
        "grim",
        "hypridle",
        "hyprland",
        "hyprlock",
        "hyprpaper",
        "imv",
        "kitty",
        "libcanberra",
        "libnotify",
        "pulsemixer",
        "rofi-wayland",
        "rofimoji",
        "slurp",
        "waybar",
        "wl-clip-persist",
        "wtype",
        "xdg-desktop-portal-gtk",
        "xdg-desktop-portal-hyprland",
        "xdg-user-dirs",
        "yazi",
    ]

    aur_packages = [
        "uwsm",
        "hyprsunset",
    ]

    configs = [
        "waybar",
        "hypr",
        "dunst",
        "rofi",
    ]

    @override
    def run(self) -> None:
        pacman.install_packages(self.packages)
        aur.install_packages(self.aur_packages)

        _ = subprocess.run(["xdg-user-dirs-update"])

        apply_configs(self.configs)

        gsettings_set(
            "org.gnome.desktop.wm.preferences", "button-layout", "'appmenu:none'"
        )
