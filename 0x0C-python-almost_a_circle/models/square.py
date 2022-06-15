#!/usr/bin/python3
"""inherit class from rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """difines a Square with Rectangle attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor that takes size instead of with and height"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """show all the attribute of the rectangle object"""
        id_txt = "({}) ".format(self.id)
        xy_txt = "{}/{} - ".format(self.x, self.y)
        return ("[Square] " + id_txt + xy_txt + "{}".format(self.size))

    @property
    def size(self):
        """size attribute getter method"""
        return self.__size

    @size.setter
    def size(self, size):
        """
            size attribute setter method
            raise error if size is not int or less than 0
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def update(self, *args, **kwargs):
        """update object with passed arguments"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of object attributes"""
        my_dict = {
            'id': self.id, 'size': self.size,
            'x': self.x, 'y': self.y
        }
        return my_dict
