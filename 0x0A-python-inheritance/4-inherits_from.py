#!/usr/bin/python3
"""checks if the object is an intance of a clas that inhereted"""


def inherits_from(obj, a_class):
    """ return true if obj is a class or false if is not """
    if type(obj) is a_class:
        return False
    return (isinstance(obj, a_class))
