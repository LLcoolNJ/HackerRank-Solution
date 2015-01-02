#!/usr/bin/python
# -*- coding: utf-8 -*-
 
def getPrimesBelowN(n=1000000):
    """Get all primes below n with the sieve of Eratosthenes. 
    @return: a list 0..n with boolean values that indicate if 
             i in 0..n is a prime.
    """
    from math import ceil
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []
    roundUp = lambda n, prime: int(ceil(float(n) / prime))
    for currentPrime in xrange(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in xrange(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primes
 
def isCircularPrime(primes, number):
    """Check if number is a circular prime.
     
    Keyword arguments:
    primes -- a list from 0..n with boolean values that indicate if 
              i in 0..n is a prime
    number -- the integer you want to check
    """
    number = str(number)
    for i in xrange(0, len(number)):
        rotatedNumber = number[i:len(number)] + number[0:i]
        if not primes[int(rotatedNumber)]:
            return False
    return True
 
if __name__ == "__main__":
    primes = getPrimesBelowN(input())
    sm =7
    numberOfPrimes = 2
    '''print(2)    # I print them now, because I want to skip all primes
    print(5)    # that contain one of those digits: 0,2,4,5,6,8'''
    for prime, isPrime in enumerate(primes):
        if (not isPrime) or ("2" in str(prime)) or \
           ("4" in str(prime)) or ("6" in str(prime)) or \
           ("8" in str(prime)) or ("0" in str(prime)) or \
           ("5" in str(prime)):
            continue
        if isCircularPrime(primes, prime):
            #print(prime)
            #numberOfPrimes += 1
			sm += prime
 
    print sm