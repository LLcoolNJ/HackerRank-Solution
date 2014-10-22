n,k = map(int,raw_input().split())
a = map(int,raw_input().split())
a = sorted(a,reverse=True)
s = 0
p = 0
l = 1
for i in a:
    if p==k:
        p=0
        l += 1
    s += i*l
    #print i*l
    p += 1
print s