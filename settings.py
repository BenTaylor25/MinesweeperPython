from menu_handler import menu_handler
from string_helpers import capitalise_words
from logger import log_message

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

    if new_width != INVALID_SETTING:
        global WIDTH
        log_message(f"Changing Width setting from {WIDTH} to {new_width}")
        WIDTH = new_width

def set_height():
    new_height = get_setting_as_int_in_range("height", 20)

    if new_height != INVALID_SETTING:
        global HEIGHT
        log_message(f"Changing Height setting from {HEIGHT} to {new_height}")
        HEIGHT = new_height

def set_mine_count():
    new_mine_count = get_setting_as_int_in_range("mine count", 300)

    if new_mine_count > WIDTH * HEIGHT:
        log_message(f"Failed to set Mine Count setting to {new_mine_count} because >{WIDTH*HEIGHT} (width*height)")
        print("Failed: Mine Count cannot be greater than the number of tiles on the grid.")
        return

    if new_mine_count != INVALID_SETTING:
        global MINE_COUNT
        log_message(f"Changing the Mine Count setting from {MINE_COUNT} to {new_mine_count}")
        MINE_COUNT = new_mine_count


INVALID_SETTING = -1
def get_setting_as_int_in_range(setting_name: str, max_value: int) -> int:
    new_value_str = input(f"New {capitalise_words(setting_name)}: ")

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
