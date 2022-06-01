#!/usr/bin/python3
""" create a class that defines a rectangle"""


class Rectangle:
    """ Representation of a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """defines rectangle with tidth and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("widh must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """calculate rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (2*(self.height+self.width))

    def __str__(self):
        """print # to representate rectangle """
        new_str = ""
        charac = self.print_symbol
        if self.height != 0 and self.width != 0:
            new_str = ("{}".format(charac) * self.width + "\n") * self.height
            new_str = new_str[:-1]
        return new_str

    def __repr__(self) -> str:
        """representation of width and height"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """print a message"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
