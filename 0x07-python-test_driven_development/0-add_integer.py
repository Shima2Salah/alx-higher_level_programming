#!/usr/bin/python3
"""
A module that add integers
This module contains only one function to add two integers.
like add_integer(5, 2) should give the result 7
"""


def add_integer(a, b=98):
    """
    Function that add two integers
    Args:
        a = first integer number
        b = second integer number
    Raises:
        TypeError: if a or b not integer
    Returns:
        sum of a and b
    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
