#!/usr/bin/python3
import string
for alphabet in string.ascii_lowercase:
    if (alphabet == 'q') or (alphabet == 'e'):
        continue
    else:
        print(alphabet, end="")
