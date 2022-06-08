#!/usr/bin/python3
"""class inherits basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """validate if width or height are int and set it private"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("heigh", height)
        self.__width = width
        self.__height = height
