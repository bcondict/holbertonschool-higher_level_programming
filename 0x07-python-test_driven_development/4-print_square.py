#!/usr/bin/python3
""" print a square with the character #"""


def print_square(size):
    """rise error if given number is not an int"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for height in range(size):
        for lenght in range(size):
            print("#", end="")
        print()
