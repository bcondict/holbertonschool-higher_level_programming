#!/usr/bin/python3
""" class with an exception """


class BaseGeometry:
    """raise an exception"""
    def area(self):
        """area exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator of value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
