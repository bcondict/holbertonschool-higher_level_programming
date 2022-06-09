#!/usr/bin/python3
""" create a class to define a student """


class Student:
    """class to define a student"""
    def __init__(self, first_name, last_name, age):
        """set name, last name and age of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method to retrieves a dictionary representation of a student"""
        self.__dict__
