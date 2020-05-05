#!/usr/bin/python3
def multiple_returns(sentence):
    """returns the lenght of a string and first character"""
    if sentence:
        string_length = len(sentence)
        first_character = sentence[0]
    else:
        string_length = 0
        first_character = None
    return (string_length, first_character)
