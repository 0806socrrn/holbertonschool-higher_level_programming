#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    uni = list(set(my_list))
    for x in uni:
        i += x
    return (i)
