"""
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of 
the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares 
of the first one hundred natural numbers and the square of the sum.
"""

from itertools import combinations
from simple_profile import timed_call

N = 100

## solution 1
def solution1():
    return sum([
        2 * n1 * n2
        for (n1, n2) in combinations(range(1, N+1), 2)
        ])

## solution 2
def solution2():
    ns = xrange(1, N+1)
    s = sum(ns)
    return s * s - sum(n * n for n in ns)

print timed_call(solution1)
print timed_call(solution2)
