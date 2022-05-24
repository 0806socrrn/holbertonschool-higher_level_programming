#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    count = 0
    for count in range(0, x):
        try:
            print("{}".format(my_list[count]), end="")
            number += 1
        except IndexError:
            pass
    print("")
    return number
