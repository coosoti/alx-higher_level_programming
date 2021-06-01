#!/usr/bin/python3
"""this script adds all arguments to a Python list, then save them to a file"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

if __name__ == "__main__":
    try:
        json_list = load_from_json_file(filename)
    except Exception:
        json_list = []

    for i in argv[1:]:
        json_list.append(i)

    save_to_json_file(json_list, filename)
