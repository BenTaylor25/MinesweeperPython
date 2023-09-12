from dependency_importer import install_all
install_all(["pynput", "colorama"])

from menu_handler import menu_handler
from clear_screen import clear_screen
from generate_board import generate_board, generate_covers
from display_board import display_board
from settings import settings_menu
from tile_actions import uncover_tile, flag_tile
from check_game_over import check_game_over
from keyboard_input import get_cursor_command, CursorAction
from logger import clear_log, log_message


def main_menu():
    while menu_handler("Main Menu", {
        "Play": play_minesweeper,
        "Settings": settings_menu,
        "Exit": (lambda : None)
    }) != "Exit":
        pass

def play_minesweeper():
    from settings import WIDTH, HEIGHT, MINE_COUNT
    log_message(f"started game - {WIDTH}x{HEIGHT} board with {MINE_COUNT} mines")

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
            log_message("moving up")
            cursor = (cursor[0] - 1, cursor[1])
        elif cmd == CursorAction.DOWN and cursor[0] < HEIGHT - 1:
            log_message("moving down")
            cursor = (cursor[0] + 1, cursor[1])
        elif cmd == CursorAction.LEFT and cursor[1] > 0:
            log_message("moving left")
            cursor = (cursor[0], cursor[1] - 1)
        elif cmd == CursorAction.RIGHT and cursor[1] < WIDTH - 1:
            log_message("moving right")
            cursor = (cursor[0], cursor[1] + 1)
        elif cmd == CursorAction.UNCOVER:
            log_message(f"uncovering tile ({cursor[0]},{cursor[1]}) - {board[cursor[0]][cursor[1]]}")
            uncover_tile(*cursor, board, covered)
        elif cmd == CursorAction.FLAG:
            log_message(f"flagging tile ({cursor[0]},{cursor[1]}) - {board[cursor[0]][cursor[1]]}")
            flag_tile(*cursor, covered)

        game_over, game_won = check_game_over(board, covered)

    clear_screen()
    display_board(board, covered, cursor)

    if game_won:
        log_message("Game Over : Win")
        print("\nYou Win\n")
    else:
        log_message("Game Over : Loss")
        print("\nGame Over\n")
    input()


if __name__ == "__main__":
    clear_log()
    main_menu()
