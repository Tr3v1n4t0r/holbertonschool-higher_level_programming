#!/usr/bin/python3
class Rectangle:
    """Represents a Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if width == 0 or height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the rectangle"""
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        string += (str(self.print_symbol) * self.__width + '\n') * self.__height
        return string[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return ('Rectangle(' + str(self.__width) + ', ' +
                str(self.__height) + ')')

    def __del__(self):
        """Deletes a rectangle"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
