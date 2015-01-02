from itertools import chain
def first(gen):
    try:
        return gen.next()
    except StopIteration :
        return None
def prime_factors(n):
    while n > 1 :
        ff = first(val for val in chain(
                        xrange(2,int(n**0.5+1.0)),[n]) if n % val == 0)
        yield ff
        n = n / ff
n = []
for i in range(input()):
    n.append(input())
for i in n:
    print max(prime_factors(i))