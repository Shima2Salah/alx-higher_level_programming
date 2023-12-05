#!/usr/bin/python3
"""read element from the file"""


def write_file(filename="", text=""):
    """write element to the file

    Args:
        filename: the file name
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
        return len(text)
