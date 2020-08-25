#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import requests

body = requests.get('https://intranet.hbtn.io/status').text
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
