#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (len(sentence), None)
    needed_tuple = len(sentence), sentence[0]
    return needed_tuple
