#!/usr/bin/python3
"""
This is the "inherits from module
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited from
    the specified class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
