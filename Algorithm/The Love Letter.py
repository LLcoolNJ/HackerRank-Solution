def main():
    t = input()
    s = []
    for i in range(t):
        s.append(raw_input())
    for i in range(t):
        l = s[i]
        out = 0
        j = 0
        k = len(l) - 1
        while(j<k):
            p = ord(l[j])
            q = ord(l[k])
            if(p<q):
                out += q-p
            elif(p>q):
                out += p-q
            j += 1
            k -= 1
        print out
         

if __name__ == '__main__':
    main()