#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""

import urllib.request as request
from sys import argv

if __name__ == '__main__':
    with request.urlopen(argv[1]) as r:
        headers = dict(r.info())
        if 'X-Request-Id' in headers:
            print(headers['X-Request-Id'])
