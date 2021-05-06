#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    sum, avg = 0, 0
    for i in my_list:
        sum += i[0] * i[1]
        avg += i[1]
    return sum / avg
