t = input()
n = []
for i in range(t):
    n.append(input())
for i in n:
    st = str(i)
    s = list(set(str(i)))
    cnt = 0
    for j in s:
        if j != '0':
            if i%int(j)==0:
                cnt += st.count(j)
    print cnt