#!/usr/bin/python3
""" read a text file UTF8 """

def read_file(filename=""):
    """open an read a file in UTF8 """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
