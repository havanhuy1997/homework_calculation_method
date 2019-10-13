import sys
sys.path.append('..')
from util import read_maxtrix_from_input

INPUT_FILE_NAME = 'input_homework1.txt'
OUTPUT_FILE_NAME = 'output_homework1.txt'

out_file = open(OUTPUT_FILE_NAME, 'w')

def print_mesg(mesg):
    print(mesg)
    out_file.write(mesg + '\n')
    out_file.flush()

def print_matrix(matrix):
    for row in matrix:
        for i in row: 
            print('%12.4f|' %i, end=' ')
            out_file.write('%12.4f|' %i)
        print('\n')
        out_file.write('\n')
    print('\n')
    out_file.write('\n')
    out_file.flush()

def divide_row_with_first_element(row, i):
    mesg = 'Divide {}-th row with {}'.format(i + 1, row[i])
    print(mesg)
    out_file.write(mesg + '\n') 
    return row / row[i]

def cal(i, matrix):
    rand = len(matrix)
    if i == rand - 1:
        return
    else:
        row = matrix[i]
        if round(row[i], 3) != 1:
            matrix[i] = divide_row_with_first_element(row, i)
            print_matrix(matrix)
        for j in range(i + 1, rand):
            factor = matrix[j][i]
            mesg = 'row[{}] = row[{}] - row[{}] * ({})'.format(j + 1, j + 1, i + 1, factor) 
            print_mesg(mesg)
            matrix[j] = matrix[j] - matrix[i] * factor 
            print_matrix(matrix)
        cal(i + 1, matrix)

def reverse_call(i, matrix):
    if i == -1:
        return
    else:
        row = matrix[i]
        if round(row[i], 3) != 1:
            matrix[i] = divide_row_with_first_element(row, i)
            print_matrix(matrix)
        for j in range(i - 1, -1, -1):
            factor = matrix[j][i]
            mesg = 'row[{}] = row[{}] - row[{}] * ({})'.format(j + 1, j + 1, i + 1, factor) 
            print_mesg(mesg)
            matrix[j] = matrix[j] - matrix[i] * factor
            print_matrix(matrix)
        reverse_call(i - 1, matrix)

if __name__ == "__main__":
    matrix = read_maxtrix_from_input(INPUT_FILE_NAME)
    rand = len(matrix)
    cal(0, matrix)
    reverse_call(rand - 1, matrix)

    x = []
    inverse_matrix= []
    for row in matrix:
        x.append(row[-1])
        inverse_matrix.append(row[rand: rand + rand])

    print_mesg('Рерультат:')
    print_mesg(str(x))
    print_mesg('Обратная матрица')
    print_matrix(inverse_matrix)
    out_file.close()