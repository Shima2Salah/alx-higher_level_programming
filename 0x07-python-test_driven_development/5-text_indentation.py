#!/usr/bin/python3
"""
A module that indent text
"""


def text_indentation(text):
    """
    Function that indent text
    Args:
        text = string needs indentation
    Raises:
        TypeError: text must be a string
    Returns:
        printed indent text
    """
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < len(text):
        print(text[i], end="")
        if (text[i] == "." or text[i] == "?" or text[i] == ":"):
            print("\n")
            i += 1
            print(text[i].lstrip(), end="")
        i += 1
