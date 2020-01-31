#!/usr/bin/python3
"""
This is the "pascal triangle" module
"""


def pascal_triangle(n):
    """Return a list of integers representing Pascal's triangle of n"""
    new_list = []
    if n <= 0:
        return new_list
    for i in range(1, n + 1):
        value = 1
        temp_list = []
        for j in range(1, i + 1):
            temp_list.append(str(value))
            value = value * (i - j) // j
        new_list.append(temp_list)
    return new_list
