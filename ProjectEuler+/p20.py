from math import factorial
def cnt_fac(n):
	sm = 0
	s = str(factorial(n))
	l = len(s)
	for i in xrange(l):
		sm += int(s[i])
	return sm
for i in xrange(input()):
	print cnt_fac(input())