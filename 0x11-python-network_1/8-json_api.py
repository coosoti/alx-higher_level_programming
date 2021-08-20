#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

from sys import argv
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ""
    r = requests.post(url, data={'q': letter})
    try:
        json_dict = r.json()
        if json_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_dict['id'], json_dict['name']))
    except ValueError:
        print("Not a valid JSON")
