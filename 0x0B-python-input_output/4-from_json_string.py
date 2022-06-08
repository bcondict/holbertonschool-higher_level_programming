#!/usr/bin/python3
""" """


import json


def from_json_string(my_str):
    new_str = json.dumps(my_str)
    return(new_str)
