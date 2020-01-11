#!/usr/bin/python3

"""Add integer module"""

def add_integer(a, b=98):

    """Returns the sum of integers a and b"""

    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not(isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
