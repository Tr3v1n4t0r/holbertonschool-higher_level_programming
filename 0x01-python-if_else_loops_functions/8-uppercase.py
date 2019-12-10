#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        case = 0
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            case = 32
        print('{:c}'.format(ord(letter) - case), end="")
    print()
