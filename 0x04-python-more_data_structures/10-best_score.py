#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    for value in a_dictionary.values():
        if max <= value:
            max = value
    return max
