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
    new_width = get_int_in_range("width", 20)
    if new_width != -1:
        global WIDTH
        WIDTH = new_width

def get_int_in_range(setting_name: str, max_value: int) -> int:
    new_value_str = input(f"New {setting_name.capitalize()}: ")

    if not new_value_str.isnumeric():
        print(f"Failed: {setting_name} must be a positive whole number.")
        return -1

    new_value = int(new_value_str)

    if new_value < 1:
        print(f"Failed: {setting_name} is too small.")
        return -1

    if new_value > 20:
        print(f"Failed: {setting_name} is too large.")
        return -1
    
    return new_value
