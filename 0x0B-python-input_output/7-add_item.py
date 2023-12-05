#!/usr/bin/python3
"""Script that stores args in json"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
sn = sys.argv[0]
args = sys.argv[1:]
existing_data = load_from_json_file(filename)
save_to_json_file(existing_data + args, filename)
