#!/usr/bin/python3
"""file module"""


def read_file(filename=""):
    """read file function"""
    with open(filename, 'r')as file:
        f = file.read()
    print(f)
