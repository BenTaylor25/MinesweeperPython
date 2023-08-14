from typing import Dict, Callable

WIDTH = 15
HEIGHT = 15
MINES = 30

def menu_handler(options: Dict[str, Callable[[], None]]):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = ""
    while choice not in [str(i+1) for i in range(len(options))]:
        choice = input("->")
    
    options[list(options)[int(choice)-1]]()

def main_menu():
    menu_handler({
        "test 1": foo,
        "test 2": bar,
    })

def foo():
    print("foo")

def bar():
    print("bar")

if __name__ == "__main__":
    main_menu()
