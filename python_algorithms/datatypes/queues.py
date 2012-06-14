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
    """
    pass

## Tests    
if __name__ == '__main__':
    ## test seive
    assert seive(10, (2, 3, 5)) == [2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
    assert seive(10, (2, )) == [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    
    ## test euler_cycle
    g1 = {'a': ('b', 'c'), 'b': ('a', 'c'), 'c': ('b', 'a')}
    print euler_path(g1)
    ## g2 does not satisfy constraint 1, though there is a Euler PATH
    ## but there is no Euler CYCLE
    g2 = {'a': ('b',), 'b': ('c', ), 'c': tuple()}
    print euler_path(g2)
    g3 = {'a': ('b',), 'b': ('c', ), 'c': ('a', )}
    print euler_path(g3)
    
    print 'all tests pass'