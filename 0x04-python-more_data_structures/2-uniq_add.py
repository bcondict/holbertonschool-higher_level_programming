#!/usr/bin/python3
def uniq_add(my_list=[]):
    value = 0
    for i in set(my_list):
        value += i
    return value
