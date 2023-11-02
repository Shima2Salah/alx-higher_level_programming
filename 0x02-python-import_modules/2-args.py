#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    x = 1
    if (n == 0):
        print("{} arguments.".format(n))
    if (n == 1):
        print("{} argument:".format(n))
        print("{}: {}".format(n ,sys.argv[1]))
    if (n > 1):
        print("{} arguments:".format(n))
        while x <= n:
            print("{}: {}".format(x, sys.argv[x]))
            x += 1
