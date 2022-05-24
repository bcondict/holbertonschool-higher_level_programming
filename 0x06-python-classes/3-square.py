#!/usr/bin/python3
""" class square to difine a square """


class Square:

    """ define a squeare with 'size' size  and type and value error"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ define area of square """
    def area(self):
        return (self.__size ** 2)
