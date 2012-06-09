## generate permutations of a sequence
## permutations are generated without replacement

## use recursive
def recursive_permutations(seq):
    if len(seq) == 1: return [seq]
    return [
        [seq[i]] + p
        for i in range(len(seq))
        for p in recursive_permutations(seq[:i]+seq[i+1:])
    ]
    
## inspired by the start, end, specific-order loop framework
## the specific-order is lexigraphic order (the same prefix, suffix is increasing)
## inspiration:
## (1) How do we find the next permutation in the lexicographic order? 
## (2) When is it possible to increase k-th term in a permutation without
## changing all preceding terms?
## (3) Answer is: when the term is smaller than one of the subsequent terms
## i.e., find k (rightmost) that has candidate to swap with k in sebsequences (larger s[k])
## swap s[k] and min(s[k+1:] if s > s[k])
## LOOP INVARIANT: next element is always bigger than lexigraphic order
def permutations(seq):
    def next(perm):
        N = len(perm)
        maxtoi = [perm[-1] for _ in range(N)]
        for i in range(N-2, -1, -1):
            if perm[i] < maxtoi[i+1]:
                break
            maxtoi[i] = max(perm[i], maxtoi[i+1])
        _, j = min((e,ii) for ii, e in enumerate(perm[i+1:], i+1) if e > perm[i])
        # sort is like reset
        return perm[:i] + [perm[j]] + sorted(perm[i+1:j] + [perm[i]] + perm[j+1:])
    
    seq = sorted(seq)
    start = seq
    end = seq[::-1]
    perm = start
    while perm < end:
        yield perm
        perm = next(perm)
    yield end

## test
if __name__ == '__main__':
    ## test recursive_permutations
    assert recursive_permutations(['a', 'b', 'c']) == [
            ['a', 'b', 'c'], ['a', 'c', 'b'], 
            ['b', 'a', 'c'], ['b', 'c', 'a'], 
            ['c', 'a', 'b'], ['c', 'b', 'a']]
    ## test permutations
    assert list(permutations(['a', 'b', 'c'])) == [
            ['a', 'b', 'c'], ['a', 'c', 'b'], 
            ['b', 'a', 'c'], ['b', 'c', 'a'], 
            ['c', 'a', 'b'], ['c', 'b', 'a']]
    assert list(permutations([1])) == [[1]]
    assert list(permutations([])) == [[]]
    print 'all tests passed'