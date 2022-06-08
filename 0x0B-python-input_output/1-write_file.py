#!/usr/bin/python3
""" read a text file UTF8 """


def write_file(filename="", text=""):
    """open an write a file in UTF8 """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
