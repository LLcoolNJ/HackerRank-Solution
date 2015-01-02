from math import sqrt
def init(n,k):
	a = [0]
	for i in xrange(1,n):
		a.append((i*((3*i)-1))/2)
	for i in xrange(n,10**6+1):
		a.append(0)
	return a
def solve(n,k):
	a = init(n,k)
	for i in xrange(k+1,n):
		p3 = a[i]- a[i-k]
		p4 = a[i] + a[i-k]
		p1 = int((1+sqrt(1+24*p3))/6)
		p2 = int((1+sqrt(1+24*p4))/6)
		if p1<=10**6:
			if a[p1] == p3:
				print a[i]
			elif p2<=10**6:
				if a[p2] == p4:
					print a[i]
		elif p2<=10**6:
				if a[p2] == p4:
					print a[i]
n,k = map(int,raw_input().split())
solve(n,k)