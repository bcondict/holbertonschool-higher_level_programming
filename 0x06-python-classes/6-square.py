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
            self._Square__size = size

        if not isinstance(value, tuple) or len(value) != 2\
                or isinstance(value[0], int) is false\
                or isinstance(value[1], int) is false\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = value

    """ define area of square """
    def area(self):
        return (self._Square__size ** 2)

    @property
    def size(self):
        """ Size - Square's size """
        return self._Square__size

    @size.setter
    def size(self, value):
        self.__init__(value, self.position)

    @property
    def position(self):
        return self.__position

    @position.setter
        self.__init__(self.size, value)

    """ My print - Prints the square using # at given position """
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for top_sapce in range(self.__position[1]):
                print()
            for height in range(self.__size):
                for middle_sapce in range(self.__position[0]):
                    print(" ", end="")
                for width in range(self.__size):
                    print("#", end="")
                print()
