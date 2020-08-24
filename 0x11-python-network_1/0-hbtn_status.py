#!/usr/bin/python3
"""
This file creates a request on the internet
"""
from urllib import request
import sys

url = "https://intranet.hbtn.io/status"
my_data_request = request.urlopen(url)
key_values = ['type', 'content', 'utf8 content']
values = []
my_data = my_data_request.read()
values.append(type(my_data))
values.append(my_data)
values.append(my_data.decode())
print("Body response:")
for i in range(3):
    print("\t- {}: {}".format(key_values[i], values[i]))
