#!/usr/bin/env python3
def no_c(my_string):
    my_string_list = list(my_string)
    idx = 0
    for index in my_string_list:
        if index == 'c' or index == 'C':
            my_string_list[idx] = ""
        idx += 1
    return "".join(my_string_list)
