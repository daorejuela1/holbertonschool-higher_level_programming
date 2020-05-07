#!/usr/bin/python3
def roman_to_int(roman_string):

    acumulator = 0
    if not roman_string or type(roman_string) is not str:
        return acumulator
    roman_dictionary = {
    'M':1000,
    'D':500,
    'C':100,
    'L':50,
    'X':10,
    'V':5,
    'I':1
    }
    for index in range (0, len(roman_string)):
        try:
            if (roman_dictionary[roman_string[index]] >= roman_dictionary[roman_string[index + 1]]):
                acumulator = roman_dictionary[roman_string[index]] + acumulator
            else:
                acumulator = - roman_dictionary[roman_string[index]] + acumulator
        except IndexError:
            acumulator = roman_dictionary[roman_string[index]] + acumulator
    return(acumulator)