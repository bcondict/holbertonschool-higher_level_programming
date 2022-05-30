#!/usr/bin/python3
""" print a text with 2 new lines after ., ? or : character"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for n_t in range(len(text)):
        less = text[n_t - 1]
        if text[n_t] == '.' or text[n_t] == '?' or text[n_t] == ':' and n_t > 0:
            if text[n_t] == " ":
                continue
            print(text[n_t])
            print()
        elif ((text[n_t] == ' ') and (less == '.' or less == ':' or less == '?') and (n_t > 0)):
            continue
        else:
            print(text[n_t], end="")
