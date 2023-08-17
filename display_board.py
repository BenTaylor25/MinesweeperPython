from typing import List

from dependency_importer import dep_import

dep_import("colorama")
from colorama import Fore, Style

def display_board(board: List[List[int]], covered: List[List[bool]]):
    assert len(board) == len(covered), "board values and covered values are not compatible"
    for r in range(len(board)):
        assert len(board[r]) == len(covered[r]), "board values and covered values are not compatible"
        for c in range(len(board[r])):
            if covered[r][c]:
                print(Fore.WHITE + "?", end = " ")
            else:
                char = value_to_display_char(board[r][c])
                print(char, end=" ")
        print()
    print(Style.RESET_ALL)

COLOURS = [
    Fore.GREEN,
    Fore.LIGHTCYAN_EX, Fore.CYAN,
    Fore.LIGHTBLUE_EX, Fore.BLUE,
    Fore.LIGHTMAGENTA_EX, Fore.MAGENTA,
    Fore.LIGHTYELLOW_EX, Fore.YELLOW
]
def value_to_display_char(value: int) -> str:
    if value == -1:
        return Fore.RED + 'M'
    
    return COLOURS[value] + str(value)
