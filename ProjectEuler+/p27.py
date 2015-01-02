#import time
 
def primes_xrange(stop):
    primes = [True] * stop
    primes[0], primes[1] = [False] * 2
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2::ind] = [False] * (((stop - 1)//ind) - 1)
    return primes
 
#start = time.time()
 
P = primes_xrange(6842000)
a_max, b_max, c_max = 0, 0, 0
p = input()
for a in range(-p,p+1):
    for b in range(1,p+1):
        if P[b] is False: continue
        if b < -1600-40*a or b< c_max: continue
        c, n = 0, 0
        while P[n**2 + a*n + b] is True:
            c += 1
            n += 1
        if c > c_max:
            a_max, b_max, c_max = a, b, c
 
print a_max, b_max
#print time.time()-start

'''
from timeit import default_timer as timer
import math
start = timer()

def longestPrimeQuadratic(alim, blim):

    def isPrime(k): # checks if a number is prime
        if k < 2: return False
        elif k == 2: return True
        elif k % 2 == 0: return False
        else: 
            for x in range(3, int(math.sqrt(k)+1), 2):
                if k % x == 0: return False

        return True 

    longest = [0, 0, 0] # length, a, b
    for a in range((alim * -1) + 1, alim):
        for b in range(2, blim):
            if isPrime(b):
                count = 0
                n = 0
                while isPrime((n**2) + (a*n) + b):
                    count += 1
                    n += 1

                if count > longest[0]:
                    longest = [count, a, b]

    return longest
n = input()
ans = longestPrimeQuadratic(n+1, n+1)
print ans
print (timer() - start)
'''