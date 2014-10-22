import math
t = input()
i = []
for x in xrange(t):
    i.append(input())
for x in i:
    d = 4*(x+1)
    n = math.ceil((math.sqrt(d) - 2)/2)
    if(int(n)%2 == 0):
        print 'even'
    else:
        print 'odd'
