def fibPlus((a,b),(c,d)):
    bd = b*d
    return (bd-(b-a)*(d-c), a*c+bd)
 
def unFib((a,b),n):
    if n<a:
        return (0,0,1)
    else:
        (k,c,d) = unFib(fibPlus((a,b),(a,b)),n)
        (e,f) = fibPlus((a,b),(c,d))
        if n<e: return (2*k, c, d)
        else:
            return (2*k+1,e,f)
 
def isfib(n):
    (k,a,b) = unFib((1,1),n)
    return n==a

def main():
    t = input()
    y = "IsFibo"
    n = "IsNotFibo"
    inp = []
    for i in range(t):
        inp.append(input())
    for i in inp:
        if isfib(i):
            print y
        else:
            print n


if __name__ == '__main__':
    main()
