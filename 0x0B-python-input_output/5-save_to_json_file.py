#!/usr/bin/python3
"""read element from the file"""
import json


def save_to_json_file(my_obj, filename):
    """write to json file

    Args:
        my_obj: entered object
        filename: json file
    """
    js_str = json.dumps(my_obj)
    with open(filename, 'w')as f:
        f.write(js_str)
