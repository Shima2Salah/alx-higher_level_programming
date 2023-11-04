#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even_list = []
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            even_list.append(True)
        else:
            even_list.append(False)
    return (even_list)
