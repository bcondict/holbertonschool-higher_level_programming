#!/usr/bin/python3
""" create a class that defines a rectangle"""


class Rectangle:

    """defines rectangle with tidth and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("widh must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """height getter"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
