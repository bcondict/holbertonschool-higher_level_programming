#!/usr/bin/python3
""" create a class to define a student """


class Student:
    """class to define a student"""
    def __init__(self, first_name, last_name, age):
        """set name, last name and age of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method to retrieves a dictionary representation of a student"""
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if attr in self.__dict__.keys():
                new_dict[attr] = self.__dict__[attr]

        return new_dict
