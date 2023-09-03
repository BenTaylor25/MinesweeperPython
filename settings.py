from menu_handler import menu_handler

WIDTH = 15
HEIGHT = 15
MINE_COUNT = 30

def settings_menu():
    while menu_handler("Settings", {
        "Set Width": set_width,
        "Back": (lambda : None)
    }) != "Back":
        pass

def set_width():
    pass
