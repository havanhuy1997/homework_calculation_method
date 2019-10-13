import sys
sys.path.append('..')
from util import read_raw_input, write_to_output
import numpy as np
import math

INPUT_FILE_NAME = 'input_homework3.txt'
OUTPUT_FILE_NAME = 'output_homework3.txt'
PRECISION = 0.01
RANK_MATRIX = None

def read_input():
    global RANK_MATRIX
    matrix_alpha = []
    matrix_beta = []

    raw_input = read_raw_input(INPUT_FILE_NAME)
    RANK_MATRIX = len(raw_input)

    for i, line in enumerate(raw_input):
        matrix_beta.append(np.array([line[-1] / line[i]]))
        row = []
        for j, e in enumerate(line[0:-1]):
            if j != i:
                row.append(- e / line[i])
            else:
                row.append(0)
        row = np.array(row)
        matrix_alpha.append(row)

    matrix_alpha = np.array(matrix_alpha)
    matrix_beta = np.array(matrix_beta)
    return matrix_alpha, matrix_beta

def cal_dif(x1, x2):
    dif_matrix = x1 - x2
    return max(np.abs(dif_matrix))[0]

def write_line_to_output(count_step, x_matrix, e_matrix, f_ouput):
    write_to_output('%5d|' % count_step , f_ouput, end='')
    for el in x_matrix:
        write_to_output('%10.4f|' % el[0], f_ouput, end='')
    if e_matrix is not None:
        for el in e_matrix:
            write_to_output('%10.4f|' % el[0], f_ouput, end='')
    else:
        for _ in range(RANK_MATRIX):
            write_to_output('%10s|' % '---', f_ouput, end='')
    write_to_output('\n', f_ouput)

def write_heading_to_output(f_output):
    write_to_output('%5s|' % 'k', f_output, end='')
    for i in range(RANK_MATRIX):
        write_to_output('%10s|' % ('x' + str(i)), f_output, end='')
    for i in range(RANK_MATRIX):
        write_to_output('%10s|' % ('e' + str(i)), f_output, end='')
    write_to_output('\n', f_output)

def cal_precision_matrix(previous_x, new_x):
    return np.abs(new_x - previous_x)

def init_x(rank):
    matrix = []
    for _ in range(rank):
        matrix.append(
            np.array([0])
        )
    return np.array(matrix)

def cal_norma(matrix):
    result = 0
    for row in matrix:
        for el in row:
            result += el ** 2
    return math.sqrt(result)

if __name__ == "__main__":
    f_output = open(OUTPUT_FILE_NAME, 'w')

    matrix_aplha, matrix_beta = read_input()

    norma = cal_norma(matrix_aplha)
    if norma < 1:
        write_to_output('norma = {} < 1 \n'.format(norma), f_output)
    else:
        write_to_output('Norma > 1', f_output)
        import sys
        sys.exit(-1)

    dif = PRECISION + 1
    x = init_x(RANK_MATRIX)
    count_step = 0
    write_heading_to_output(f_output)
    write_line_to_output(count_step, x, None, f_output)
    while dif > PRECISION:
        count_step += 1
        new_x = matrix_aplha.dot(x) + matrix_beta
        dif = cal_dif(new_x, x)
        write_line_to_output(
            count_step, 
            new_x, 
            cal_precision_matrix(new_x, x),
            f_output
        )
        x = new_x
    
    write_to_output('Skip iteration with precision {}\n'.format(dif), f_output)
    write_to_output(str(x), f_output)
    f_output.close()