#!/usr/bin/python3
"""Script that stores args in json"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
args = sys.argv[1:]

existing_list = load_from_json_file(filename)

existing_list.extend(args)

save_to_json_file(existing_list, filename)
