#!/usr/bin/python3
"""
This file creates a request on the internet
"""
from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    address = sys.argv[2]
    data = parse.urlencode({'email': address})
    with request.urlopen(url, data) as response:
        my_data = response.read()
        print(my_data.decode())
