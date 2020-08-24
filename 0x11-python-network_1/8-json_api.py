#!/usr/bin/python3
"""
This file gets info from an url
"""
import requests
import sys

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) > 1):
        value = sys.argv[1]
    else:
        value = ""
    dataset = {'q': value}
    response = requests.post(url, data=dataset)
    try:
        json = response.json()
        if not json:
            print("No result")
        else:
            value = json.loads
            print("[{}] {}".format(value['id'], value['name']))
    except ValueError:
        print("Not a valid JSON")
