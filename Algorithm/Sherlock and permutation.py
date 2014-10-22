mod = 10**9+7
def ncr(n,r):
    s = 1
    if r> n-r:
        r = n-r
    for i in xrange(r):
        s = ((s*(n-i))/(i+1))
    return s%mod

for i in xrange(input()):
    n,m = map(int,raw_input().split())
    print ncr(n+m-1,m-1)