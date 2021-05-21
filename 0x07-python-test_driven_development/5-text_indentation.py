#!/usr/bin/python3
"""text_indentation function documentation"""


def text_indentation(text):
    """the function splits a string of text according to punctuation

    Args:
        text (str): the string of text to split

    Raises:
        TypeError: if the text called with the function is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if flag == 0:
            if c == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if c == '?' or c == '.' or c == ':':
                print(c)
                print()
                flag = 0
            else:
                print(c, end="")
