#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_list = list(set(my_list))
    for i in my_list:
        sum += 1
    return sum
