## Dynamic Programming  (Recursive Nature + Memoization Structure + Iterative Framework) 
## can be applied to several different scenarios. e.g., 
## (1) development of optimal partial solutions to get optimal complete solution
## (2) a memoization (plus caluclate and store values in table in reversed way), as
## an alternative to recursions.

## Dynamic Programming typically for optimization problems, where
## there are many feasible solutions, and we need to find the optimal one.
## The key assumption is the Principle of Optimality: Solution composed of
## optimal supproblem solutions.
## It is useful if the problem can be breaken into subproblems and there are
## overlapping in those subproblems

import itertools, cProfile, time, math, collections

def timedcall(fn, *args):
    start = time.clock()
    result = fn(*args)
    end = time.clock()
    return (end-start, result)

############################# Computation of Binomial Coefficients#########
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
    
#################################### Computation of Combination Number#########
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

################################Triangulation of Convext polygon #######
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
## 1. Use Dynamic Programming
## AHA: Assume the vertices of polygon is given in the clockwise in (1..n)
## the solution cost(1..n) is the optimal solution for poly(1..n)
## For cost(i..j), its optimal cost satisfies Principle of Optimality:
## Base Case: cost(i, i+1) = 0, cost(i, i+2) = 0 for degenerate cases
## Recursion: for any middle point m in between i, j
## cost(i, j) = min{ cost(i, m) + cost(m, j) + edge(i, m) + edge(j, m) } for each m
## After finding the recursion relation, dynamic programming is about building
## the table from bottom up
def iterative_triangulation(vertices):
    N = len(vertices) # 0 to N-1
    costs = {}
    pathes = {}
    ## The order of filling out tables is
    ## the key to dynamic programming
    ############### ASK THE QUESTION: AFTER YOU GOT VALUE(I, J) ################
    ############### WHAT VALUE CAN YOU IMMEDIATELY GET? ########################
    ### THAT IS, WHAT IS THE BOTTOM PART (BASE CONDTIONS) FOR THE IERATION #####
    ### IN THIS CASE, THE ORDER IS NOT LINEAR, BUT WITH BIGGER OVERLAPPING EACH
    ### TIME, E.G., FOR 1, 2, 3, 4, 5. THE CALCULATION ORDER SHOULD BE
    ### -> (1, 2), (2, 3), (3, 4), (4, 5)
    ### -> (1, 2, 3), (2, 3, 4), (3, 4, 5)
    ### -> (1, 2, 3, 4), (2, 3, 4, 5)
    ### -> (1, 2, 3, 4, 5)
    ### PYRAMID STRUCTURE
    ############################################################################
    for step in range(2, N+1):
        for i in range(N-step+1):
            start, end = i, i+step-1
            if (end-start) <= 2:
                costs[(start, end)] = 0
            else:
                d, v = min([
                    (costs[(start, m)] 
                    + costs[(m, end)] 
                    + (0 if m==start+1 else dist(vertices[start], vertices[m])) 
                    + (0 if end==m+1 else dist(vertices[m], vertices[end])), m)
                    for m in range(start+1, end)
                ])
                costs[(start, end)] = d
                pathes[(start, end)] = v
    
    def find_edges(start, end):
        if (end-start) <= 2:
            return []
        else:
            m = pathes[(start, end)] 
            edges = set(find_edges(start, m)) | set(find_edges(m, end))
            if m-start >= 2: edges |= set([(start, m)])
            if end-m >= 2: edges |= set([(m, end)])
            return edges
    edges = find_edges(0, N-1)
    return costs[(0, N-1)], edges
    
