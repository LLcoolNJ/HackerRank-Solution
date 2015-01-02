a = [0, 9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889L, 98888888889L, 1088888888889L, 11888888888889L, 128888888888889L, 1388888888888889L, 14888888888888889L, 158888888888888889L, 1688888888888888889L]
def get(n):
	if n in a:
		return [a.index(n)]
	else:
		pre = 0
		for i in xrange(1,len(a)):
			nxt = a[i]
			if nxt > n and pre <n:
				return (i-1,i)
			else:
				pre = nxt
def nth(n):
	ind = get(n)
	if len(ind) == 1:
		return str(a[ind[0]])[-1]
	else:
		p = str(pow(10,ind[1]) - 1 - (a[ind[1]] - n)/ind[1])
		r = (a[ind[1]] - n)%ind[1]
		p = p[-1::-1]
		return p[r]
def solve(t):
	for i in xrange(t):
		a = map(int,raw_input().split())
		s = 1
		for i in a:
			s *= int(nth(i))
		print s
t = input()
solve(t)