#!/usr/bin/python3
"""function that return an object represented by a JSON string """


import json


def from_json_string(my_str):
    """object by a json string"""
    new_str = json.loads(my_str)
    return(new_str)
