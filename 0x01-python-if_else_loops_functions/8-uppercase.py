#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (ord(str[i]) < 97 or ord(str[i]) > 122):
            change = 0
        else:
            change = 32
        print(chr(ord(str[i]) - change), end="")
        if (i == len(str) - 1):
            print("")
