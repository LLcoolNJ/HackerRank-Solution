from collections import Counter

def main():
    a = raw_input()
    b = raw_input()
    ca = Counter(a)
    cb = Counter(b)
    count = 0
    for i in ca.keys():
        if cb.has_key(i):
            if cb[i] > ca[i]:
                count += cb[i] - ca[i]
            else:
                count += ca[i] - cb[i]
            del(cb[i])
        else:
            count += ca[i]
    for i in cb.keys():
        count += cb[i]
    print count

if __name__ == '__main__':
    main()
