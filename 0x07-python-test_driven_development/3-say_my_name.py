#!/usr/bin/python3
"""
A module that print name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that print full name
    Args:
        first_name = first name string
        last_name = second name string
    Raises:
        TypeError: first_name or last_name not string
    Returns:
        full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
