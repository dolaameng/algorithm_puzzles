"""
2520 is the smallest number that can be divided 
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
"""
from simple_profile import timed_call

def sieve(N):
    isprime = [True for _ in range(N+1)]
    isprime[0] = isprime[1] = False
    current = 2
    while current < N:
        i = 2
        while current * i <= N:
            isprime[current * i] = False
            i += 1
        current += 1
        while not isprime[current] and current < N: current += 1
    print [n for n in range(N+1) if isprime[n]] 

## use the fact that nums starts from 1
def factor_union(N):
    factors = []
    nums = range(2, N+1)
    while nums:
        factor = min(nums)
        factors.append(factor)
        nums = filter(lambda x: x > 1, 
                    map(lambda x: x/factor if x%factor == 0 else x,
                    nums))
    return factors
    
def solution1(N):
    return reduce(lambda x, y: x*y, factor_union(N), 1)
    
    
def solution2(N):
    def gcd(a, b): return b and gcd(b, a % b) or a
    def lcm(a, b): return a * b / gcd(a, b)
    n = 1
    for i in range(1, N+1):
        n = lcm(n, i)
    return n
    
if __name__ == '__main__':
    ## test sieve for primes
    ## print sieve(20)
    t1, r1 = timed_call(solution1, 20)
    t2, r2 = timed_call(solution2, 20)
    print t1 < t2
    