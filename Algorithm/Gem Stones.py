def main():
    t = input()
    w = []
    for i in range(t):
        w.append(raw_input())
    l = set(w[0])
    for i in range(1,len(w)):
        l = l.intersection(w[i])
    print len(l)
    
if __name__ == '__main__':
    main()