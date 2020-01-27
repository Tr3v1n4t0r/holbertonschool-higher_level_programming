#!/usr/bin/python3
"""
Define a Rectangle class
"""
from models.base import Base


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

    def area(self):
        """Returns the area value of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance to the stdout"""
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
              self.__height, end='')

    def __str__(self):
        """Prints the Rectangle attributes"""
        return ('[Rectangle] (' + str(self.id) + ') ' + str(self.__x) + '/' +
                str(self.__y) + ' - ' + str(self.__width) + '/' +
                str(self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}

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
