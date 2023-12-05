#!/usr/bin/python3
"""file module"""


def read_file(filename=""):
    """read file function"""
    with open(filename, 'r', encoding='utf-8')as file:
        f = file.read()
    print(f)
