#!/usr/bin/python3
""" return the dictionary descrption with a simple data structure """


def class_to_json(obj):
    """return a dictionary setted by __dict__"""
    return obj.__dict__
