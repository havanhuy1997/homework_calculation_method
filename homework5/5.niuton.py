import math
import numpy as np

def f(x):
	return  np.log(x+1) -2*x + 0.5

def f1(x):
	return 1 / (x+1) - 2
	
e = 0.001
x0  = 0.5

def method(x0):
	while True:
		x = x0 - f(x0) / f1(x0)
		e2 = abs(x-x0)
		if e2 <= e:
			break
		x0 = x
	return x, e2
x, e2 = method(x0)
print('x =', x, 'precision =', e2)

# x = 0.42821161923307766 precision = 0.0008872118480456326