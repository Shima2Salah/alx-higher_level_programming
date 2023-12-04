#!/usr/bin/python3
"""Module returns list of objects"""


class MyList(list):
    """class print sorted list"""

    def __init__(self):
        """intianlize func"""
        super().__init__()

    def print_sorted(self):
        """sort class"""
        print(sorted(self))
