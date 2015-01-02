def solve(n):
	mod = pow(10,10)
	c = 0
	s = 1
	if n > 100000:
		c = 3031782500L
		s = 100001
	for i in xrange(s,n+1):
		c += pow(i,i,mod)
		c %= mod
	return c
print solve(input())