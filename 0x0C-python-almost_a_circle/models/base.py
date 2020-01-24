#!/usr/bin/python3
class Base:
    """Defines class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
