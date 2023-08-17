from typing import Dict, Callable

from generate_board import generate_board, generate_covers
from display_board import display_board

WIDTH = 15
HEIGHT = 15
MINE_COUNT = 30

def menu_handler(options: Dict[str, Callable[[], None]]) -> str:
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = ""
    option_numbers = [str(i+1) for i in range(len(options))]   # ["1", "2", ...]
    while choice not in option_numbers:
        choice = input("->")

    # call function of selected option
    options[list(options)[int(choice)-1]]()

    return list(options)[int(choice)-1]

def main_menu():
    while menu_handler({
        "Play": play_minesweeper,
        "Settings": settings_menu,
        "Exit": (lambda : None)
    }) != "Exit":
        pass

def play_minesweeper():
    board = generate_board(WIDTH, HEIGHT, MINE_COUNT)
    covered = generate_covers(WIDTH, HEIGHT)

    # test
    covered[1][1] = False
    covered[1][2] = False
    covered[2][1] = False
    covered[2][2] = False

    display_board(board, covered)

def settings_menu():
    print("[todo] settings")


if __name__ == "__main__":
    main_menu()
