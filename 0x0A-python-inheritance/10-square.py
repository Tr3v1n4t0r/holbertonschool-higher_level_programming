#!/usr/bin/python3
"""
This is the BaseGeometry and Rectangle modules
"""
Rectangle = __import__('9-rectangle').Rectangle


"""
This is the Square module
"""


class Square(Rectangle):
    """Represents a Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
