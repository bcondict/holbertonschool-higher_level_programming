#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for a in my_string:
        if a != "c" and a != "C":
            new_string += a
    return (new_string)
