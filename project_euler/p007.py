"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

## Ancient algorithm: sieve of Eratosthenes

## Sieve of Atkin: optimized version of sieve of Eratosthenes
## Algorithm Description:
## All remainders are modulo-60 remainders
## All numbers are positive integers
## Flipping an entry in the sieve list means to change the marking (prime or non-prime)
## to the opposite marking
## wiki page http://en.wikipedia.org/wiki/Sieve_of_Atkin

from simple_profile import timed_call

## the performance depends on how sparse the primes
## are within the range

def prime_generator():
    primes = [2]
    def is_prime(n):
        for p in primes:
            if p * p > n:
                return True
            if n % p == 0:
                return False
    while True:
        yield primes[-1]
        n = primes[-1] + 1
        while not is_prime(n):
            n += 1
        primes.append(n)
     
     
def solution1():
    N = 10001
    primes = prime_generator()
    for i in range(1, N):
        next(primes)
    return next(primes)
       
## tests
if __name__ == '__main__':
    print timed_call(solution1) # 0.18 s