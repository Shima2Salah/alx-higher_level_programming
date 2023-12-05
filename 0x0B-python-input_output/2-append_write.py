#!/usr/bin/python3
"""read element from the file"""


def append_write(filename="", text=""):
    """write element to the file

    Args:
        filename: the file name
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return len(text)
