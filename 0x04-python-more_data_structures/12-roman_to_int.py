#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    res = 0
    key = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    r_length = len(roman_string)
    for i in range(r_length):
        if i < r_length - 1 and key[roman_string[i]]< \
           key[roman_string[i + 1]]:
            res -= key[roman_string[i]]
        else:
            res += key[roman_string[i]]
    return res
