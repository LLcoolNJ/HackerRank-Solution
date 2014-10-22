from collections import Counter
def main():
    w = raw_input()
    c = Counter(w)
    if(len(w)%2==0):
            flag = True
            for i in c.values():
                    if i%2 !=0:
                            flag = False
                            break
    else:
            flag = True
            count = 0
            for i in c.values():
                    if i%2 !=0:
                            count += 1
                    if count >=2:
                            flag = False
                            break
    if(flag == True):
            print 'YES'
    else:
            print 'NO'
if __name__ == '__main__':
    main()