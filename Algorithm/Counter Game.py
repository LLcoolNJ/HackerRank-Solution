import math
def c(n):
	cn = 0
	while n!=1:
		if (n&(n-1)==0 and n!=0):
			n /= 2
		else:
			i= n.bit_length()-1
			n -= int(math.pow(2,i))
		cn += 1
	return cn
for i in xrange(input()):
	n = c(input())
	if n%2==0:
		print 'Richard'
	else:
		print 'Louise'