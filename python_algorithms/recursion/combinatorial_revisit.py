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

## Tests
if __name__ == '__main__':
    ## test sequences
    assert len(sequences((1, 2, 3), 3)) == 27
    assert sequences((1, 2, 3), 2) == [
        (1, 1), (1, 2), (1, 3), 
        (2, 1), (2, 2), (2, 3), 
        (3, 1), (3, 2), (3, 3)]
    
    print 'all tests pass'