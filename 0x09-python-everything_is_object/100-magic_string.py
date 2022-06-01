#!/usr/bin/python3
count = 0
def magic_string():
    global count 
    text_to_print = "BestSchool"
    for i in range(count):
        text_to_print += ", " + "BestSchool"
    count += 1
    return(text_to_print)