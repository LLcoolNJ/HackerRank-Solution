t = "Go On Bob"
f = "Better Luck Next Time"
from math import sqrt
def check(x):
	s = sqrt(8*x+1)
	if s%1 ==0:
		n = (s-1)/2.0 
		if (s-1)/2.0 %1 == 0:
			return t + ' ' + str(int(n))
		else:
			return f
	else:
		return f

for i in xrange(input()):
	print check(input())