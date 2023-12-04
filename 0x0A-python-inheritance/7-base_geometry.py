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

    def integer_validator(self, name, value):
        """int func validator function"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
