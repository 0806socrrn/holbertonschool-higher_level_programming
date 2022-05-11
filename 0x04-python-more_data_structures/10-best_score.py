#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    res = ""
    if a_dictionary:
        for c, v in a_dictionary.items():
            if v > i:
                res = c
                i = v
        return res
    else:
        return None
