#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    for x, y in a_dictionary.items():
        if max <= y:
            max = y
            max_key = x
    return max_key
