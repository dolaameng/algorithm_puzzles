## Catalan sequences and Catalan numbers
## generate all sequences of length 2n, composed of 1s and -1s,
## satisfying the following conditions a) the sum of all terms is 0
## b) the sum of any prefix is nonnegative.
## the number of such sequences is called Catalan number.
## n = 2: +-+-, ++--,
## n = 3: +-+-+-, +-++--, ++--+-, ++-+--, +++---,

#################################################################################
## Inspiration: suppose the first seq is the zig-zag +-+-+-.... and
## the last seq is +++...---...
## But how do we generate the next sequence? It should concide with the current
## seq up to some point where they differ and - is replaced by + (BIG TREAND). This place 
## should be as close to the end as possible (ORDER SPECIFICATION).
## But there is a restriction (CONSTRAINT SPECIFICATION): 
## - may be replaced by + only if there is + on the right of it.

## After we replace - with +, we are faced with the following problem (RECURSION): 
## a prefix of the sequence is fixed, find the minimal sequence with the prefix.
## The solution: extend the given prefix step by step; at each step append - 
## if possible (whereas the sum must be nonnegative); otherwise, append +.
## +-+-+-, +-++--, ++--+-, ++-+--, +++---
## This mental algorithm applies to almost all combinatorial generation problems
#################################################################################
def catalan_sequences(n):
    def next(seq):
        N = len(seq)
        replacable = False
        for i in range(N-1, -1, -1):
            if seq[i] == 1: replacable = True
            if replacable and seq[i] == -1: break
        prefix = seq[:i] + [1]
        PRE_PLUS, PRE_MINUS = prefix.count(1), prefix.count(-1)
        SUF_PLUS, SUF_MINUS = N/2 - PRE_PLUS, N/2 - PRE_MINUS
        suffix = [-1 for _ in range(PRE_PLUS-PRE_MINUS)] + sum([[1, -1] for _ in range(SUF_PLUS)], [])
        return prefix + suffix
    start = sum([[1, -1] for _ in range(n)], [])
    end = [1 for _ in range(n)] + [-1 for _ in range(n)]
    seq = start
    while True:
        yield seq
        if seq >= end: break
        seq = next(seq)
    
## find all possible ways to compute the product of n factors. The order
## of the factors remains unchanged. Each multiplication should be indicated
## by parentheses. e.g., for n = 4, generate the following 5 expressions:
## ((ab)c)d, (a(bc))d, (ab)(cd), a((bc)d), a(b(cd))
## see the wiki page for catalan number
def all_products(n):
    raise RuntimeError('not implemented')

## test    
if __name__ == '__main__':
    ## test catalan_sequences
    assert list(catalan_sequences(2)) == [[1, -1, 1, -1], [1, 1, -1, -1]]
    assert list(catalan_sequences(3)) == [
        [1, -1, 1, -1, 1, -1], 
        [1, -1, 1, 1, -1, -1], 
        [1, 1, -1, -1, 1, -1], 
        [1, 1, -1, 1, -1, -1], 
        [1, 1, 1, -1, -1, -1]]
    print 'all tests pass'