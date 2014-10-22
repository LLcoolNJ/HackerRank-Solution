from fractions import gcd
out = []
for i in range(input()):
    a,b,c = [int(i) for i in raw_input().strip().split()]
    if c%gcd(a,b) == 0 and (c<=a or c<=b):
        out.append("YES")
    else:
        out.append("NO")
for i in out:
    print i