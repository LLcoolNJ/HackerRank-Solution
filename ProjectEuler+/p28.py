mod = 10**9+7
def s(L):
	n = (L-1)//2
	return ((16*n**3 + 30*n**2 + 26*n + 3) // 3)%mod
for _ in xrange(input()):
	print s(input())