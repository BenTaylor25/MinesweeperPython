from typing import Dict, Callable

WIDTH = 15
HEIGHT = 15
MINES = 30

def menu_handler(options: Dict[str, Callable[[], None]]) -> str:
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = ""
    option_numbers = [str(i+1) for i in range(len(options))]   # ["1", "2", ...]
    while choice not in option_numbers:
        choice = input("->")

    # call function of selected option
    options[list(options)[int(choice)-1]]()

    return choice

def main_menu():
    while menu_handler({
        "Play": play_minesweeper,
        "Settings": settings_menu,
        "Exit": (lambda : None)
    }) != "3":
        pass

def play_minesweeper():
    pass

def settings_menu():
    print("[todo] settings")


if __name__ == "__main__":
    main_menu()