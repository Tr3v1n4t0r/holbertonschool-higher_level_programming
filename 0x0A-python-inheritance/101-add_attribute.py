#!/usr/bin/python3
"""
This is the add attribut module
"""


def add_attribute(self, attribute, value):
    """Adds attribute if possible"""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
