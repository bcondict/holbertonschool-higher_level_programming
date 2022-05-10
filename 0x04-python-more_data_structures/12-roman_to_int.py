#!/usr/bin/python3
def roman_to_int(roman_string):
    letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) is str:
        num = 0
        for i in range(len(roman_string)):
            if i > 0 and letter[roman_string[i]] > letter[roman_string[i-1]]:
                num += letter[roman_string[i]] - letter[roman_string[i-1]] * 2
            else:
                num += letter[roman_string[i]]
        return num
    return 0
