from typing import List

from apply_to_neighbours import apply_to_neighbours_2

def uncover_tile(row: int, col: int, board: List[List[int]], covered: List[List[bool]]):
    if covered[row][col]:
        covered[row][col] = False

        if board[row][col] == 0:
            apply_to_neighbours_2(row, col, uncover_tile, board, covered)
