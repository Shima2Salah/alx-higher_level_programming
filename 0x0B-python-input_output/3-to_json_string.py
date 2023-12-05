#!/usr/bin/python3
"""read element from the file"""
import json


def to_json_string(my_obj):
    """write to json file

    Args:
        my_obj: entered object
    """
    js_str = json.dumps(my_obj)
    return (js_str)
