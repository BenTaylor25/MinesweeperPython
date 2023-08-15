from typing import List, Callable

def apply_to_neighbours(board: List[List[int]], row: int, col: int, callback: Callable[[List[List[int]], int, int], None]):
    can_go_left = col > 0
    can_go_right = col < len(board[0]) - 1
    can_go_up = row > 0
    can_go_down = row < len(board) - 1
    
    if can_go_up:
        if can_go_left:
            callback(board, row - 1, col - 1)

        callback(board, row - 1, col)

        if can_go_right:
            callback(board, row - 1, col + 1)

    if can_go_left:
        callback(board, row, col - 1)

    if can_go_right:
        callback(board, row, col + 1)

    if can_go_down:
        if can_go_left:
            callback(board, row + 1, col - 1)

        callback(board, row + 1, col)

        if can_go_right:
            callback(board, row + 1, col + 1)

