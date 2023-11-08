#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = None
    for x, y in a_dictionary.items():
        if max is None or max < y:
            max = y
            max_key = x
    return max_key
