#!/usr/bin/python3
""" module base """
from base import Base


class Rectangle(Base):
    """ class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ intialize function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        """ width getter function """
        return self.__width
    @width.setter
    def width(self, value):
        """ width setter function """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter function """
        return self.__height
    @height.setter
    def height(self, value):
        """ height getter function """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x setter function """
        return self.__x
    @x.setter
    def x(self, value):
        """ x getter function """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y setter function """
        return self.__y
    @y.setter
    def y(self, value):
        """ y getter function """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area calculate function """
        return (self.__width * self.__height)

    def display(self):
        """ rectangle display function """
        a, c = 0, 0
        while (c < self.__y):
            print("")
            c += 1
        while (a < self.__height):
            b, d = 0, 0
            while (d < self.__x):
                print(" ", end="")
                d += 1
            while (b < self.__width):
                print("#", end="")
                b += 1
            a += 1 
            print("")
    
    def __str__(self):
        """ string function """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ rectangle update function """
        if args != ():
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except Exception:
                pass
        for key, value in kwargs.items():
            if key == "width":
                self.__width = value
            if key == "height":
                self.__height = value
            if key == "x":
                self.__x = value
            if key == "y":
                self.__y = value
            if key == "id":
                self.id = value

    def to_dictionary(self):
        """ convert to dictionary function """
        return {"x":self.__x, "y":self.__y, "id":self.id, "height":self.__height, "width":self.__width}
