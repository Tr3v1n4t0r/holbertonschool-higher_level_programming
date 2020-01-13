#!/usr/bin/python3

"""Print Square function"""

def print_square(size):

    """Prints a square of size size"""

    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print(('#' * size + '\n') * size, end='')
