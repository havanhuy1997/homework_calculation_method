import sys
sys.path.append('..')
from util import read_raw_input, write_to_output

INPUT_FILE_NAME = 'input_homework2.txt'
OUTPUT_FILE_NAME = 'output_homework2.txt'
RANK_LEFT_MATRIX = 5

def read_input():
    raw_matrix = read_raw_input(INPUT_FILE_NAME)
    a = [0] + [raw_matrix[i][i-1] for i in range(1, RANK_LEFT_MATRIX)]
    b = [raw_matrix[i][i] for i in range(RANK_LEFT_MATRIX)]
    c = [raw_matrix[i][i+1] for i in range(RANK_LEFT_MATRIX - 1)] + [0]
    d = [raw_matrix[i][-1] for i in range(RANK_LEFT_MATRIX)]
    return a, b, c, d

def write_output(array_dict):
    out_file = open(OUTPUT_FILE_NAME, 'w')

    for heading in array_dict.keys():
        write_to_output('%15s|' % heading, out_file, end='')
    write_to_output('\n', out_file)
    for i in range(RANK_LEFT_MATRIX):
        for array in array_dict.values():
            write_to_output('%15.10f|' % array[i], out_file, end='')
        write_to_output('\n', out_file)
    out_file.close()

if __name__ == "__main__":
    try:
        a, b, c, d = read_input()
        p = []
        q = []
        
        for i in range(RANK_LEFT_MATRIX):
            if i == 0 :
                previous_p = 0
                previous_q = 0
            else:
                previous_p = p[i-1]
                previous_q = q[i-1]

            p_i = -c[i] / (b[i] + a[i] * previous_p)
            q_i = (d[i] - a[i] * previous_q) / (b[i] + a[i] * previous_p)
            p.append(p_i)
            q.append(q_i)

        x = [None for i in range(RANK_LEFT_MATRIX)]
        for i in range(RANK_LEFT_MATRIX - 1, -1, -1):
            if i == RANK_LEFT_MATRIX - 1:
                x[i] = q[i]
            else:
                x[i] = p[i] * x[i+1] + q[i] 

        write_output({
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'p': p,
            'q': q,
            'x': x
        })
    except Exception as e:
        print(e)