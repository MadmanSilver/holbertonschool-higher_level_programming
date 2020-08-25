#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import requests
import sys

res = requests.get(sys.argv[1])
if res.status_code > 400:
    print('Error code: {}'.format(res.status_code))
else:
    print("{}".format(res.text))
