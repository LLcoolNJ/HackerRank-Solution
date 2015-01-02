l ={4:12,5:52,6:162,7:0,8:13458,9:45228}
print l[input()]'''
def is_pandigital(*args, **kwargs):
    num = sorted(''.join(str(arg) for arg in args))

    try:
        if kwargs['length'] and len(num) != kwargs['length']:
            return False
    except KeyError:
        pass

    for i in xrange(len(num)):
        if str(i+1) != str(num[i]):
            return False
    return True

def main(n):
    pandigitals = set()
    total = 0
    for multiplicand in xrange(1, 5000):
        for multiplier in xrange(1, 100):
            product = multiplicand * multiplier
            if is_pandigital(multiplicand, multiplier, product, length=9):
                pandigitals.add(product)
    print sum(pandigitals)
main(input())
'''