#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import requests
import requests.auth
import sys

if __name__ == "__main__":
    res = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    try:
        print("{}".format(res.json().get('id')))
    except ValueError as e:
        print('Not a valid JSON')
