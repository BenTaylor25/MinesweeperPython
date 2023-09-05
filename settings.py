from menu_handler import menu_handler

WIDTH = 15
HEIGHT = 15
MINE_COUNT = 30

def settings_menu():
    while menu_handler("Settings", {
        f"Set Width ({WIDTH})": set_width,
        f"Set Height ({HEIGHT})": set_height,
        f"Set Mine Count ({MINE_COUNT})": set_mine_count,
        "Back": (lambda : None)
    }) != "Back":
        pass


def set_width():
    new_width = get_setting_as_int_in_range("width", 20)

    if new_width != -1:
        global WIDTH
        WIDTH = new_width

def set_height():
    new_height = get_setting_as_int_in_range("height", 20)

    if new_height != -1:
        global HEIGHT
        HEIGHT = new_height

def set_mine_count():
    new_mine_count = get_setting_as_int_in_range("mine count", 300)

    if new_mine_count > WIDTH * HEIGHT:
        print("Failed: Mine Count cannot be greater than the number of tiles on the grid.")
        return

    if new_mine_count != -1:
        global MINE_COUNT
        MINE_COUNT = new_mine_count


def get_setting_as_int_in_range(setting_name: str, max_value: int) -> int:
    new_value_str = input(f"New {setting_name.capitalize()}: ")

    if not new_value_str.isnumeric():
        print(f"Failed: {setting_name} must be a positive whole number.")
        return -1

    new_value = int(new_value_str)

    if new_value < 1:
        print(f"Failed: {setting_name} is too small.")
        return -1

    if new_value > max_value:
        print(f"Failed: {setting_name} is too large.")
        return -1
    
    return new_value
