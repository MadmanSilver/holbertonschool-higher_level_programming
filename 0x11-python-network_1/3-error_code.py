#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import urllib.request
from urllib.error import HTTPError
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as res:
        print("{}".format(res.read().decode('utf-8')))
except HTTPError as err:
    print('Error code: {}'.format(err.code))
