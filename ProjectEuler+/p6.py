def diff(n):
    return (n*(n*n-1)*(3*n+2))/12
a = []
for i in range(input()):
    a.append(input())
for i in a:
    print diff(i)