#!/usr/bin/python3
def common_elements(set_1, set_2):
    _set = []
    for y in set_1:
        for x in set_2:
            if y == x:
                _set.append(y)

    return _set
