#!/usr/bin/python3
"""
This file gets info from an url
"""
import requests
import sys

if __name__ == "__main__":

    repository = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repository)
    response = requests.get(url)
    try:
        my_data = response.json()
    except ValueError:
        print("Not a valid JSON")
        exit()
    try:
        if not my_data or my_data.get('message') == "Not Found":
            print("No result")
            exit()
    except AttributeError:
        pass
    for i in range(10):
        print("{}: {}".format(my_data[i].get('sha'),
                              my_data[i].get('commit').
                              get('author').get('name')))
