#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniquelist = set(my_list)
    for id in uniquelist:
        sum += id
    return sum
