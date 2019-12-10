import numpy as np
import math

def f1(x,y):
	return x*x / 4 + x + y*y - 1
def f2(x,y):
	return 2 * y - math.e ** x - x

def j(x,y):
	return np.array([
		[x / 2 + 1, 2 * y],
		[-math.e ** x - 1, 2]
	])
	
def detj(x,y):
	matrix_j = j(x, y)
	return matrix_j[0][0] * matrix_j[1][1] - matrix_j[0][1] * matrix_j[1][0]
	
e = 0.001
x = -1
y = 0.1
print('choose x0=', x, 'y0=', y)
while True:
	j1 = j(x,y)
	x1 = x - (1/ detj(x,y)) * (j1[1][1] * f1(x,y) - j1[0][1] * f2(x,y))
	y1 = y - (1/ detj(x,y)) * (j1[0][0] * f2(x,y) - j1[1][0] * f1(x,y))
	if abs(x-x1) < e and abs(y-y1) < e:
		break
	x = x1
	y = y1
print(x, y)