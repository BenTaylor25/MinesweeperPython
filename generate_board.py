from typing import List
from random import randint

MINE = -1

def generate_board(width: int, height: int, mine_count: int) -> List[List[int]]:
    assert width * height >= mine_count, "cannot place more mines than tiles on the board"

    board = [[0 for _ in range(width)] for _ in range(height)]

    place_mines(board, mine_count)

    return board

def place_mines(board: List[List[int]], mine_count: int):
    mines_placed = 0
    while mines_placed < mine_count:
        y = randint(0, len(board)-1)
        x = randint(0, len(board[y])-1)

        if board[y][x] != MINE:
            board[y][x] = MINE
            mines_placed += 1
