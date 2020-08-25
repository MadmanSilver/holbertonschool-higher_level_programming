#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import urllib.request
import urllib.parse
import sys

data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
with urllib.request.urlopen(urllib.request.Request(sys.argv[1], data)) as res:
    print("{}".format(res.read().decode('utf-8')))
