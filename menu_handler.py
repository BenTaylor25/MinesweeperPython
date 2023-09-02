from typing import Dict, Callable

def menu_handler(options: Dict[str, Callable[[], None]]) -> str:
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = ""
    option_numbers = [str(i+1) for i in range(len(options))]   # ["1", "2", ...]
    while choice not in option_numbers:
        choice = input("-> ")

    # call function of selected option
    options[list(options)[int(choice)-1]]()

    return list(options)[int(choice)-1]
