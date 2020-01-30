#!/usr/bin/python3
"""
This is a lookup module that supplies one function, lookup()
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
