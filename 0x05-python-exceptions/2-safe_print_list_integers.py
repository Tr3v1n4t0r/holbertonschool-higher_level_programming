#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        a, b = 0, 0
        while a < x:
            try:
                print("{:d}".format(my_list[a]), end='')
                a += 1
                b += 1
            except:
                a += 1
        if a == b:
            print()
    except:
        print()
    if a > b:
        return IndexError
    return b
