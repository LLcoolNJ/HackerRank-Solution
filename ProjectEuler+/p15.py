mod = 10**9+7
def mcn(m,n):
	r = m
	if m>n:
		r = n
	p = 1
	for i in xrange(r):
		p *= (m+n) - i
		p /= i+1
	return p%mod
n = []
for i in xrange(input()):
	n.append(map(int,raw_input().split()))
for i in n:
	print mcn(i[0],i[1])