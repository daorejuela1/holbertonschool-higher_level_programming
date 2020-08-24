#!/usr/bin/python3
"""
This file gets info from an url
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if (response.status_code >= 400):
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
