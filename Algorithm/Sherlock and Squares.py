from math import ceil, sqrt, floor
def c(a,b):
    return int(floor(sqrt(b)) - ceil(sqrt(a)) + 1)
for i in xrange(input()):
    a,b = map(int,raw_input().split())
    print c(a,b)