#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = 0
    for x in range(1, len(sys.argv)):
        n = n + int(sys.argv[x])
    print("{}".format(n))
