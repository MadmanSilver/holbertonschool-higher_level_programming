#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as res:
    print("{}".format(res.info()['X-Request-Id']))
