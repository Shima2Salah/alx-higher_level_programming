#!/usr/bin/python3
alpha = 97
while (alpha >= 97 and alpha <= 122):
    if (alpha != 101 and alpha != 113):
        print("{:c}".format(alpha), end="")
    alpha += 1
