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
    random = b"This is not random"
    encoded_number = base64.b64encode(random)
    auth_data = {'grant_type': 'client_credentials'}
    key = "{}:{}".format(CONSUMER_KEY, CONSUMER_SECRET_API).encode('ascii')
    key = base64.b64encode(key).decode('ascii')
    header_data = {'Authorization': 'Basic {}'.format(key),
                   'Content-Type':
                   'application/x-www-form-urlencoded;charset=UTF-8'}
    r = requests.post('https://api.twitter.com/oauth2/token',
                      data=auth_data,
                      headers=header_data)
    try:
        access_token = r.json().get('access_token')
    except ValueError:
        exit()
    parameters = {'q': search_string, 'count': 5}
    url = "https://api.twitter.com/1.1/search/tweets.json"
    authorize = {'Authorization': 'Bearer {}'.format(access_token)}
    response = requests.get(url, headers=authorize, params=parameters)
    try:
        json = response.json()
    except ValueError:
        exit()
    if "errors" in json:
        exit()
    for data in json.get('statuses'):
        print("[{}] {} by {}".format(data.get('id'),
                                     data.get('text'),
                                     data.get('user').get('name')))
