#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import requests
import sys

res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
print("{}".format(res.text))
