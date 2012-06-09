## generate subsets of the set s having k elements
## subsets of k elements correspond to n-bits strings with exact k 1s
## A naive way of doing it is to generate all n-bits sequences
## and find those with exact k 1s. It is inefficient.

## s set, find subsets of s having k elements
## generate n-bit binary strings with exact k 1s in lexigraphic order
## LOOP INVARIANT: next element is lexigraphically behind the current
## i.e., the same prefix, larger suffix, e.g., 000111 -> 001011
## 010110 -> 011001
## INSPIRATION: when is it possible to increase the s-th term of a bit
## string with k 1s without changing the preceding terms? If x[s] is 
## changed from 0 to 1, we should replace by 0 somewhere to keep the 
## total number of 1s fixed. Therefore, it is necessary to have 1s on the
## right of x[s]
def subsequences(N, K):
    def next(seq):
        ## find the rightmost 0 with 1s behind
        tail_1s = 0 if seq[-1] == 0 else 1
        for i in range(N-2, -1, -1):
            if seq[i] == 1: tail_1s += 1
            if tail_1s and seq[i] == 0:
                break
        tail_1s -= 1
        tail_0s = len(seq) - i - 1 - tail_1s
        return seq[:i] + [1] + [0 for _ in range(tail_0s)] + [1 for _ in range(tail_1s)]
    start = [0 for _ in range(N-K)] + [1 for _ in range(K)]
    end = [1 for _ in range(K)] + [0 for _ in range(N-K)]
    seq = start
    while True:
        yield seq
        if seq >= end: break
        seq = next(seq)
def subsets(s, K):
    N = len(s)
    s = tuple(s)
    return map(
        lambda bits: set(s[i] for i, e in enumerate(bits) if e == 1),
        subsequences(N, K)
    )


## same algorithms for other similiar problems
## Generate (in lexicographic order) all increasing sequences of length K
## consisting of the numbers 1..N, e.g., for N = 5, K = 2
## output [12, 13, 14, 15, 23, 24, 25, 34, 35, 45]
def ascending_sequences(N, K):
    def next(seq):
        for i in range(K-1, -1, -1):
            if seq[i] < N - (K-1-i): break
        return seq[:i] + range(seq[i]+1, seq[i]+1+K-i)
    start, end = range(1, K+1), range(N-K+1, N+1)
    seq = start
    while True:
        yield seq
        if seq >= end: break
        seq = next(seq)

## Same algorithms for similiar problems
## Generate in lexigraphic order all decreasing sequence of K
## consisting of numbers 1 .. N. E.g. for N = 5, K = 2, output
## [21, 31, 32, 41, 42, 43, 51, 52, 53, 54]
def descending_sequences(N, K):
    def next(seq):
        # find the rightmost element that is still increasable
        for i in range(K-1, -1, -1):
            if seq[i-1] and seq[i-1] - seq[i] > 1: break
        return seq[:i] + [seq[i]+1] + range(1, K-i)[::-1]
    start, end = range(K, 0, -1), range(N, N-K, -1)
    seq = start
    while True:
        yield seq
        if seq >= end: break
        seq = next(seq)
        
## same algorithm for similiar problems
## Generate all injective mappings of the set 1..K into 1..N (k <= n)
## A mapping is injective if no two elements of 1..K are mapped to the same 
## element of 1..N. Generation of each mapping should require no more than O(K) time
## find the subsets of K out of N, find the perumutations of each selection

## find all sub-permutations of length K of seq
## by finding indices 0..N-1, e.g. 012->013
import permutations
def subpermutations(seq, K):
    return sorted(sum([list(permutations.permutations(s)) for s in subsets(seq, K)], []))

def injective_mapping(seta, setb):
    K, N = len(seta), len(setb)
    a, b = tuple(seta), tuple(setb)
    return [dict(zip(a, s)) for s in subpermutations(b, K)]
    

## test
if __name__ == '__main__':
    ## test subsequences
    assert list(subsequences(3, 2)) == [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    ## test subsets
    assert subsets(set(['a', 'b', 'c']), 2) == [set(['c', 'b']), set(['a', 'b']), set(['a', 'c'])]
    assert subsets(set(['a']), 1) == [set(['a'])]
    assert subsets(set(['a', 'b', 'c']), 3) == [set(['a', 'c', 'b'])]
    assert subsets(set(['a', 'b', 'c']), 1) == [set(['b']), set(['c']), set(['a'])]
    ## test ascending_sequences
    assert list(ascending_sequences(5, 2)) == [
        [1, 2], [1, 3], [1, 4], [1, 5], 
        [2, 3], [2, 4], [2, 5], 
        [3, 4], [3, 5], 
        [4, 5]]
    assert list(ascending_sequences(3, 3)) == [[1, 2, 3]]
    ## test descending_sequences
    assert list(descending_sequences(5, 2)) == [
        [2, 1], 
        [3, 1], [3, 2], 
        [4, 1], [4, 2], [4, 3], 
        [5, 1], [5, 2], [5, 3], [5, 4]]
    ## test subpermutations
    import itertools
    answer = lambda seq, K: sorted(sum([[list(p) for p in itertools.permutations(c, K)] for c in itertools.combinations(seq, K)], []))
    assert subpermutations([1, 2, 3], 2) == answer([1, 2, 3], 2)
    assert subpermutations([1, 2, 3, 4], 3) == answer([1, 2, 3, 4], 3)
    assert injective_mapping(set('abc'), set('1234')) == [
            {'a': '1', 'c': '2', 'b': '3'}, 
            {'a': '1', 'c': '2', 'b': '4'}, 
            {'a': '1', 'c': '3', 'b': '2'}, 
            {'a': '1', 'c': '3', 'b': '4'}, 
            {'a': '1', 'c': '4', 'b': '2'}, 
            {'a': '1', 'c': '4', 'b': '3'}, 
            {'a': '2', 'c': '1', 'b': '3'}, 
            {'a': '2', 'c': '1', 'b': '4'}, 
            {'a': '2', 'c': '3', 'b': '1'}, 
            {'a': '2', 'c': '3', 'b': '4'}, 
            {'a': '2', 'c': '4', 'b': '1'}, 
            {'a': '2', 'c': '4', 'b': '3'}, 
            {'a': '3', 'c': '1', 'b': '2'}, 
            {'a': '3', 'c': '1', 'b': '4'}, 
            {'a': '3', 'c': '2', 'b': '1'}, 
            {'a': '3', 'c': '2', 'b': '4'}, 
            {'a': '3', 'c': '4', 'b': '1'}, 
            {'a': '3', 'c': '4', 'b': '2'}, 
            {'a': '4', 'c': '1', 'b': '2'}, 
            {'a': '4', 'c': '1', 'b': '3'}, 
            {'a': '4', 'c': '2', 'b': '1'}, 
            {'a': '4', 'c': '2', 'b': '3'}, 
            {'a': '4', 'c': '3', 'b': '1'}, 
            {'a': '4', 'c': '3', 'b': '2'}]
    print 'all tests passed'