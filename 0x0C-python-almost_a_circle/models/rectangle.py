#!/usr/bin/python3
""" inherit class from base"""

from models.base import Base


class Rectangle(Base):
    """difine a rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            constructor that takes width, height, x value and y value
            id gives one if None is pass
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(self.id)

    @property
    def width(self):
        """width attribute getter method"""
        return self.__width

    @width.setter
    def width(self, width):
        """
            width attribute setter method
            raise error if height is not int or less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height attribute getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """
            height attribute setter method
            raise error if height is not int or less than 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x attribute getter method"""
        return self.__x

    @x.setter
    def x(self, x):
        """
            x attribute setter method
            raise error if x is not int or less than 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y attribute getter method"""
        return self.__y

    @y.setter
    def y(self, y):
        """
            y attribute setter method
            raise error if y is not int or less than 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return area of rectangle object"""
        return (self.__height * self.__width)

    def display(self):
        """print rectangle object with attributes already set"""
        my_rectangle = '\n' * self.y
        my_rectangle += ((" "*self.__x) + "#"*self.__width+'\n')*self.__height
        my_rectangle = my_rectangle[:-1]
        print(my_rectangle)

    def __str__(self):
        """show all the attribute of the rectangle object"""
        id_txt = "({}) ".format(self.id)
        xy_txt = "{}/{} - ".format(self.__x, self.__y)
        wh_txt = "{}/{}".format(self.__width, self.__height)
        return("[Rectangle] " + id_txt + xy_txt + wh_txt)

    def update(self, *args, **kwargs):
        """update object with passed arguments"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of object attributes"""
        my_dict = {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
        }
        return my_dict
