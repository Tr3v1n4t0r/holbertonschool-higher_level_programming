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
