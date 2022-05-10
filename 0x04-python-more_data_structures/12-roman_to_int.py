#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman_string)):
            for j in letter:
                if j == roman_string[i]:
                    if i > 0 and letter[j] > letter[roman_string[i - 1]]:
                        result += letter[j] - 2
                    else: 
                        result += letter[j]
    return result
