#!/usr/bin/python3
""" base clase to create child class"""

import json


class Base:
    """ all methods to inherit to child class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
            assign an id to a object
            if there's not id assign nb_object to it
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            take a list of dictionaries and
            return a JSON string representation
            return [] if is None or empty list
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the JSON string representation of list_objs
            to a file
        """
        filename = "{}.json".format(cls.__name__)
        my_list = []

        if list_objs or list_objs is not None:
            for new_obj in list_objs:
                my_list.append(cls.to_dictionary(new_obj))

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """
            return the list of JSON string representation
            return empty list if JSON S.R is empty or None
        """
        my_list = []
        my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """
            return an instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            return empty list if file doesn't exist
            return a list of instance
        """
        instance_list = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                new_list = cls.from_json_string(f.read())
            for list_obj in new_list:
                instance_list.append(cls.create(**list_obj))
        except FileNotFoundError:
            pass

        return instance_list
