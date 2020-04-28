#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        print(chr(ord(str[i])), end="")
        if (i == len(str) - 1):
            print("")
