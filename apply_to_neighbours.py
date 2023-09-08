from typing import List, Callable

def apply_to_neighbours(
    board: List[List[int]],
    row: int, col: int,
    callback: Callable[[List[List[int]], int, int], None]
):
    n_row_min = max(0, row - 1)
    n_row_max = min(len(board[0]) - 1, row + 1)

    n_col_min = max(0, col - 1)
    n_col_max = min(len(board) - 1, col + 1)

    for n_row in range(n_row_min, n_row_max + 1):
        for n_col in range(n_col_min, n_col_max + 1):
            callback(board, n_row, n_col)
