#!/usr/bin/python3
"""
This file creates a request on the internet
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    key = ['type', 'content']
    response = requests.get(url)
    print("Body response:")
    value = [type(response.text), response.text]
    for i in range(2):
        print("\t- {}: {}".format(key[i], value[i]))
