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
        self.__size = size

    @property
    def size(self):
        """
        prperty method
        Returns:
        size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        property setter method for function
        Args:
        size value
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method calculate area"""
        return (self.__size * self.__size)

    def my_print(self):
        """method print area with the character #"""
        if self.__size == 0:
            print("")
        for a in range(self.__size):
            for b in range(self.__size):
                print("#", end="")
            print("")
