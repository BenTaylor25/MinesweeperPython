from typing import List

from dependency_importer import dep_import

dep_import("colorama")
from colorama import Fore, Style

def display_board(board: List[List[int]]):
    for row in board:
        for char in list(map(value_to_display_char, row)):
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
