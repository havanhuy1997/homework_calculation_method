import math
import numpy as np
def f(x):
	return  np.log(x+1) -2*x + 0.5

e = 0.001
left = 0
right = 1
while right - left > e:
	t = (left + right) / 2
	if f(t) * f(left) < 0:
		right = t
	else:
		left = t
print(t)

# 0.4287109375
