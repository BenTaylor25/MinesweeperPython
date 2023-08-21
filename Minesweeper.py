from typing import Dict, Callable

from dependency_importer import dep_import
dep_import("pynput")
from pynput.keyboard import Key, Listener

from generate_board import generate_board, generate_covers
from display_board import display_board
from uncover_tile import uncover_tile
from keyboard_input import get_cursor_command, CursorAction

WIDTH = 15
HEIGHT = 15
MINE_COUNT = 30

def menu_handler(options: Dict[str, Callable[[], None]]) -> str:
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = ""
    option_numbers = [str(i+1) for i in range(len(options))]   # ["1", "2", ...]
    while choice not in option_numbers:
        choice = input("-> ")

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
    cursor = (0, 0)

    # uncover_tile(1, 1, board, covered)

    while True:
        display_board(board, covered, cursor)
        cmd = get_cursor_command()

        if cmd == CursorAction.UP and cursor[0] > 0:
            cursor = (cursor[0] - 1, cursor[1])
        elif cmd == CursorAction.DOWN and cursor[0] < HEIGHT - 1:
            cursor = (cursor[0] + 1, cursor[1])

def settings_menu():
    print("[todo] settings")


# test
def on_press(key):
    print('{0} pressed'.format(key))

    if key == Key.esc:
        return False

if __name__ == "__main__":
    main_menu()
