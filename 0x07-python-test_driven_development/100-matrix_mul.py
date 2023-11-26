#!/usr/bin/python3
"""Module that multiply 2 matrixes
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrixes
    Args:
        m_a = First matrix
        m_b = Second matrix
    Raises:
        TypeError: m_a or m_b must be a list
        TypeError: m_a or m_b must be a list of lists
        TypeError: m_a or m_b should contain only integers or floats
        TypeError: each row of m_a or m_b must be of the same size
        ValueError: m_a or m_b can't be empty
        ValueError: m_a and m_b can't be multiplied
    Returns:
        multiplied matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")
    k = []
    i = 0
    while i < len(m_a):
        n = 0
        q = []
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")
        if len(m_a[i]) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if len(m_b[i]) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        while n < len(m_b[i]):
            j = 0
            sum = 0
            while j < len(m_a[i]):
                if not isinstance(m_a[i][j], (int, float)):
                    raise ValueError("m_a should contain \
only integers or floats")
                if not isinstance(m_b[j][n], (int, float)):
                    raise ValueError("m_b should contain \
only integers or floats")
                if len(m_a[0]) != len(m_b):
                    raise ValueError("m_a and m_b can't be multiplied")
                sum += m_a[i][j] * m_b[j][n]
                j += 1
            q.append(sum)
            n += 1

        k.append(q)
        i += 1
    return k
