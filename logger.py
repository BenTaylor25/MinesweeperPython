from os import path

FILENAME = "debug.log"

def clear_log():
    with open(FILENAME, 'w') as f:
        f.write("")

def log_message(message: str):
    with open(FILENAME, 'a') as f:
        f.write(message + "\n")

def log_nl(message: str = ""):
    log_message(message + "\n")
