#!/usr/bin/python3

"""Matrix multiplication function"""

def matrix_mul(m_a, m_b):

    """Multiplies m_a by m_b"""

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for a in m_a:
        if type(a) is not list:
            raise TypeError('m_a must be a list of lists')
    for a in m_b:
        if type(a) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for a in m_a:
        if len(a) == 0:
            raise ValueError("m_a can't be empty")
    for a in m_b:
        if len(a) == 0:
            raise ValueError("m_b can't be empty")

    for a in m_a:
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for a in m_b:
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError('m_b should contain only integers or floats')

    for a in m_a:
        if len(a) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for a in m_b:
        if len(a) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    rowA = len(m_a)
    colA = len(m_a[0])
    rowA = len(m_b)
    colA = len(m_b[0])

    if colA != rowB:
        raise ValueError("m_a and m_b can't be multiplied")

    new = [[0 for a in range(colB)] for b in range(rowA)]
    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                new[i][j] += m_a[i][k] * m_b[k][j]
    return new
