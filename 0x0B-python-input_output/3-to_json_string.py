#!/usr/bin/python3
""" function that return the json representation"""


import json


def to_json_string(my_obj):
    """json representation of my_obj"""
    return json.dumps(my_obj)
