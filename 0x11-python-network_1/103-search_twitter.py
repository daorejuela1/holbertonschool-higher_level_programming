#!/usr/bin/python3
"""
This file gets info from an url
"""
import requests
import sys
import base64

if __name__ == "__main__":

    CONSUMER_KEY = sys.argv[1]
    CONSUMER_SECRET_API = sys.argv[2]
    search_string = sys.argv[3]
    auth_data = {'grant_type': 'client_credentials'}
    r = requests.post('https://api.twitter.com/oauth2/token',
                      auth=(CONSUMER_KEY,
                            CONSUMER_SECRET_API), data=auth_data)
    try:
        access_token = r.json().get('access_token')
    except:
        exit()
    parameters = {'q': search_string}
    url = "https://api.twitter.com/1.1/search/tweets.json"
    authorize = {'Authorization': 'Bearer {}'.format(access_token)}
    response = requests.get(url, headers=authorize, params=parameters)
    try:
        json = response.json()
    except:
        exit()
    if "errors" in json:
        exit()
    for i, data in enumerate(json.get('statuses')):
        if i == 5:
            break
        print("[{}] {} by {}".format(data.get('id'),
                                     data.get('text'),
                                     data.get('user').get('name')))
