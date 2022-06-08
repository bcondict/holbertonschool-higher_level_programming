#!/usr/bin/python3
""" inherits rectangle """

Rectangle = __import__("9-rectangle").Rectangle


class Square (Rectangle):
    """ def a square and validate it size"""
    def __init__(self, size):
        """validate if size is a """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """set a Square description"""
        return("[Square] {}/{}".format(self.__width, self.__height))
