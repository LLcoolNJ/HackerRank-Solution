def lcm(a,b):
    gcd, tmp = a,b
    while tmp != 0:
        gcd,tmp = tmp, gcd % tmp
    return a*b/gcd
n = []
for i in range(input()):
    n.append(input())
for i in n:
    print reduce(lcm,range(1,i+1))