#!/usr/bin/python3
""" module base """
import json


class Base:
    """parent class for id """
    __nb_objects = 0

    def __init__(self, id=None):
        """intializing method"""
        if id is not None:
            self.id = id
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
                return
            for obj in list_objs:
                z.append(obj.to_dictionary())
            file.write(Base.to_json_string(z))

    @staticmethod
    def from_json_string(json_string):
        """get from json file method"""
        if json_string is None or json_string is []:
            return []
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

    @classmethod
    def load_from_file_csv(cls):
        """
        Function that loads from a .csv file
        """
        ans = []
        with open(cls.__name__ + ".csv", "r") as f:
            reader = csv.DictReader(f)
            for line in reader:
                kwargs = dict(line)
                for key, val in kwargs.items():
                    kwargs[key] = int(val)
                ans.append(cls.create(**kwargs))
            return ans

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Function that draws squares and rectangles.
        """
        my_t = turtle.Turtle()
        for rect in list_rectangles:
            my_t.setheading(0)
            my_t.penup()
            my_t.goto(rect.x, rect.y)
            my_t.pendown()
            my_t.forward(rect.width)
            my_t.right(90)
            my_t.forward(rect.height)
            my_t.right(90)
            my_t.forward(rect.width)
            my_t.right(90)
            my_t.forward(rect.height)
        for squ in list_squares:
            my_t.setheading(0)
            my_t.penup()
            my_t.goto(squ.x, squ.y)
            my_t.pendown()
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
        input()
