#!/usr/bin/python3
def remove_char_at(str, n):
    x = str[0:n]
    y = str[n + 1:len(str)]
    if (n >= 0):
        return (x + y)
    if (n < 0):
        return (str)
