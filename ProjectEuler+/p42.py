from math import sqrt
def root(tn):
	s = sqrt(1+8*tn)
	if s%1 == 0:
		return int((s-1)/2)
	else:
		return -1
for i in xrange(input()):
    print root(input())