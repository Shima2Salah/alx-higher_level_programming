#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = 0
    for i in range(len(my_list)):
        n += my_list[i]
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                n -= my_list[j]
    return (n)
