#!/usr/bin/python3
""" read a text file UTF8 """


def append_write(filename="", text=""):
    """append text to a file utf8"""
    with open(filename, 'a+', encoding="utf-8") as f:
        return f.write(text)
