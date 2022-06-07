#!/usr/bin/python3
"""class inherits a list"""


class MyList(list):
    """ sort a given list"""
    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
