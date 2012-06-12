## In general it is much easier to count all the objects with some property than
## to generate them explicitly. e.g., the number of combinations of selecting
## k-element subsets of an n-element set (n, k).
## It follows the following recursion calucation
## base condition: (n, 0) = (n, n) = 1
## recursion: (n, k) = (n-1, k-1) + (n-1, k)
## THE KEY TO MANY COUNTING PROBLEMS is to decompose the problem into DISJOINT subproblems
## and use recursion for that.

## Number of Partitions: Let p(n) be the number of representations
## of a nonnegative integer n as a sum of positive integer summands
## (order is insignificant, i.e., 1+2 and 2+1 are counted as the same).
## Assume p(0) = 1 (the only representation has no summands at all).
## Examples: p(1) = 1, p(2) = 1 (1+1), p(3) = 2 (1+2,1+1+1)

## Inspirations: define r(n, k) for n >= 0, k >= 0 as the number of
## representations of n as a sum of positive integers not exceeding k.
## r(0, k) = 1 for all k >= 0 and obviously p(n) = r(n, n).
## All the reprsentations of n are classified according to the maximal
## summand (denoted by i). The number r(n, k) is the sum over all i in {1,...,k}
## of the number of partitions with elements not exceding k and maximal element i.
## The partitons of n into a sum where all terms do not exceed k and maximal term 
## is equal to i are in one-to-one correspondence with the partitions of n-i
## into terms not exceeding i (assuming i <= k). Thus,
## r(n, k) = sum_i_from_1_to_k(r(n-i, i)) for k <= n 
## THIS IS BECAUSE R(N-I, I) CORRESPONDS TO NUMBER OF PARTITIONS OF N, WITH 
## EACH PARTITION SATISFIES THAT THE MAXIMUM ELEMENT IS EXACTLY I
## r(n, k) = r(n, n) for k > n
caches = {}
def recursive_num_partitions(n):
    def r(n, k):
        if n == 0: return 1
        if n < k: return r(n, n)
        if (n, k) not in caches:
            caches[(n, k)] = sum([
                r(n-i, i)
                for i in range(1, k+1)
            ])
        return caches[(n, k)]
    return r(n, n)

## non-recursive version to calcualte num of partitions    
def num_partitions(n):
    """
    solutions by explicitly build the caches
    without use of recursion and memoization
    """
    raise RuntimeError('not implemented')
    
## number of lucky sequences
## a sequence of 2n digits (0..9) is called lucky if the sum
## of the first n digits is equal to the sum of last n digits.
## find the number of all lucky sequences of a given length
## e.g., n = 1: sum = 0..9 -> XX (X=0..9), 9
## n = 2: sum = 0..18
## INSPIRATION: 
def num_lucky_sequences(n):
    raise RuntimeError('not implemented')
    
## catalan number
def num_catalan(n):
    raise RuntimeError('not implemented')
    
## tests
if __name__ == '__main__':
    ## test recursive num of partitions
    ## recursion wont work for n > 1000
    assert recursive_num_partitions(0) == 1
    assert recursive_num_partitions(1) == 1
    assert recursive_num_partitions(2) == 2
    assert recursive_num_partitions(100) == 190569292
    assert recursive_num_partitions(300) == 9253082936723602
    assert recursive_num_partitions(1000) == 24061467864032622473692149727991
    ## test recursive num of partitions
    """
    assert num_partitions(0) == 1
    assert num_partitions(1) == 1
    assert num_partitions(2) == 2
    assert num_partitions(100) == 190569292
    assert num_partitions(300) == 9253082936723602
    assert num_partitions(1000) == 24061467864032622473692149727991
    """
    ## test num_lucky_sequences
    print num_lucky_sequences(1)
    print 'all tests pass'