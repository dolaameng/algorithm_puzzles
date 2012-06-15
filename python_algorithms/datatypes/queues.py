## Queue: FIFO
## In python, Queue can be simulated by (1) a list using insert(0, item) and pop()
## (2) a list using append() and pop(0) or (3) collections.deque
## It should not be a superise that queue is widely used in graph traversal algorithms

## Factorization
## Print in ascending order the first n positive integers whose
## factorization contains only the factors 2, 3, and 5.
## e.g. n = 10, ints: 2, 3, 4, 5, 6, 8, 9, 10, 12, 15

## Inspirations: It is similiar to a tree-search problem
## in the sense that partial solutions are solutions
## and they are extended to get new solutions. So In general
## the tree-search (backtracking) can be used for the problem.
## HOWEVER, notice the factors (possible extensions) for the 
## partial solution are always fixed. So instead of using 
## one frontier queue, several queues (several frontiers) can be used so that
## the SORTING of the frontier is not necessary
def seive(n, factors):
    factors = sorted(factors)
    L = len(factors)
    queues = [[] for _ in range(L)]
    results = []
    while len(results) < n:
        num = results[-1] if results else 1
        for i in range(L):
            queues[i].append(num*factors[i])
        queue = min(queues, key = lambda q: q[0])
        next_num = queue.pop(0)
        if next_num not in results: results.append(next_num)
    return results[:n]

## Euler Cycle
## Suppose a directed graph satisifies two requirements:
## (1) it is connected, i.e., there is a path from any given 
## vertex to any other
## (2) for any vertex the number of incoming edges is equal
## to the number of outgoing edges. 
## NOTE THESE CONDITIONS ARE SUFFICIENT BUT NOT NECESSARY 
## for Euler PATH (not Euler Cycle)
## SEE TEST CASE FOR g2 BELOW
## Find an EDGE CYCLE that traverses each edge exactly ONCE.
## GRAPH is represented as a dict of node -> [node]
## So it is iterable through all vertices and through all edges
## for a certain starting node
## e.g., for fully connected graph with 3 vertices a, b, c
## a possible path could be a permutation of: (ab, bc, ca, ac, cb, ba)
## e.g., for simple linearly connected graph a->b->c->a
## the cycle will be permutations of (ab, bc, ca)
## e.g., for simple linearly connected graph a->b->c
## there is no euler cycle, but the euler path will be permutations of (ab, bc, ca)
## NO BACKTRACKING NEEDED
def euler_path(graph):
    """Input: graph
    Output: a path of edges or None
    Implementation: Starting poit in Euler Cycle does matter for Euler path
    Using Hierholzer's algorithm: (1) randomly start with an edge, find the closed
    tour (cycle). (2) Find the next unvisited edge, repeat the previous step.
    (3) Merge all the found tours, if not possible, report None
    """
    def find_tour(start, edges):
        path = []
        edge = start
        while edge:
            path.append(edge)
            try:
                edge = next(
                    e for e in edges 
                    if e not in path
                    if e[0] == edge[1])
            except:
                edge = None
        return path
    def merge_path2(patha, pathb):
        (p1, i1), (p2, i2) = next(
            [(patha, ia), (pathb, ib)][::(1 if a2==b1 else -1)]
            for (ia, (a1, a2)) in enumerate(patha)
            for (ib, (b1, b2)) in enumerate(pathb)
            if a2 == b1 or a1 == b2
        )
        return p1[i1+1:]+p1[:i1+1]+p2[i2:]+p2[:i2]
    def merge_pathes(pathes):
        if len(pathes) == 1: 
            return pathes[0]
        merged = pathes[0]
        for path in pathes[1:]:
            merged = merge_path2(merged, path)
        return merged
        
    edges = [(va, vb) for (va, vbs) in graph.items() for vb in vbs]
    unvisited = set(edges)
    pathes = []
    while unvisited:
        start = unvisited.pop()
        path = find_tour(start, unvisited)
        unvisited = unvisited.difference(path)
        pathes.append(path)
    return merge_pathes(pathes)
        
## Binary Substring Problem
## Given integer n, find a binary bit string x of length 2**n with
## the following property: any binary string of length n is a substring
## of the string xxx...
## The complexity of the algorithm should be O(C**n)
## INSPIRATION: Consider a graph whose vertices are binary strings of length n-1.
## An edge leaving x and entering y exists if and only if there is a string z of 
## length n such that x is a prefix of z and y is a suffix of z, in other words,
## x and y have n-2 bits in common (x[1:] == y[:-1]). This graph is CONNECTED, 
## and each vertex has two incomming and two outgoing edges (first/last bit is 0/1).
## A cycle that traverses all edges provides a string satisfying the desired property,
## since there are 2**(n-1) vertices and there are 2**(n-1) x 2 = 2**n edges
## (count outgoing edges only to avoid redundancy). 

## Tests    
if __name__ == '__main__':
    ## test seive
    assert seive(10, (2, 3, 5)) == [2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
    assert seive(10, (2, )) == [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    
    ## test euler_cycle
    g1 = {'a': ('b', 'c'), 'b': ('a', 'c'), 'c': ('b', 'a')}
    assert set(euler_path(g1)) == set([('b', 'c'), ('c', 'a'), 
                        ('a', 'b'), ('b', 'a'), 
                        ('a', 'c'), ('c', 'b')])
    ## g2 does not satisfy constraint 1, though there is a Euler PATH
    ## but there is no Euler CYCLE
    g2 = {'c': ('d', ), 'a': ('b',), 'b': ('c', ), 'd': tuple()}
    assert set(euler_path(g2)) == set([('a', 'b'), ('b', 'c'), ('c', 'd')])
    g3 = {'a': ('b',), 'b': ('c', ), 'c': ('a', )}
    assert set(euler_path(g3)) == set([('c', 'a'), ('a', 'b'), ('b', 'c')])
    
    print 'all tests pass'