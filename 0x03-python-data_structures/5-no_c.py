#!/usr/bin/python3
def no_c(my_string):
    x = len(my_string)
    i = 0
    new_str = ""
    while i < x:
        if (my_string[i] != "c" and my_string[i] != "C"):
            new_str += my_string[i]
        i += 1
    return new_str
