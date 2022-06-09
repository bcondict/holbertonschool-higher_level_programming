#!/usr/bin/python3
"""
function that writes an object to a text file 
using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        new_str = json.loads(my_obj)
        return f.write(new_str)
