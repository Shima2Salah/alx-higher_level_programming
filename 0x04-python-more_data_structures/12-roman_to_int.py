#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    last = 0
    for numeral in reversed(roman_string):
        value = roman_numerals[numeral]
        if value >= last:
            total += value
        else:
            total -= value
        last = value
    return total
