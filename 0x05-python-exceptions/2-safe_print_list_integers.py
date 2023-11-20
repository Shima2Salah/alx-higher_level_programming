#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    n = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            print(end="")
            n += 1
        else:
            print(end="")
        i += 1
    print("")
    return (i - n)
