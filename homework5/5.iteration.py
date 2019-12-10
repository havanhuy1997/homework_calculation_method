import math
import numpy as np

def f(x):
	return  np.log(x+1) -2*x + 0.5

def f2(x):
	return -1 / ((x+1) ** 2) 
	
e = 0.001
x0  = 0.5
x1  = 1

def method(x0, x1):
	while True:
		x = x1 - f(x1)*(x1 - x0) / (f(x1) - f(x0))
		e2 = abs(x-x1)
		if e2 <= e:
			break
		x0 = x1
		x1 = x
	return x, e2
x, e2 = method(x0, x1)
print('x =', x, 'precision =', e2)

# x = 0.42821190653508506 precision = 0.00042650588678799783