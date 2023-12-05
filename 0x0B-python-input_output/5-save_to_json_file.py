#!/usr/bin/python3
"""read element from the file"""
import json


def save_to_json_file(my_obj, filename):
    """write to json file

    Args:
        my_obj: entered object
        filename: json file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
