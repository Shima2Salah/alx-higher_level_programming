#!/usr/bin/python3
"""module that return is object or not"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class square child"""

    def __init__(self, size):
        """int func validator function"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
