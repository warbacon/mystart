from mystart.modules.fonts import Fonts
from mystart.modules.gtk import GTK
from mystart.modules.hyprland import Hyprland
from mystart.modules.neovim import Neovim
from mystart.modules.qt import Qt
from mystart.modules.tools import Tools
from mystart.modules.amd import AMD


def main():
    modules = [AMD(), Fonts(), Hyprland(), Tools(), Neovim(), GTK(), Qt()]
    for module in modules:
        module.run()


if __name__ == "__main__":
    main()
