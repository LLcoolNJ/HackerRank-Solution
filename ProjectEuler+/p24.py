facs = [479001600, 39916800, 3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
def pr(n):
	s = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
	out = ''
	for i in facs:
		if n/i>0:
			j = n/i
			n = n%i
			if n == 0:
				j-=1
				n+= i
			#print j
			out += str(s[j])
			del(s[j])
		else:
			#print 0
			out += s[0]
			del(s[0])
	return out + s[0]
for i in xrange(input()):
	print pr(input())