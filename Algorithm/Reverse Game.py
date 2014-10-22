def find(n,k):
	if k == n/2:
		return n
	elif k< n/2:
		return ((k+1)*2 - 1)
	else:
		return ((n-k)*2)
for i in xrange(input()):
	n,k = map(int,raw_input().split())
	print find(n-1,k)