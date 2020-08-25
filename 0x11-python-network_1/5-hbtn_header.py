#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import requests
import sys

res = requests.get(sys.argv[1])
print("{}".format(res.headers['X-Request-Id']))
