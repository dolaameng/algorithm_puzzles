## This is an assemble of problems that are specially suitable to
## be solved by recursion. The problem set here has overlapping 
## with those shown in other packages. 
## Inutitively, recursion is very suitable for divide-and-conquer
## and reduction-and-conquer problems.
## TO WRITE CORRECT RECURSION CODE, JUST MAKE SURE THAT
## (1) there is a base case
## (2) in the recursion part, there is a progress (usually reduction) towards
## termination.
## Some recursion may involve twisted (mutual) recursion -- especially for 
## game strategy development.

import math, time, string
########################################################################
## PROFILING TOOLS
def timedcall(fn, *args):
    t1 = time.clock()
    result = fn(*args)
    t2 = time.clock()
    return (t2-t1, result)
########################################################################

## Factorial - O(n)
def factorial(n):
    ## base condition
    if n == 1: 
        return 1
    else:
        return n * factorial(n-1)

## Integral power of real values - O(logn)
def power(base, p):
    if p == 1:
        return base
    elif p % 2 == 0:
        half = power(base, p/2)
        return half * half
    else:
        half = power(base, p/2)
        return half * half * base
        
## Hanoi Tower Problem - Recursive Version
## n - number of sticks, tower will be A (initial), B, C (target)
## output a list of movements. 
## e.g., for n = 2, output: ['A->B', 'A->C', 'B->C']
## Complexity nlogn
def hanoi(n, source, middle, target):
    if n == 1:
        return ['%s->%s' % (source, target)]
    else:
        return (hanoi(n-1, source, target, middle) 
                + ['%s->%s' % (source, target)]
                + hanoi(n-1, middle, source, target))

## it seems that it is the memory that brings the method down
STM_Table = string.maketrans('SMT', 'STM')
MST_Table = string.maketrans('SMT', 'MST') 
def memo_hanoi(n, source, middle, target):
    cache = [None, ['%(S)s->%(T)s']]
    for i in range(2, n+1):
        cache.append( map(lambda s: s.translate(STM_Table), cache[i-1])
                    + ['%(S)s->%(T)s']
                    + map(lambda s: s.translate(MST_Table), cache[i-1]) ) 
    return [
        s % {'S': source, 'M': middle, 'T': target}
        for s in cache[n]
    ] 
"""          
def memo_hanoi(n, source, middle, target):
    if n not in memo_hanoi.cache:
        if n == 1:
            memo_hanoi.cache[1] = ['%(S)s->%(T)s']
        else:
            ## prepare memo_hanoi.cache[n-1]
            memo_hanoi(n-1, source, target, middle)
            ## by now memo_hanoi.cache[n-1] should be ready
            memo_hanoi.cache[n] = ( map(lambda s: s.translate(STM_Table), memo_hanoi.cache[n-1])
                + ['%(S)s->%(T)s']
                + map(lambda s: s.translate(MST_Table), memo_hanoi.cache[n-1]) )
    template = memo_hanoi.cache[n]
    return [
        s % {'S': source, 'M': middle, 'T': target}
        for s in template
    ]
memo_hanoi.cache = {}
"""

## Tests
if __name__ == '__main__':
    ## test factorial
    ## ESTIMATE the limit of recursion depth in python
    try:
        n = 1
        while True:
            factorial(n)
            n += 1
    except RuntimeError:
        print 'recusion depth limit: ', n # n = 1000 on macbook pro
    
    ## test power
    assert power(2.0, 10) == 1024 
    ## test hanoi tower
    assert hanoi(2, 'A', 'B', 'C') == ['A->B', 'A->C', 'B->C']
    assert memo_hanoi(2, 'A', 'B', 'C') == ['A->B', 'A->C', 'B->C']
    assert hanoi(3, 'A', 'B', 'C') == ['A->C', 'A->B', 'C->B', 'A->C', 'B->A', 'B->C', 'A->C']
    assert memo_hanoi(3, 'A', 'B', 'C') == ['A->C', 'A->B', 'C->B', 'A->C', 'B->A', 'B->C', 'A->C']
    ## profiling normal hanoi and memoized version
    ## naive optimization doesnt actually help
    n = 22
    dt, r1 = timedcall(hanoi, n, 'A', 'B', 'C')
    print 'normal hanoi n = %d, time = %fs' % (n, dt) ## 56.778993s
    dt, r2 = timedcall(memo_hanoi, n, 'A', 'B', 'C')
    print 'normal memoized hanoi n = %d, time = %fs' % (n, dt)
    assert r1 == r2
    
    print 'all tests pass'