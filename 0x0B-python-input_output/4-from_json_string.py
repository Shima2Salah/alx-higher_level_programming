#!/usr/bin/python3
"""read element from the file"""
import json


def from_json_string(my_str):
    """write to json file

    Args:
        my_obj: entered object
    """
    js_str = json.loads(my_str)
    return (js_str)
