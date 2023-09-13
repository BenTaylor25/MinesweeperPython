from typing import List

from generate_board import MINE
from apply_to_neighbours import apply_to_neighbours


UNCOVERED = 0
COVERED = 1
FLAGGED = 2

def uncover_tile(
    row: int,
    col: int,
    board: List[List[int]],
    covered: List[List[int]]
):
    if covered[row][col] == COVERED:
        covered[row][col] = UNCOVERED

        if board[row][col] == 0:
            callback = lambda b, r, c : uncover_tile(r, c, b, covered)
            apply_to_neighbours(board, row, col, callback)

def flag_tile(row: int, col: int, covered: List[List[int]]):
    if covered[row][col] == COVERED:
        covered[row][col] = FLAGGED

    elif covered[row][col] == FLAGGED:
        covered[row][col] = COVERED
