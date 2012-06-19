## Dynamic Programming can be applied to several different scenarios. e.g., 
## (1) development of optimal partial solutions to get optimal complete solution
## (2) a memoization (plus caluclate and store values in table in reversed way), as
## an alternative to recursions.

import itertools, cProfile, time, math

def timedcall(fn, *args):
    start = time.clock()
    result = fn(*args)
    end = time.clock()
    return (end-start, result)

############################# Computation of Binomial Coefficients
## e.g. n = 0, coeffs = (1, )
## n = 1, coeffs = (1, 1)
## n = 2, coeffs = (1, 2, 1)
## 1. Recursive Version -- a tail recursion
def recursive_binomials(n):
    if n == 0:
        return [1]
    else:
        augmented = [0] + recursive_binomials(n-1) + [0]
        pairs = map(lambda i: augmented[i:i+2], range(len(augmented)-1))
        return map(lambda (a, b): a+b, pairs)
## 2. Iterative Version
def iterative_binomials(n):
    binomials = [[1]]
    for order in range(1, n+1):
        augmented = [0] + recursive_binomials(n-1) + [0]
        binomials.append(map(lambda i: sum(augmented[i:i+2]), range(len(augmented)-1)))
    return binomials[n]
    
#################################### Computation of Combination Number
## e.g., C(n, k) = C(n-1, k-1) + C(n-1, k)
## 1. recursive version
def recursive_combination(n, k):
    if k == 1:
        return n
    elif k == n:
        return 1
    else:
        return recursive_combination(n-1, k-1) + recursive_combination(n-1, k)
## 2. memoization version
## should have improvements because the redundancy of calls
## C(5, 3) would call C(4, 3) and C(4, 2) -> 2XC(3, 2), C(3, 3), C(3, 1)
def memo_combination(n, k):
    memo_combination.calls += 1
    if (n, k) not in memo_combination.cache:
        memo_combination.cache[(n, k)] = (n if k == 1
                else 1 if k == n
                else memo_combination(n-1, k-1) 
                    + memo_combination(n-1, k))
    else:
        memo_combination.hits += 1
        pass
    return memo_combination.cache[(n, k)]

## 3. iterative version
## What does the table of C(n, k) ?
## it looks exactly like the Pascal triangle for
## binomial coefficients
def iterative_combination(n, k):
    table = [[1], [1, 1]]
    for n_ in range(n+1):
        table.append([])
        for k_ in range(n_+1):
            table[n_].append(0)
            table[n_][k_] = (1 if k_ == n_ or k_ == 0
                else n_ if k == 1
                else table[n_-1][k_] + table[n_-1][k_-1])
    return table[n][k]

################################Triangulation of Convext polygon
## A convex polygon with n vertices is given (by a list of coordinates
## of its vertices). It is cut into triangles by non-intersecting 
## diagonals. To do this, we need exactly n-3 diagonals (proof by 
## by induction over n). The cost of the triangulation is defined
## as the total length of all the diagonals used. Find the minimal
## cost of the triangulation. The number of operations should be limited
## by a plonomial of n. Brute force will take C(n**2, n-3) complexity
def dist(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
## Use Dynamic Programming
def triangulation(vertices):
    pass

## tests
if __name__ == '__main__':
    ## test recursive binomial coefficients
    assert recursive_binomials(0) == [1]
    assert recursive_binomials(1) == [1, 1]
    assert recursive_binomials(5) == [1, 5, 10, 10, 5, 1]
    ## test iterative binomial coefficients
    assert iterative_binomials(0) == [1]
    assert iterative_binomials(1) == [1, 1]
    assert iterative_binomials(5) == [1, 5, 10, 10, 5, 1]
    
    ############################################
    ## the complexity of memoziation and iterative
    ## are almost the same, which are both much better
    ## than recursive version
    ############################################
    ## test recursive combination number
    assert recursive_combination(2, 2) == 1
    assert recursive_combination(10, 1) == 10
    assert recursive_combination(6, 3) == 20
    #print timedcall(recursive_combination, 30, 15)[0], 's' ## 65.05 s
    ## test memoization combination number
    #assert memo_combination(2, 2) == 1
    #assert memo_combination(10, 1) == 10
    #assert memo_combination(6, 3) == 20
    memo_combination.cache = {}
    memo_combination.calls = 0
    memo_combination.hits = 0
    print timedcall(memo_combination, 30, 15)[0], 's' ## 0.0004 s
    print 'hit rate for memo_combination: ', \
        float(memo_combination.hits) / memo_combination.calls # 0.43
    ## test iterative combination number
    assert iterative_combination(2, 2) == 1
    assert iterative_combination(10, 1) == 10
    assert iterative_combination(6, 3) == 20
    print timedcall(iterative_combination, 30, 15)[0], 's' ## 0.0005s
    print timedcall(iterative_combination, 100, 50)[0], 's' ## 0.004s
    
    ## test recursive_triangulation
    polygon1 = [(0, 0), (1, 1), (2, 1.5), (3, 0), (1.5, -1)]
    all_dists = sorted([(dist(p1, p2), p1, p2)
                    for i1, p1 in enumerate(polygon1)
                    for i2, p2 in enumerate(polygon1[i1+2:], i1+2)
                    if (i2-i1) not in (1, len(polygon1)-1)])
    print all_dists
    print triangulation(polygon1)
    
    print 'all tests pass'