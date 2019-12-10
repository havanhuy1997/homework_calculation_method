import math
import numpy as np

def f(x):
	return math.sin(x) - x
	
x_list = [0, math.pi / 6, 2*math.pi / 6]
y_list = [f(i) for i in x_list]
check_x = math.pi / 4

def lagran(rank, x):
	result = 0
	for i in range(rank + 1):
		temp = 1
		for j in range(rank + 1):
			if j != i:
				temp *= (x - x_list[j]) / (x_list[i] - x_list[j])
		result += y_list[i] * temp
	return result
	
def different(n, i_th):
	if n == 1:
		return (y_list[i_th + 1] - y_list[i_th]) / (x_list[i_th + 1] - x_list[i_th])
	else:
		return (different(n-1, i_th+1) - different(n-1, i_th)) / (x_list[i_th+2] - x_list[i_th])
	
def niuton(rank, x):
	result = y_list[0]
	for i in range(rank):
		t = 1
		for j in range(i):
			t = t * (x - x_list[i])
		result += different(i +1, 0) * t
	return result


l1 = lagran(1, check_x)
l2 = lagran(2, check_x)
print('погрешность лагланжа 1:', abs(l1 - f(check_x)))
print('погрешность лагланжа 1:', abs(l2 - f(check_x)))

n1 = niuton(1, check_x)
n2 = niuton(2, check_x)
print('погрешность нЬютон 1:', abs(n1 - f(check_x)))
print('погрешность нЬютон 1:', abs(n2 - f(check_x)))

# погрешность лагланжа 1: 0.04289321881345251
# погрешность лагланжа 1: 0.007347254767382988
# погрешность нЬютон   1: 0.03322104076227283
# погрешность нЬютон   1: 0.030747116947069136
