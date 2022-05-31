#!/usr/bin/python3
""" create a empty class that defines a rectangle"""


from turtle import width
from typing import Type


class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("widh must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
