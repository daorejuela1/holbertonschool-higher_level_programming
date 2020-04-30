#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    acum = 0
    for i in range(1, len(sys.argv)):
        acum = int(sys.argv[i]) + acum
    print("{:d}".format(acum))
