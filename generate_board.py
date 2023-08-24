from typing import List
from random import randint

from apply_to_neighbours import apply_to_neighbours

MINE = -1

def generate_board(width: int, height: int, mine_count: int) -> List[List[int]]:
    assert width * height >= mine_count, "cannot place more mines than tiles on the board"

    board = [[0 for _ in range(width)] for _ in range(height)]

    place_mines(board, mine_count)
    calculate_values(board)

    return board

def place_mines(board: List[List[int]], mine_count: int):
    mines_placed = 0
    while mines_placed < mine_count:
        y = randint(0, len(board)-1)
        x = randint(0, len(board[y])-1)

        if board[y][x] != MINE:
            board[y][x] = MINE
            mines_placed += 1

def calculate_values(board: List[List[int]]):
    """
        Locate all mines.
        Foreach: increment all non-mine neighbours.

        [This step could be integrated into place_mines()]
    """
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == MINE:
                # print(f"\nCaller: {row}, {col}")
                apply_to_neighbours(board, row, col, _increment_if_not_mine)

def _increment_if_not_mine(board, row, col):
    if board[row][col] != MINE:
        board[row][col] += 1
        # print(f"{row}, {col} ({board[row][col]})")

def generate_covers(width: int, height: int) -> List[List[bool]]:
    return [[1 for _ in range(width)] for _ in range(height)]