## 2. Use memoization to avoid explicitly build the table
## the main difference between memoization and dynamic programming
## is the limit of recursion depth
def memo_triangulation(vertices):
    N = len(vertices)
    def memo(start, end):
        assert start < end, 'start index %d should be before end index %d' % (start, end)
        if (start, end) not in memo.cache:
            if (end - start) <= 2:
                memo.cache[(start, end)] = 0
            else:
                d, v = min([
                    (memo(start, m) 
                    + memo(m, end) 
                    + (0 if m==start+1 else dist(vertices[start], vertices[m])) 
                    + (0 if end==m+1 else dist(vertices[m], vertices[end])), m)
                    for m in range(start+1, end)
                ])
                memo.cache[(start, end)] = d
                memo.path[(start, end)] = v
        return memo.cache[(start, end)]
    def find_edges(start, end):
        if (end-start) <= 2:
            return []
        else:
            m = memo.path[(start, end)] 
            edges = set(find_edges(start, m)) | set(find_edges(m, end))
            if m-start >= 2: edges |= set([(start, m)])
            if end-m >= 2: edges |= set([(m, end)])
            return edges
    memo.cache = {}
    memo.path = {}
    cost = memo(0, N-1)
    edges = find_edges(0, N-1)
    return cost, edges

##########################################Matrix chain multiplication##########
## e.g., matrices of size 2x3, 3x4 and 4x5 can be multiplied in two different ways.
## The cost is wither 2x3x4 + 2x4x5 = 64 or 3x4x5 + 2x3x5 = 90
## for a list of matrices, find the minimal cost for the chain multiplication
## use dynamic programming
## AHA: almost the same structure with the convex polygon problem - pyramid structure
def iterative_matrix_chain(matrices):
    N = len(matrices)
    cache = {}
    path = {}
    for step in range(1, N+1):
        for i in range(N-step+1):
            start, end = i, i+step-1
            mstart, mend = matrices[start], matrices[end]
            if (end-start) == 0: 
                cache[(start, end)] = 0
            elif (end-start) == 1:
                assert mstart[1] == mend[0]
                cache[(start, end)] = mstart[0] * mstart[1] * mend[1]
            else:
                d, v = min([
                    (cache[(start, m)] 
                    + cache[(m+1, end)] 
                    + mstart[0]*matrices[m][1]*mend[1], m)
                    for m in range(start, end)
                ])
                cache[(start, end)] = d
                path[(start, end)] = v
    def expression(start, end):
        if start == end:
            return "%d" % (start,)
        elif start + 1 == end:
            return "(%d*%d)" % (start, end)
        else:
            m = path[(start, end)]
            return "(%s*%s)" % (expression(start, m), expression(m+1, end))
    cost, exp = cache[(0, N-1)], expression(0, N-1)
    return cost, exp

############################# Railway ticket problem #############
## A one-way railway has n stops, we know the price of the tickets
## form ith stop to jth stop (i < j). Find the minimal travel cost
## from stop 1 to stop n, assume possible savings due to intermediate
## stops

