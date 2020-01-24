#!/usr/bin/python3
"""
Define a class Base
"""
import json
import csv

class Base:
    """Defines class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        dictionary = []

        if list_objs is not None:
            dictionary = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(dictionary))
