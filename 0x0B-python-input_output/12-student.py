#!/usr/bin/python3
"""
This is the Student module
"""


class Student:
    """Represents a Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve specified attributes of a Student"""
        if attrs is None:
            return self.__dict__
        new_attrs = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_attrs[key] = value
        return new_attrs
