#!/usr/bin/python3
""" class square to difine a square """


class Square:

    """ define a squeare with 'size' size  and type and value error"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ define area of square """
    def area(self):
        return (self.size ** 2)

    @property
    def size(self):
        return(self.size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value

    @property
    def position(self):
        return(self.position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2\
                or isinstance(value[0], int) is false\
                or isinstance(value[1], int) is false\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.position = value

    def my_print(self):
        if self.size == 0:
            print("")
            return
        for top_sapce in range(self.position[1]):
            print("")
        for height in range(self.size):
            for middle_sapce in range(self.position[0]):
                print(" ", end="")
            for width in range(self.size):
                print("#", end="")
            print("")
