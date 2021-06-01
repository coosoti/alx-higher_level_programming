#!/usr/bin/python3
"""write_file function documentation"""


def write_file(filename="", text=""):
    """this function writes a string to a text file(UTF8)

    Args:
        text (str): a string to write to the file
    Return:
        number of characters written
    """

    with open(filename, "w", encoding='utf-8') as myFile:
        return myFile.write(text)
