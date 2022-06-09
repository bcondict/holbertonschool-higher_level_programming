#!/usr/bin/python3
"""script that add all arguments to a python list and save it in a file"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    new_list = load_from_json_file(filename)
except Exception:
    new_list = []
save_to_json_file(new_list + argv[1:], filename)
