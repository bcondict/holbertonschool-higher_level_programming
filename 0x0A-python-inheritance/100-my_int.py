#!/usr/bin/python3
""" inherit int"""


class MyInt(int):
    """invert bitways operator"""
    def __eq__(self, other):
        """ invert == operator"""
        return super().__eq__(other)

    def __ne__(self, other):
        """invert != operator"""
        return super().__ne__(other)
