#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    number = 0
    for number in range(list_length):
        try:
            result = my_list_1[number]/my_list_2[number]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            number += 0
            list.append(result)
    return(list)
