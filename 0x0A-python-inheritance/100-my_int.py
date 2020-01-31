#!/usr/bin/python3
"""
This is the MyInt module
"""


class MyInt(int):
    """Represents a MyInt"""
    def __eq__(self, other):
        """Checks id two MyInts are epual"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Checks if two MyInts are not equal"""
        return int(self) == int(other)
