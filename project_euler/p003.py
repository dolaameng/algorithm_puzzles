"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

## Quadratic Sieve (from wiki http://en.wikipedia.org/wiki/Quadratic_sieve)
## The quadratic sieve algorithm (QS) is an integer factorization algorithm
## and in practice, the second fastest method known (after the General Number
## Field Sieve). It is still the fastest for integers under 100 decimal digits
## or so, and it is considered simpler than the number field sieve

## Another special purpose factorization algorithm is Pollard's rho algorithm

## But there is an easier implementation for finding the last prime factor
## using the concept of prime factor tree

N = 600851475143

## Solution 1        
## prime factor tree method
## based on the prime factor tree
## LOOP INVARIANCE: 
## n has no factors in between 2 to i
## n is always >= i (for i * i <= n), so it is bigger than all other prime factors
## n is a factor of N
## => there is prime factor larger than n
################## Why the algorithm is correct ##############
## Because of the loop invariance
##############################################################
def largest_prime_factor(N):
    i, n = 2, N
    while i * i <= n:
        while n % i == 0 and n > i:
            n = n / i
            #largest_prime_factor.count += 1
        i += 1
    return n
    

## Solution 2
## find factors in O(sqrt(N)) and do the prime test 
## find the max prime factor
        
        
# tests
if __name__ == '__main__':
    ## test the largest prime number
    largest_prime_factor.count = 0
    #assert largest_prime_factor(N) == 6857
    #print largest_prime_factor.count
    from simple_profile import timed_call
    #N = 688543
    print timed_call(largest_prime_factor, N)
    