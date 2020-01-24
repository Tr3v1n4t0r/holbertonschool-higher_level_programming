#!/usr/bin/python3
"""
Define a Rectangle class
"""

class Rectangle(Base):
    """Defines class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the private instance attribute"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def error_check(self, name, value):
        """Checks for value errors"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and (name == 'width' or name == 'height'):
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and (name == 'x' or name == 'y'):
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        self.error_check('width', value)
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        self.error_check('height', value)
        self.__height = value

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        self.error_check('x', value)
        self.__x = value

    @property
    def y(self):
        """Gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y"""
        self.error_check('y', value)
        self.__y = value