############################ Binary operation problem ############
## A finite set and a binary operation defined on the set. We have
## n elements a1, ..., an from the set and one more element x. 
## Check if it is possible to insert parentheses in the expressions
## a1 op a2 ... op an in such a way that the result is equal to x.
## The number of operations should not exceed O(n**3)
## AHA: Grouping by parentheses has a natural correspondence with
## the pyramid structure in dynamic programming
## HOWEVER, a key difference here from above problems is that 
## this problem is a search problem, instead of optimizatoin problem.
## so all possible values need to be tracked
############# HERE THE PARTIAL SOLUTIONS HAVE A PYRAMID STRUCTURE, 
############# INSTEAD OF A LINEAR STRUCTURE
def expression(nums, op, target):
    N = len(nums)
    values = {}
    pathes = {}
    for step in range(1, N+1):
        for i in range(0, N-step+1):
            start, end = i, i+step-1
            if start == end:
                values[(start, end)] = [nums[start]]
            elif start + 1 == end:
                values[(start, end)] = [op(nums[start], nums[end])]
            else:
                result = [
                    (op(v1, v2), m)
                    for m in range(start, end)
                    for v1 in values[(start, m)]
                    for v2 in values[(m+1, end)]
                ]
                values[(start, end)] = map(lambda r: r[0], result)
                pathes[(start, end)] = dict(result)
    def find_expression(start, end):
        ## TODO
        pass
    print; print values; print
    print pathes
    exp = find_expression(0, N-1) if target in values[(start, end)] else None
    return exp

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
    
    ####################################################
    ## the complexity of memoziation and iterative
    ## are almost the same, which are both much better
    ## than recursive version
    ## But the advantage of iteration is that it is 
    ## limited by the recursion depth
    ####################################################
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
    assert timedcall(memo_combination, 30, 15)[0] < 0.01 ## 0.0004 s
    print 'hit rate for memo_combination: ', \
        float(memo_combination.hits) / memo_combination.calls # 0.43
    ## test iterative combination number
    assert iterative_combination(2, 2) == 1
    assert iterative_combination(10, 1) == 10
    assert iterative_combination(6, 3) == 20
    assert timedcall(iterative_combination, 30, 15)[0] < 0.01 ## 0.0005s
    assert timedcall(iterative_combination, 100, 50)[0] < 0.01 ## 0.004s
    
    ## test memo_triangulation
    polygon1 = [(0, 0), (1, 1), (2, 1.5), (3, 0), (1.5, -1)]
    all_dists = sorted([(dist(p1, p2), (i1, i2))
                    for i1, p1 in enumerate(polygon1)
                    for i2, p2 in enumerate(polygon1[i1+2:], i1+2)
                    if (i2-i1) not in (1, len(polygon1)-1)])
    #print all_dists
    cost, edges = memo_triangulation(polygon1)
    assert cost == all_dists[0][0] + all_dists[1][0]
    assert edges == set([all_dists[0][1], all_dists[1][1]])
    ## counter-example by Lloyd where greedy selection of shortest path
    ## does not give an optimal answer
    ## after pick node1-node3, it is forced to pick node1-node4, because
    ## the second shortest node0-node2 intersects with node1-node3
    ## The OPTIMAL solution is are dissects [(0, 2), (2, 4)], which gives 170
    polygon2 = [(0, 0), (50, 25), (80, 30), (125 ,25), (160, 0)] 
    all_dists = sorted([(dist(p1, p2), (i1, i2))
                    for i1, p1 in enumerate(polygon2)
                    for i2, p2 in enumerate(polygon2[i1+2:], i1+2)
                    if (i2-i1) not in (1, len(polygon2)-1)])
    #print all_dists
    cost, edges = memo_triangulation(polygon2)
    assert abs(cost - 170.880074906) < 1e-5
    assert edges == set([(0, 2), (2, 4)])
    
    ## test iterative_triangulation
    polygon1 = [(0, 0), (1, 1), (2, 1.5), (3, 0), (1.5, -1)]
    all_dists = sorted([(dist(p1, p2), (i1, i2))
                    for i1, p1 in enumerate(polygon1)
                    for i2, p2 in enumerate(polygon1[i1+2:], i1+2)
                    if (i2-i1) not in (1, len(polygon1)-1)])
    cost,edges = iterative_triangulation(polygon1)
    assert cost == all_dists[0][0] + all_dists[1][0]
    assert edges == set([all_dists[0][1], all_dists[1][1]])
    polygon2 = [(0, 0), (50, 25), (80, 30), (125 ,25), (160, 0)] 
    all_dists = sorted([(dist(p1, p2), (i1, i2))
                    for i1, p1 in enumerate(polygon2)
                    for i2, p2 in enumerate(polygon2[i1+2:], i1+2)
                    if (i2-i1) not in (1, len(polygon2)-1)])
    cost, edges = iterative_triangulation(polygon2)
    assert abs(cost - 170.880074906) < 1e-5
    assert edges == set([(0, 2), (2, 4)])
    
    ## test iterative_matrix_chain
    matrices = (m0, m1, m2) = [(2, 3), (3, 4), (4, 5)]
    cost, exp = iterative_matrix_chain(matrices)
    assert cost == 64
    assert exp == '((0*1)*2)'
    matrices = (m0, m1, m2, m3, m4, m5) = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
    cost, exp = iterative_matrix_chain(matrices)
    assert cost == 15125
    assert exp == '((0*(1*2))*((3*4)*5))'
    
    ## test binary operation problem
    print expression([1, 2, 3, 4], lambda x, y: x-y, -1)
    
    print 'all tests pass'