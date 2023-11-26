#!/usr/bin/python3
"""
A module that print square
"""


def print_square(size):
    """
    Function that print squre
    Args:
        size = integer number
    Raises:
        TypeError: size not integer
        ValueError: size less than 0
    Returns:
        printed square
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        for b in range(size):
            print("#", end="")
        print("")
