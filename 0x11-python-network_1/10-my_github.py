#!/usr/bin/python3
"""
This file gets info from an url
"""
import requests
import sys

if __name__ == "__main__":

    url = "https://api.github.com/user"
    user = "daorejuela1"
    one_way_token = "aba627147b5c2e4b74aa29d68be2aea818e299aa"
    response = requests.get(url, auth=(user, one_way_token))
    my_data = response.json()
    print(my_data.get('id'))
