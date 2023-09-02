from typing import Dict, Callable

from dependency_importer import dep_import
dep_import("pynput")
from pynput.keyboard import Key, Listener

from menu_handler import menu_handler
from clear_screen import clear_screen
from generate_board import generate_board, generate_covers
from display_board import display_board
from tile_actions import uncover_tile, flag_tile
from check_game_over import check_game_over
from keyboard_input import get_cursor_command, CursorAction
from logger import clear_log, log_message

WIDTH = 15
HEIGHT = 15
MINE_COUNT = 30


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

    game_over = False
    game_won = False

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

        game_over, game_won = check_game_over(board, covered)

    clear_screen()
    display_board(board, covered, cursor)

    if game_won:
        print("\nYou Win\n")
    else:
        print("\nGame Over\n")
    input()


def settings_menu():
    print("[todo] settings")


if __name__ == "__main__":
    clear_log()
    main_menu()
