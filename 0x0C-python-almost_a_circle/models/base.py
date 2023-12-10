#!/usr/bin/python3
""" module base """
import json


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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to string method"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file method"""
        z = []
        with open(cls.__name__ + '.json', 'w')as file:
            if list_objs is None:
                file.write("[]")
            for obj in list_objs:
                z.append(obj.to_dictionary())
            file.write(Base.to_json_string(z))

    @staticmethod
    def from_json_string(json_string):
        """get from json file method"""
        if json_string is None or json_string is []:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create new instance method"""
        if cls.__name__ == "Rectangle":
            new_inst = cls(1, 1)
        elif cls.__name__ == "Square":
            new_inst = cls(1)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """load from file method"""
        inst = []
        try:
            with open(cls.__name__ + '.json', 'r')as file:
                content = Base.from_json_string(file.read())
                for con in content:
                    inst.append(cls.create(**con))
                return inst
        except Exception:
            return []
