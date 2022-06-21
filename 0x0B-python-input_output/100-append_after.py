#!/usr/bin
""" """


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "a+", encoding="utf-8") as f:
        complete_str = f.readlines()
        for my_string in complete_str:
            f.write(my_string)
            if my_string == search_string:
                f.write(new_string)
        return f

