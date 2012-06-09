## pring all the sequences of length k composed of the numbers 1 .. n
## sequences (different from permutations) -- elements in seq are independent of each other
## in lexicographic sequence (see next_seq for details)
def sequences(k, values):
    ## find the rightmost one < end, increase by 1, reset the subsequent to start
    def next_seq(s):
        pivot = len(s) - 1 - next(i for i, e in enumerate(s[::-1]) if values.index(e)!= len(values)-1)
        return s[:pivot] + [values[values.index(s[pivot])+1]] + [values[0] for _ in range(len(s)-pivot-1)]
    seq = [values[0] for _ in range(k)]
    last = [values[-1] for _ in range(k)]
    while seq <= last:
        yield seq
        seq = next_seq(seq)
        
## find all subsets of the set a
## solve subsets problems as generating all sequences of k, {False True}
def subsets(s):
    k = len(s)
    s = tuple(s)
    return map(
        lambda seq: set(s[i] for i, v in enumerate(seq) if v),
        sequences(k, [False, True])
    )

## find all sequences of length k of positive integers such that the i-th
## term does not exceed i for all i
def ith_sequences(k):
    return [seq
        for seq in sequences(k, range(1, k+1))
        if all(map(lambda (i, e): e <= i+1, enumerate(seq)))
    ]

## tests    
if __name__ == '__main__':
    ## test all sequences
    assert list(sequences(3, range(1, 3+1))) == [
        [1, 1, 1], [1, 1, 2], [1, 1, 3], 
        [1, 2, 1], [1, 2, 2], [1, 2, 3], 
        [1, 3, 1], [1, 3, 2], [1, 3, 3], 
        [2, 1, 1], [2, 1, 2], [2, 1, 3], 
        [2, 2, 1], [2, 2, 2], [2, 2, 3], 
        [2, 3, 1], [2, 3, 2], [2, 3, 3], 
        [3, 1, 1], [3, 1, 2], [3, 1, 3], 
        [3, 2, 1], [3, 2, 2], [3, 2, 3], 
        [3, 3, 1], [3, 3, 2], [3, 3, 3]]
    assert list(sequences(3, [False, True])) == [
        [False, False, False], [False, False, True], [False, True, False], 
        [False, True, True], [True, False, False], [True, False, True], 
        [True, True, False], [True, True, True]]
    ## test all subsets
    assert subsets(set()) == [set([])]
    assert subsets(set([1])) == [set([]), set([1])]
    assert subsets(set([1, 2, 3])) == [set([]), set([3]), set([2]), 
                set([2, 3]), set([1]), set([1, 3]), 
                set([1, 2]), set([1, 2, 3])]
                
    ## test ith_sequences
    assert ith_sequences(1) == [[1]]
    assert ith_sequences(2) == [[1, 1], [1, 2]]
    assert ith_sequences(3) == [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3]]
    print 'all tests passed'
    