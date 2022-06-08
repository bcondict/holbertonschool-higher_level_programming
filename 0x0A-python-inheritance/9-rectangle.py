#!/usr/bin/python3
"""class inherits basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """validate if width or height are int and set it private"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """set area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """set a rectangle description"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
