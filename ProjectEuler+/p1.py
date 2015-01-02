def s(l):
	n3 = l/3
	n5 = l/5
	n15 = l/15
	su = 0
	su += 3*(n3*(n3+1))/2
	su += 5*(n5*(n5+1))/2
	su -= 15*(n15*(n15+1))/2
	print su
for i in xrange(input()):
    s(input()-1)