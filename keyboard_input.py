from enum import Enum
from typing import Literal

from pynput.keyboard import Key, Listener, KeyCode, Controller

class CursorAction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    FLAG = 5
    UNCOVER = 6
CursorActionType = Literal[
    CursorAction.UP, CursorAction.RIGHT,
    CursorAction.DOWN, CursorAction. LEFT,
    CursorAction.FLAG, CursorAction.UNCOVER
]

_most_recent_key = None

def watch_keyboard(key: Key):
    global _most_recent_key
    _most_recent_key = key
    return False

def get_cursor_command() -> CursorActionType:
    cmd = None
    while cmd == None:
        with Listener(on_press=watch_keyboard) as listener:
            listener.join()

        # remove key from terminal
        Controller().press(Key.backspace)

        if _most_recent_key == KeyCode.from_char('j'):
            cmd = CursorAction.DOWN

    return cmd

