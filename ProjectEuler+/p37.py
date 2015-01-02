#import time

#########################################################
'''
Miller-rabin primality test
Valid for all 64-bit unsigned integers
Sometimes wrong for numbers greater
'''
def check_composite(n, s, d, a):
    '''
    check compositeness of n with witness a
    (n,s,d) should satisfy d*2^s = n-1 and d is odd
    '''
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for y in xrange(1, s):
        x = x * x % n
        if x == 1:
            return True
        if x == n - 1:
            return False
    return True

small_primes = set([3,5,7,11,13,17,19,23,29,31,37])
small_is_prime = [s in small_primes for s in xrange(38)]
small_is_prime[2] = True

# witnesses for different bounds (taken from http://miller-rabin.appspot.com/ )
witnesses_bounds = [
    (341531, [9345883071009581737]),
    (716169301, [15, 13393019396194701]),
    (154639673381, [15, 176006322, 4221622697]),
    (47636622961201, [2, 2570940, 211991001, 3749873356]),
    (3770579582154547, [2, 2570940, 880937, 610386380, 4130785767]),
]
# set of witnesses for < 2^64 (taken from http://miller-rabin.appspot.com/ )
i64_witnesses = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]


def is_prime(n):
    '''
    returns True if n is probably prime, and False if n is definitely not prime.
    if n < 2^64, then is_prime(n) never returns a wrong answer.
    '''
    # if too small, check small_is_prime
    if n < 38:
        return small_is_prime[n]
    # check divisibility with small primes
    for s in small_primes:
        if n % s == 0:
            return False
    # find (d,s) such that d*2^s = n-1 with d odd
    d = n - 1
    s = 0
    while not d & 1:
        d >>= 1
        s += 1
    # find the best set of witnesses
    best_witnesses = i64_witnesses
    for bound, bound_ws in witnesses_bounds:
        if n < bound:
            best_witnesses = bound_ws
            break
    # check compositeness with the witnesses
    for a in best_witnesses:
        a %= n
        if a and check_composite(n, s, d, a):
            return False
    return True
def getL(n):
	s = str(n)[1:]
	while len(s) != 0:
		if is_prime(int(s)):s = s[1:]
		else:return False
	return True
def getR(n):
	s = str(n)[:-1]
	while len(s) != 0:
		if is_prime(int(s)):s = s[:-1]
		else:return False
	return True
#st = time.time()
i = 11
end = input()
s = 0
while i< end:
	if is_prime(i) and getL(i) and getR(i):
		#print i
		s+= i
	i += 1
print s
#print time.time()-st