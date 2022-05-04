#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letter_str = ord(i)
        if (letter_str >= 97) and (letter_str <= 122):
            i = chr(letter_str - 32)
        print(i, end="")
    print("\n", end="")
