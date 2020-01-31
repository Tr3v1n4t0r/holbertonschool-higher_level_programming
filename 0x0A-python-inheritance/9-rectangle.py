#!/usr/bin/python3
"""
This is the BaseGeometry module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
This is the Rectangle module
"""


class Rectangle(BaseGeometry):
    """Represents a Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __repr__(self):
        """Prints the width and height of the rectangle"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
