#!/usr/bin/python3
""" module base """


class Base:
    """parent class for id """
    __nb_objects = 0

    def __init__(self, id=None):
        """intializing method"""
        if id is not None:
            self.id  = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
