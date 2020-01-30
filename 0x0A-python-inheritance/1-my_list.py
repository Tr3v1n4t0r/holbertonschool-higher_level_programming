#!/usr/bin/python3
"""
This is the "my list" module that supplies one function, print_sorted()
"""


class MyList(list):
    """Represents a MyList class"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
