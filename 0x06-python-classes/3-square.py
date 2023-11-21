#!/usr/bin/python3
"""A module that declare a class"""


class Square:
    """It is an empty class called square"""
    def __init__(self, size=0):
        """
        intialize method for function
        Args:
        size value
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method calculate area"""
        return (self.__size * self.__size)
