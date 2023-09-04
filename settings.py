from menu_handler import menu_handler

WIDTH = 15
HEIGHT = 15
MINE_COUNT = 30

def settings_menu():
    while menu_handler("Settings", {
        f"Set Width ({WIDTH})": set_width,
        "Back": (lambda : None)
    }) != "Back":
        pass

def set_width():
    new_width_str = input("New Width: ")

    if not new_width_str.isnumeric():
        print("Failed: width must be a positive whole number.")
        return

    new_width = int(new_width_str)

    if new_width < 1:
        print("Failed: width is too small.")
        return

    if new_width > 20:
        print("Failed: width is too large.")
        return

    global WIDTH
    WIDTH = new_width
