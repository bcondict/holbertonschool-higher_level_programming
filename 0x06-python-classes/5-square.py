#!/usr/bin/python3
""" class square to difine a square """


class Square:

    """ define a squeare with 'size' size  and type and value error"""
    def __init__(self, size=0):
        self.size = size

    """ define area of square """
    def area(self):
        return(self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("\n")
        for i in range(self.__size):
            print("#" * self.__size)
