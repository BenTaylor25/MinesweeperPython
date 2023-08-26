from typing import List

from apply_to_neighbours import apply_to_neighbours_2
from generate_board import MINE

UNCOVERED = 0
COVERED = 1
FLAGGED = 2

def uncover_tile(row: int, col: int, board: List[List[int]], covered: List[List[int]]) -> bool:
    if covered[row][col] == COVERED:
        covered[row][col] = UNCOVERED

        if board[row][col] == 0:
            apply_to_neighbours_2(row, col, uncover_tile, board, covered)
        elif board[row][col] == MINE:
            return True

    return False

def flag_tile(row: int, col: int, covered: List[List[int]]):
    if covered[row][col] == COVERED:
        covered[row][col] = FLAGGED

    elif covered[row][col] == FLAGGED:
        covered[row][col] = COVERED
