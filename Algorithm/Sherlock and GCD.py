from fractions import gcd
t = input()
a = []
n = []
for i in range(t):
    n.append(input())
    a.append(map(int,raw_input().split()))
for i in a:
    l = len(i)
    if l >1:
        g = gcd(i[0],i[1])
    else:
        g = i[0]
    for j in range(2,l):
        if g==1:
            break
        g = gcd(g,i[j])
    if g==1:
        print 'YES'
    else:
        print 'NO'