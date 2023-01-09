#!/usr/bin/python3
def max_integer(my_list=[]):
    maxint = None
    if my_list:
        maxint = my_list[0]
        for item in my_list:
            if item > maxint:
                maxint = item
    return maxint
