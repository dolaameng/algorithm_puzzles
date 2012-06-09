## Generate all partitions of a given positive integer n
## i.e., all the representations of n as a sum of positive integers.
## Dont take the order of the summands into account.
## e.g., n = 4, output 1+1+1+1, 2+1+1, 2+2, 3+1, 4
## e.g., n = 5, output 1+1+1+1+1, 2+1+1+1, 2+2+1, 3+1+1, 3+2,
## 4+1, 5
## Algorithm: Find the rightmost element i that s[i] < s[i-1] and 
## elements after i is not empty
## LOOP INVARIANT: assume the summands are in descending order
## and partitions are generated in lexicographic order
def partitions(n):
    def next(seq):
        L = len(seq)
        ## start from L-2 element, must have at least one element in suffix
        for i in range(L-2, -1, -1):
            if seq[i-1] and seq[i-1] > seq[i]: break
        remainder = n - sum(seq[:i+1]) - 1
        return seq[:i] + [seq[i]+1] + [1 for _ in range(remainder)]
    start, end = [1 for _ in range(n)], [n]
    seq = start
    while True:
        yield seq
        if seq >= end: break
        seq = next(seq)

## Generate partitions of n in reversed alphabetic order
## each partition still has descreding order
## e.g., n = 4, output 4, 3+1, 2+2, 2+1+1, 1+1+1+1
## n = 5, output 5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1
def reverse_partitions(n):
    def next(seq):
        L = len(seq)
        for i in range(L-1, -1, -1):
            if seq[i] > 1: break
        suffix = n - sum(seq[:i])
        q, r = suffix / (seq[i] - 1), suffix % (seq[i] - 1)
        tail = [] if r == 0 else [r]
        return seq[:i] + [seq[i]-1 for _ in range(q)] + tail
    start, end = [n], [1 for _ in range(n)]
    seq = start
    while True:
        yield seq
        if seq <= end: break
        seq = next(seq)
        
## test
if __name__ == '__main__':
    ## test partitions
    assert list(partitions(4)) == [[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1], [4]]
    assert list(partitions(5)) == [
        [1, 1, 1, 1, 1], 
        [2, 1, 1, 1], [2, 2, 1], 
        [3, 1, 1], [3, 2], 
        [4, 1], 
        [5]]
    ## test reverse partitions
    assert list(reverse_partitions(4)) == list(partitions(4))[::-1]
    assert list(reverse_partitions(5)) == list(partitions(5))[::-1]
    print 'all tests passed'