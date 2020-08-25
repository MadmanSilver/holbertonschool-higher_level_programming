#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import requests
import sys

if len(sys.argv) < 2:
    sys.argv.append("")
res = requests.post('http://0.0.0.0:5000/search_user', data={'q': sys.argv[1]})
try:
    if res.json() == {}:
        print('No result')
    else:
        print("[{}] {}".format(res.json()['id'], res.json()['name']))
except ValueError as e:
    print('Not a valid JSON')
