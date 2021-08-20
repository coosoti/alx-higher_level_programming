#!/usr/bin/python3
"""
This  Python script that takes in a URL, sends a request to theURL and
displays the body of the response
"""

from sys import argv
import requests

if __name__ == '__main__':
    r = requests.get(argv[1])
    if r.status_code != 200:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
