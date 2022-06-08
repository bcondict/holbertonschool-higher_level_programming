#!/usr/bin/python3
""" see if an object is an specific type"""


def is_same_class(obj, a_class):
    """ return true if obj is a class or false if is not """
    if type(obj) is a_class:
        return True
    return False