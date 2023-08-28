import os
from typing import Dict, Callable

from dependency_importer import dep_import
dep_import("pynput")
from pynput.keyboard import Key, Listener

from generate_board import generate_board, generate_covers
from display_board import display_board
from tile_actions import uncover_tile, flag_tile
from check_game_over import check_game_over
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

    game_over = False
    while not game_over:
        clear_screen()
        display_board(board, covered, cursor)
        cmd = get_cursor_command()

        if cmd == CursorAction.UP and cursor[0] > 0:
            cursor = (cursor[0] - 1, cursor[1])
        elif cmd == CursorAction.DOWN and cursor[0] < HEIGHT - 1:
            cursor = (cursor[0] + 1, cursor[1])
        elif cmd == CursorAction.LEFT and cursor[1] > 0:
            cursor = (cursor[0], cursor[1] - 1)
        elif cmd == CursorAction.RIGHT and cursor[1] < WIDTH - 1:
            cursor = (cursor[0], cursor[1] + 1)
        elif cmd == CursorAction.UNCOVER:
            uncover_tile(*cursor, board, covered)
        elif cmd == CursorAction.FLAG:
            flag_tile(*cursor, covered)

        game_over = check_game_over(board, covered)

    clear_screen()
    display_board(board, covered, cursor)
    print("\nGame Over\n")

def clear_screen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def settings_menu():
    print("[todo] settings")


# test
def on_press(key):
    print('{0} pressed'.format(key))

    if key == Key.esc:
        return False

if __name__ == "__main__":
    main_menu()
