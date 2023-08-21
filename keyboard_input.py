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
        if cmd != None:
            Controller().press(Key.backspace)

        if _most_recent_key in (
            KeyCode.from_char('j'),
            Key.down,
        ):
            cmd = CursorAction.DOWN

        elif _most_recent_key in (
            KeyCode.from_char('k'),
            Key.up,
        ):
            cmd = CursorAction.UP

        elif _most_recent_key in (
            KeyCode.from_char('h'),
            Key.left,
        ):
            cmd = CursorAction.LEFT

        elif _most_recent_key in (
            KeyCode.from_char('l'),
            Key.right,
        ):
            cmd = CursorAction.RIGHT

        elif _most_recent_key in (
            KeyCode.from_char('f'),
            KeyCode.from_char('m'),
        ):
            cmd = CursorAction.FLAG

        elif _most_recent_key in (
            KeyCode.from_char('u'),
            KeyCode.from_char('s'),
        ):
            cmd = CursorAction.UNCOVER

    return cmd

