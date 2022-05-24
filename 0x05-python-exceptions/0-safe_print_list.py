#!/usr/bin/python3
from tokenize import Number


def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            number += 1
    except Exception:
        pass
    print()
    return number