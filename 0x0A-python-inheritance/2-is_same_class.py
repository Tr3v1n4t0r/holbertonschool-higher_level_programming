#!/usr/bin/python3
"""
This is the "is same class" module that supplies one function, is_same_class()
"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class"""
    return isinstance(obj, a_class)
