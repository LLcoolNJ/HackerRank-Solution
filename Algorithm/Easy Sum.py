def e_sum(n,m):
    s = 0
    sn = (m*(m-1))/2
    s += sn*(n/m)
    r = n%m
    s += ((r+1)*(r))/2
    return s
for i in xrange(input()):
    n,m = map(int,raw_input().split())
    print e_sum(n,m)