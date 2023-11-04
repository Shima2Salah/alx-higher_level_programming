#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence) + 0
    if (sentence[0] is None):
        b = None
    else:
        b = sentence[0]
    return (a, b)
