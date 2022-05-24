#!/usr/bin/python3
from tokenize import Number


def safe_print_list(my_list=[], x=0):
    Number = 0
    for element in my_list:
        if Number >= x:
            break
        try:
            print(element, end="")
        except:
            break
        else:
            Number += 1

    print("")
    return Number
