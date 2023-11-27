#!/usr/bin/python3
"""A module of rectangle"""


class Rectangle:
    """class that returns rectangle specs"""

    def __init__(self, width=0, height=0):
        """intialize function for Rectangle
        Args:
        width: defailt value zero
        height: default value zero
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property width function
        Return:
        private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter width function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property height function
        Return:
        private height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """property setter height function"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
