#!/usr/bin/python3
"""Find a Peak in a List"""
def find_peak(list_of_integers):
    """Find a Peak in a list"""
    my_list = list_of_integers
    b = len(my_list)
    if (b <= 2):
        return (None)
    for i in range(1, b - 1):
	    if (my_list[i - 1] <= my_list[i] >= my_list[i + 1]):
	        return (my_list[i])
    return (None)
