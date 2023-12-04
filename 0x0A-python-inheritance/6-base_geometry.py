#!/usr/bin/python3
"""module that return is object or not"""


class BaseGeometry:
    """class BaseGeometry parent"""

    def __init__(self):
        """intialize function"""
        pass

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")
