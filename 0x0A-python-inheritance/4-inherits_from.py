#!/usr/bin/python3
"""module that return is object or not"""


def inherits_from(obj, a_class):
    """is same class func"""
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    return False
