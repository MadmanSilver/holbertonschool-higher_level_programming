#!/usr/bin/python3
""" Fetches from intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("{}".format(res.text))
