#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        x = len(i) - 1
        j = 0
        while (j <= x):
            print("{}".format(i[j]), end="")
            if j != x:
                print(" ", end="")    
            j += 1
        print()
