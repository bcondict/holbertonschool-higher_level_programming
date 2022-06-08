#!/usr/bin/python3
"""class inherits a list"""


class MyList(list):
    """ sort a given list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
