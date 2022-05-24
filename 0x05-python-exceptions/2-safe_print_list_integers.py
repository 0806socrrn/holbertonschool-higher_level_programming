#!/usr/bin/python3
from tokenize import Number


def safe_print_list_integers(my_list=[], x=0):
    Number = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
        except (ValueError, TypeError):
            continue
        else:
            Number += 1

    print("")
    return Number
