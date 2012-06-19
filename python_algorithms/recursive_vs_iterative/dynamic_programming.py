## Dynamic Programming can be applied to several different scenarios. e.g., 
## (1) development of optimal partial solutions to get optimal complete solution
## (2) a memoization (plus caluclate and store values in table in reversed way), as
## an alternative to recursions.

import itertools, cProfile

## Computation of Binomial Coefficients
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
    
## Computation of Combination Number
## e.g., C(n, k) = C(n-1, k-1) + C(n-1, k)
## 1. recursive version
def recursive_combination(n, k):
    if k == 1:
        return n
    elif k == n:
        return 1
    else:
        return recursive_combination(n-1, k-1) + recursive_combination(n-1, k)
## 2. memoization version -- no improvement at all, because there is
## no redudancy in the recursive call - no hits at all
## It could be even worse because of the cache update
def memo_combination(n, k):
    cache = {}
    if (n, k) not in cache:
        cache[(n, k)] = (n if k == 1
                else 1 if k == n
                else memo_combination(n-1, k-1) 
                    + memo_combination(n-1, k))
    else:
        print 'hit', n, k
    return cache[(n, k)]
## 3. iterative version
def iterative_combination(n, k):
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
    ## test recursive combination number
    assert recursive_combination(2, 2) == 1
    assert recursive_combination(10, 1) == 10
    assert recursive_combination(6, 3) == 20
    # cProfile.run("recursive_combination(30, 15)") ## 61.35 s
    ## test memoization combination number
    assert memo_combination(2, 2) == 1
    assert memo_combination(10, 1) == 10
    assert memo_combination(6, 3) == 20
    # cProfile.run("memo_combination(30, 15)") ## 140.75 s
    ## test iterative combination number
    assert iterative_combination(2, 2) == 1
    assert iterative_combination(10, 1) == 10
    assert iterative_combination(6, 3) == 20
    cProfile.run("iterative_combination(30, 15)") ## ??
    
    print 'all tests pass'