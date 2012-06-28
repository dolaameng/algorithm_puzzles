"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

## backenvlope 2x10**6 for O(n2)

from simple_profile import timed_call

def prime_sieve(hi):
    primes = [True for _ in range(hi)]
    primes[0] = primes[1] = False
    current = 2
    s = 0
    while current < hi:
        s += current
        i = 2
        while current * i < hi:
            primes[current * i] = False
            i += 1
        current += 1
        while current < hi and not primes[current]:
            current += 1
    return sum(p for p in range(hi) if primes[p])
    

## tests
if __name__ == '__main__':
    N = 2000000
    # test prime_sieve
    print timed_call(prime_sieve, N)  ## 2.08