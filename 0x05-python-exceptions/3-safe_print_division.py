#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
    except (ZeroDivisionError):
        x = None
        print(end="")
    else:
        print(end="")
    finally:
        print("Inside result: {}".format(x))
    return x
