## It should not be a suprise that recursion is widely used
## to generate combinatorial objects (see combinatorial package)
## for details. This package includes some exercises of re-solving
## some combinatorial problems using recursion algorithms.
import itertools

## Sequences with Replacement
## Write a program that prints all sequences of length n composed
## of the numbers 1..k, i.e., k**n sequences in total
## e.g., 1, 2, 3, n = 2, generates 11, 12, 13, 21, 22, 23, 31, 32, 33
def sequences(nums, n):
    nums = set(nums)
    if n == 1:
        return [(i, ) for i in nums]
    else:
        return [(i, ) + s
        for i in nums
        for s in sequences(nums, n-1)]

        
## Permutations
## write a program that prints all permutations of 1..k of length n
## e.g., for 1..3, n = 2, generates 12, 13, 21, 23, 31, 32
def all_permutations(nums, n):
    if n == 1:
        return [(i, ) for i in nums]
    else:
        return [
            (i, ) + s
            for i in nums
            for s in all_permutations(set(nums)-set([i]), n-1)
        ]

## Binary strings -- SUBSET PROBLEM
## Print all sequences of length n that contain k ones and n-k zeros
## Each with once
## e.g., n = 3, k = 1 : 100, 010, 001
## e.g., n = 4, k = 2 : 1100, 1010, 1001, 0110, 0101, 0011
## Inspiration: A natural recurrence could be 
## C(n, k) = C(n-1, k-1) + C(n-1, k) 
## where first term corresponds to prefix1 and second prefix0
## But the problem is, the complexity of this recurrence is very high 
def ones_zeros(n1, n0):
    if n1 == 0:
        return [tuple(0 for _ in range(n0))]
    elif n0 == 0:
        return [tuple(1 for _ in range(n1))]
    else:
        prefix1 = [(1,) + s for s in ones_zeros(n1-1, n0)]
        prefix0 = [(0,) + s for s in ones_zeros(n1, n0-1)]
        return prefix1 + prefix0
        
## Partitioning
## Generate all representations of a given positive integer n
## as the sum of a non-increasing sequence of positive integers
## e.g., n = 3, output: 3, 21, 12, 111
## e.g., n = 4, output: 4, 31, 22, 211, 13, 121, 112, 1111
def partition(n):
    if n == 1:
        return [(1, )]
    else:
        return [(n, )] + [
            (i, ) + s
            for i in range(1, n)
            for s in partition(n-i)
        ]

## Topological sorting (Dependency Graph)
## A directed graph without a cycle: An arrow from A -> B means there is 
## an dependency for A on B. Put the graph vertices in such an order
## that the end of any arrow preceds its beginning.
## Write a program that performs a topological sort in time O(n+m), 
## where n is # of vertices and m is the # of edges.
## e.g. for graph 
## 1 <- 2 <-
##           5 <- 6
## 3 <- 4 <-
## The order will be either 1, 2, 3, 4, 5, 6
## OR 3, 4, 1, 2, 5, 6 OR 132456
def topological_sort(g):
    freevertexes = [v for v in g if not g[v]]
    if len(freevertexes) == len(g):
        return freevertexes
    subg = dict(
        (u, vs.difference(freevertexes)) 
        for (u, vs) in g.items() 
        if u not in freevertexes)
    return freevertexes + topological_sort(subg)

## Connected Component of Undirected Graph
## The connected component of a vertex in a undirected graph
## is the set of all vertices that are reachable from the vertex
## via edges.
## Given an undirected graph and a certain vertex, write an algorithm
## that prints the connected component of the vertex. Each vertex in 
## the component should only be printed once. The complexity of the algorithm
## should be O(n+m) where n and m are numbers of vertexes and edges.
## To make the representation compact, here the undirected graph
## is represented by the tuple(set_of_vertices, set_of_edge_pairs)
## THIS IMPLMENTATION IS BASED ON ITERATIVE BACKTRACKING FRAMEWORK
## INSTEAD OF RECURSION, BECAUSE I THINK THE ITERATIVE FRAMEWORK
## IS MORE FLEXIBLE AS IT AVOIDS RECUSION_DEPTH_LIMIT.
## THE RECURSION VERSION SHOULD BE VERY STRAIGHTFORWARD.
def connected_component(graph, start):
    vertices, edges = graph
    explored, frontier = set(), [start]
    while frontier:
        u = frontier.pop()
        if u not in explored:
            yield u
            explored.add(u)
            frontier += [v for v in vertices 
                        if u+v in edges 
                        or v+u in edges]

