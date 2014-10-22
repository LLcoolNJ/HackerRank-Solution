import re
n = input()
w = ''
for i in range(n):
    w += raw_input().strip()
t = input()
wr = []
for i in range(t):
    wr.append(raw_input().strip())
for i in wr:
    j = i[:-2]
    if i[-2] =='z':
        j+='se'
    else:
        j+='ze'
    print w.count(i)+w.count(j)