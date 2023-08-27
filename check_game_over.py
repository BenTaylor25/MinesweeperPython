from typing import List

from generate_board import MINE
from tile_actions import UNCOVERED, COVERED, FLAGGED

def check_game_over(board: List[List[int]], covered: List[List[int]]) -> bool:
    return check_mine_uncovered(board, covered) or check_game_win(board, covered)

def check_mine_uncovered(board: List[List[int]], covered: List[List[int]]) -> bool:
    # remove check from tile_actions.uncover_tile()
    assert len(board) == len(covered), "dimensions of board and status are not the same"

    for row in range(len(board)):
        assert len(board[row]) == len(covered[row]), "dimensions of board and status are not the same"

        for col in range(len([board[row]])):
            if covered[row][col] == UNCOVERED and board[row][col] == MINE:
                # if there exists an uncovered mine, end the game
                return True

    return False


def check_game_win(board: List[List[int]], covered: List[List[int]]) -> bool:
    for row in range(len(board)):
        for col in range(len([board[row]])):
            if covered[row][col] == COVERED:
                # if there exists a covered tile, resume game
                return False

            if covered[row][col] == FLAGGED and board[row][col] != MINE:
                # if there exists an incorrectly flagged tile, resume game
                return False

    return True
