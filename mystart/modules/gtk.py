import os
from mystart.lib.system import gsettings_set


def run():
    gsettings_set("org.gnome.desktop.interface", "color-scheme", "prefer-dark")
    gsettings_set("org.gnome.desktop.interface", "font-name", "'Inter Variable 10'")

    gtk3_dir = f"{os.getenv("HOME")}/.config/gtk-3.0"
    gtk3_config = f"{os.getenv("HOME")}/.config/gtk-3.0/settings.ini"

    try:
        os.mkdir(gtk3_dir)
    except FileExistsError:
        print(f"Directory '{gtk3_dir}' already exists.")

    with open(gtk3_config, "w") as f:
        # fmt: off
        _ = f.write(
"""[Settings]
gtk-application-prefer-dark-theme = true"""
        )
        # fmt: on
