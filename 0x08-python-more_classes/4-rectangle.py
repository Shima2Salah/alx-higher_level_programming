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
        self.width = width
        self.height = height

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

    def area(self):
        """function return rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """function return rectangle perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """print # as rectangle area"""
        i = 0
        a = ""
        if (self.__width == 0 or self.__height == 0):
            return ""
        while i < self.__height:
            j = 0
            while j < self.__width:
                a += "#"
                j += 1
            i += 1
            if i != self.__height:
                a += "\n"
        return a

    def __repr__(self):
        """print developer data"""
        x = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return x
