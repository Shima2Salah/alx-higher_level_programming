#!/usr/bin/python3
"""module that return is object or not"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle child"""

    def __init__(self, width, height):
        """int func validator function"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
