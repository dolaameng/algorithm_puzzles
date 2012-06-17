## It should not be a suprise that recursion is widely used
## to generate combinatorial objects (see combinatorial package)
## for details. This package includes some exercises of re-solving
## some combinatorial problems using recursion algorithms.
import itertools

## Sequences with Replacement
## Write a program that prints all sequences of length n composed
## of the numbers 1..k, i.e., k**n sequences in total
## e.g., 1, 2, 3, n = 2, generates 11, 12, 13, 21, 22, 23, 31, 32, 33
def sequences(nums, n):
    nums = set(nums)
    if n == 1:
        return [(i, ) for i in nums]
    else:
        return [(i, ) + s
        for i in nums
        for s in sequences(nums, n-1)]

        
## Permutations
## write a program that prints all permutations of 1..k of length n
## e.g., for 1..3, n = 2, generates 12, 13, 21, 23, 31, 32
def all_permutations(nums, n):
    if n == 1:
        return [(i, ) for i in nums]
    else:
        return [
            (i, ) + s
            for i in nums
            for s in all_permutations(set(nums)-set([i]), n-1)
        ]

## Binary strings -- SUBSET PROBLEM
## Print all sequences of length n that contain k ones and n-k zeros
## Each with once
## e.g., n = 3, k = 1 : 100, 010, 001
## e.g., n = 4, k = 2 : 1100, 1010, 1001, 0110, 0101, 0011
## Inspiration: A natural recurrence could be 
## C(n, k) = C(n-1, k-1) + C(n-1, k) 
## where first term corresponds to prefix1 and second prefix0
## But the problem is, the complexity of this recurrence is very high 
def ones_zeros(n1, n0):
    if n1 == 0:
        return [tuple(0 for _ in range(n0))]
    elif n0 == 0:
        return [tuple(1 for _ in range(n1))]
    else:
        prefix1 = [(1,) + s for s in ones_zeros(n1-1, n0)]
        prefix0 = [(0,) + s for s in ones_zeros(n1, n0-1)]
        return prefix1 + prefix0
        
## Partitioning
## Generate all representations of a given positive integer n
## as the sum of a non-increasing sequence of positive integers
## e.g., n = 3, 21, 12, 111
## e.g., n = 4, 31, 22, 211, 13, 121, 112
def partition(n):
    pass


## Tests
if __name__ == '__main__':
    ## test sequences
    assert len(sequences((1, 2, 3), 3)) == 27
    assert sequences((1, 2, 3), 2) == [
        (1, 1), (1, 2), (1, 3), 
        (2, 1), (2, 2), (2, 3), 
        (3, 1), (3, 2), (3, 3)]

    ## test permutations
    assert all_permutations((1, 2, 3), 2) == [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    assert all_permutations((1, 2, 3), 3) == [
        (1, 2, 3), (1, 3, 2), 
        (2, 1, 3), (2, 3, 1), 
        (3, 1, 2), (3, 2, 1)]
    ## test ones_zeros
    assert ones_zeros(1, 2) == [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    assert ones_zeros(2, 2) == [
        (1, 1, 0, 0), (1, 0, 1, 0), 
        (1, 0, 0, 1), (0, 1, 1, 0), 
        (0, 1, 0, 1), (0, 0, 1, 1)]
    ## test partition
    print partition(3)
    print partition(4)

    
    print 'all tests pass'