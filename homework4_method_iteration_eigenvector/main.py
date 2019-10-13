import sys
sys.path.append('..')
from util import read_raw_input, write_to_output
import numpy as np
import math

INPUT_FILE_NAME = 'input_homework4.txt'
OUTPUT_FILE_NAME = 'output_homework4.txt'
PRECISION = 0.01

def init_x(rank):
    matrix = []
    for _ in range(rank):
        matrix.append([1])
    return np.array(matrix)

def cal_dif(new_eigenvalue, previous_eigenvalue):
    if previous_eigenvalue:
        return abs(new_eigenvalue - previous_eigenvalue)
    else:
        return None

def write_eigenvector(x, f_output):
    l = max(x)
    write_to_output('\nEigenvector: \n{}'.format(str(x / l)), f_output)

def write_heading_for_ouput(rank, f_output):
    write_to_output('%3s|' % 'k', f_output, end='')
    for i in range(rank):
        x = 'x' + str(i + 1)
        write_to_output('%15s|' % x, f_output, end='')
    write_to_output('%15s|' % 'eigenvalue', f_output, end='')
    write_to_output('%15s|' % 'Precision', f_output, end='')

def write_line_to_output(step_count, x, eigenvalue, precision, f_output):
    write_to_output('\n', f_output)
    write_to_output('%3d|' % step_count, f_output, end='')
    for row in x:
        write_to_output('%15.4f|' % row[0], f_output, end='')
    if eigenvalue:
        write_to_output('%15.4f|' % eigenvalue, f_output, end='')
    else:
        write_to_output('%15s|' % '---', f_output, end='')
    if precision:
        write_to_output('%15.4f|' % precision, f_output, end='')
    else:
        write_to_output('%15s|' % '---' , f_output, end='')
    write_to_output('\n', f_output)

if __name__ == "__main__":
    f_output = open(OUTPUT_FILE_NAME, 'w')

    raw_matrix = read_raw_input(INPUT_FILE_NAME)
    matrix_a = np.array(raw_matrix)

    rank = len(raw_matrix)
    write_heading_for_ouput(rank, f_output)

    x = init_x(rank)
    dif = PRECISION + 1
    previous_eigenvalue = None
    count_step = 0
    write_line_to_output(count_step, x, None, None, f_output)
    while dif > PRECISION:
        count_step += 1
        new_x = matrix_a.dot(x)
        new_eigenvalue = sum([new_x[i][0]/ x[i][0] for i in range(rank)]) / rank
        dif = cal_dif(new_eigenvalue, previous_eigenvalue)
        write_line_to_output(count_step, new_x, new_eigenvalue, dif, f_output)
        x = new_x
        previous_eigenvalue = new_eigenvalue
        if dif is None:
            dif = PRECISION + 1

    write_to_output('EigenValue={}'.format(new_eigenvalue), f_output)
    write_eigenvector(x, f_output)
    f_output.close()
