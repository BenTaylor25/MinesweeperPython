
def capitalise_words(words: str) -> str:
    """
    Capitalise the first letter of each word.
    E.g. "hello world" -> "Hello World"
    """
    return " ".join([word.capitalize() for word in words.split(" ")])
