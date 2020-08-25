#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import requests
import requests.auth
import sys

res = requests.get('https://api.github.com/user',
                   auth=(sys.argv[1], sys.argv[2]))
try:
    if 'id' not in res.json():
        print('None')
    else:
        print("{}".format(res.json()['id']))
except ValueError as e:
    print('Not a valid JSON')
