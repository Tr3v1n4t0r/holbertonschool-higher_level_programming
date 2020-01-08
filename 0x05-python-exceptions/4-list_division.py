#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    dif = 0
    for i in range(list_length):
        try:
            dif = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            dif = 0
        except ZeroDivisionError:
            print("division by 0")
            dif = 0
        except IndexError:
            print("out of range")
            dif = 0
        finally:
            new_list.append(dif)
    return new_list
