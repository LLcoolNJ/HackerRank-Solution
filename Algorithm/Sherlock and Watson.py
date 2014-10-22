def main():
    w = map(int,raw_input().split())
    n = w[0]
    k = w[1]
    q = w[2]
    arr = map(int,raw_input().split())
    for i in range(k):
        w = arr.pop()
        arr.insert(0,w)
    oup = []
    for i in range(q):
        oup.append(arr[input()])
    for i in oup:
        print i


if __name__ == '__main__':
    main()
