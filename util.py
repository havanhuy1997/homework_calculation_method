import numpy as np

def read_maxtrix_from_input(file_name):
    f = open(file_name)
    lines = [line.strip() for line in f.readlines() if line.strip()]
    f.close()

    matrix = []

    for line in lines:
        row = [float(i.strip()) for i in line.split()]
        matrix.append(row)

    rand_matrix = len(matrix)


    for i in range(rand_matrix):
        row = matrix[i]
        row_of_1_matrix = [0 for i in range(rand_matrix)]
        row_of_1_matrix[i] = 1
        matrix[i] = np.array(row[0:rand_matrix] + row_of_1_matrix + [row[-1]])

    matrix = np.array(matrix)
    return matrix

def read_raw_input(file_name):
    raw_matrix = []
    f = open(file_name)
    for line in f:
        row = [float(i) for i in line.split()]
        raw_matrix.append(row)
    return raw_matrix

def write_to_output(s, f_out, end=None):
    if end is not None:
        print(s, end=end)
    else:
        print(s)
    f_out.write(s)