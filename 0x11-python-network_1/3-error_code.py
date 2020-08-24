#!/usr/bin/python3
"""
This file creates a request on the internet
"""
from urllib import request
from urllib import parse
from urllib import error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            my_data = response.read()
            print(my_data.decode())
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
