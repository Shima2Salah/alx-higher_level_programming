#!/usr/bin/python3
"""module that return is object or not"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle child"""

    def __init__(self, width, height):
        """int func validator function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """print string"""
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """area function"""
        return (self.__width * self.__height)