## Quick sort
def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for n in seq[1:]:
            if n <= pivot: 
                left.append(n)
            else:
                right.append(n)
        return quick_sort(left) + [pivot] + quick_sort(right)

## Selection Algorithm: K-Percentile
## n integers, find the k-th element of them in ascending order
## using O(n) complexity
## AHA: sorting them takes O(nlogn)
## Naive algorithm could take O(nk) by keeping the kth smallest numbers
## O(n) basically means going through elements only constant times
## we know finding min or max needs O(n) time
## SOLUTION: Median of Medians algorithm with magic number 5
def kth_element(seq, k):
    ## 1. separate array into n/5 groups, each containing 5 elements
    ## TODO
    
## Tests
if __name__ == '__main__':
    ## test sequences
    assert len(sequences((1, 2, 3), 3)) == 27
    assert sequences((1, 2, 3), 2) == [
        (1, 1), (1, 2), (1, 3), 
        (2, 1), (2, 2), (2, 3), 
        (3, 1), (3, 2), (3, 3)]

    ## test permutations
    assert all_permutations((1, 2, 3), 2) == [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    assert all_permutations((1, 2, 3), 3) == [
        (1, 2, 3), (1, 3, 2), 
        (2, 1, 3), (2, 3, 1), 
        (3, 1, 2), (3, 2, 1)]
    ## test ones_zeros
    assert ones_zeros(1, 2) == [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    assert ones_zeros(2, 2) == [
        (1, 1, 0, 0), (1, 0, 1, 0), 
        (1, 0, 0, 1), (0, 1, 1, 0), 
        (0, 1, 0, 1), (0, 0, 1, 1)]
    ## test partition
    assert partition(2) == [(2,), (1, 1)]
    assert partition(3) == [(3,), (1, 2), (1, 1, 1), (2, 1)]
    assert partition(4) == [
        (4,), (1, 3), (1, 1, 2), 
        (1, 1, 1, 1), (1, 2, 1), 
        (2, 2), (2, 1, 1), (3, 1)]
    ## test topological sort
    g1 = {
        '6': set(['5']),
        '5': set(['2', '4']),
        '4': set(['3']),
        '3': set(),
        '2': set(['1']),
        '1': set()
    }
    g2 = {
        '1' : set(['2']),
        '2' : set(['3']),
        '3' : set(['4']),
        '4' : set(['5']),
        '5' : set()
    }
    assert topological_sort(g1) == ['1', '3', '2', '4', '5', '6']
    assert topological_sort(g2) == ['5', '4', '3', '2', '1']
    
    ## test connected_component for undirected graph
    ug1 = ('abcdefg', ('ab', 'ac', 'ae', 'ec', 'bd', 'fg'))
    assert list(connected_component(ug1, 'a')) == ['a', 'e', 'c', 'b', 'd']
    assert list(connected_component(ug1, 'f')) == ['f', 'g']
    
    ## test quick sort
    import random
    nums = range(1, 11)
    random.shuffle(nums)
    assert quick_sort(nums) == range(1, 11)
    assert quick_sort([3, 1, 1, 3, 2, 2, 2, 1, 3]) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
    
    ## test k_percentile
    print kth_element(nums, 1)
    print kth_element(nums, 5)
    print kth_element([3, 1, 1, 3, 2, 2, 2, 1, 3], 6)
    
    print 'all tests pass'