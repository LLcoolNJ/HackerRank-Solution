def cal(a):
    if a%2==0:
        return True
    else:
        return False
n = input()
a = map(int,raw_input().split())
q = input()
qr = []
o = 'Odd'
e = 'Even'
for i in range(q):
    qr.append(map(int,raw_input().split()))
for i in range(q):
    x = qr[i][0]
    y = qr[i][1]
    if x>y:
        print o
    else:
        if cal(a[x-1]):
            if y!=x and x<n:
                if a[x]!=0:
                    print e
                else:
                    print o
            else:
                if cal(a[x-1]):
                    print e
                else:
                    print o
        else:
            print o