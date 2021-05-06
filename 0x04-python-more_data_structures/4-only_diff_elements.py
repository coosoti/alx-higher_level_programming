#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    _set = []
    new_list = []
    for y in set_1:
        for x in set_2:
            if x == y:
                _set.append(x)
    set_1.update(set_2)
    for i in set_1:
        for j in _set:
            if j != i:
                new_list.append(i)
    return new_list
