#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        frst_list = []
        for j in range(len(matrix[i])):
            mat = matrix[i][j] * matrix[i][j]
            frst_list.append(mat)
        new_matrix.append(new_matrix)
    return (new_matrix)
