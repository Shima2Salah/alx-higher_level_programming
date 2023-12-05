#!/usr/bin/python3
"""read element from the file"""
import json


def load_from_json_file(filename):
    """write to json file

    Args:
        my_obj: entered object
        filename: json file
    """
    with open(filename, 'r') as f:
        return (json.load(f))
