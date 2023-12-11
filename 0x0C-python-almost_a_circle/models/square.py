#!/usr/bin/python3
""" module Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ intialize function """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string function """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ size setter function """
        return self.width

    @size.setter
    def size(self, value):
        """ size getter function """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ square update function """
        if args != ():
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        for key, value in kwargs.items():
            if key == "size":
                self.size = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
            if key == "id":
                self.id = value

    def to_dictionary(self):
        """ square convert to dictionary function """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
