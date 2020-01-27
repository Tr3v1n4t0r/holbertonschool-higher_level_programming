#!/usr/bin/python3
"""
Define a Square class
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints Square attributes"""
        return ('[Square] (' + str(self.id) + ')' + str(self._Rectangle__x) +
                '/' + str(self._Rectangle__y) + ' - ' +
                str(self._Rectangle__width))

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self._Rectangle__x = args[2]
            if len(args) >= 4:
                self._Rectangle__y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.__size, 'x': self._Rectangle__x,
                'y': self._Rectangle__y}

    @property
    def size(self):
        """Gets the size"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Sets the size"""
        self.error_check('width', value)
        self.error_check('height', value)
        self._Rectangle__width = value
        self._Rectangle__height = value
