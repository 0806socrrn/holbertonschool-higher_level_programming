#!/usr/bin/python3

from xml.dom.minidom import Element


def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for elme in my_list:
            if elme > max:
                max = elme
        return max
    return None
