#!/usr/bin/python3

"""A text indentation function"""

def text_indentation(text):

    """Prints 2 new lines after a '.', a '?', or a ':'"""

    if isinstance(text, str) is False:
        raise TypeError('text must be a string')

    nl = True
    for i in text:
        if not(nl and i == ' '):
            print(i, end='')
            nl = False
        if i in '.?:':
            print('\n')
            nl = True
