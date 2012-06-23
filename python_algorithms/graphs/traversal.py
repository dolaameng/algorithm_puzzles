## Graph Algorithm Exercise Part II: TRAVERSAL OF GRAPHS
## Traversal codes are also present in other packages 
## such as ../traversal/traversal_backbone.py and ../backtracking/backtracking.py
## and ./shortest_path (A* search)
## Again the framework for different is basically the same
## different search has different traversal orders, which corresponds
## to different data structure in frontier.

import collections

## Breath First Search
def breath_first_search(graph, start):
    explored, frontier = set(), [start]
    paths = collections.OrderedDict([(start, [start])])
    while frontier:
        current = frontier.pop(0)
        explored.add(current)
        for v in graph[current]:
            if v not in explored:
                frontier.append(v)
                paths[v] = paths[current] + [v]
    return paths

## Depth first search    
def depth_first_search(graph, start):
    explored, frontier = set(), [([start], start)]
    paths = []
    while frontier:
        frontier = sorted(frontier, key = lambda (path, v): len(path))
        path, current = frontier.pop()
        if current in explored:
            continue
        paths.append((current, path))
        explored.add(current)
        for v in graph[current]:
            if v not in explored:
                newpath = path + [v]
                frontier.append((newpath, v))        
    return paths
    
## Bipartite Graph
## An undirected graph is a bipartite graph if its vertices
## may be colored in two colors in such a way that each edge
## connects vertices of different colors. Find an algorithm
## that checks whether a graph is a bipartite graph in time
## O(#edges+#vertices)
## AHA: using breath-first and depth-first search. In each 
## connected component, if the color of one vertices is
## picked, the colors of all other vertices are fixed
## HERE WE ASSUME GRAPH IS CONNECTED
def is_bipartite(graph, start = None):
    reverse = lambda c: 'red' if c is 'blue' else 'blue'
    if not start:
        start = graph.keys()[0]
    explored, frontier = set(), [start]
    colors = {start: 'red'}
    while frontier:
        current = frontier.pop()
        if current in explored:
            continue
        explored.add(current)
        for neighbor in graph[current]:
            if neighbor in colors:
                if colors[neighbor] == colors[current]:
                    return False
            colors[neighbor] = reverse(colors[current])
            frontier.append(neighbor)
    return True
    
## Topological Sorting of Graph
## A topological sorting of a directed graph is a linear ordering
## of its vertices such that for every edge u->v, u comes before v.
## A topological ordering is possible if and only if the graph has
## no directed cycles, i.e., if it is a directed acyclic graph (DAG).
## Any DAG has at least one topological ordering, and algorithms exist
## find the ordering in O(V+E) time.
## THE IMPLEMENTATION IS NOT ELEGANT, TOO MUCH REDUNDANCY
def topological_sort(graph):
    def reverse(g):
        to_from_edges = [
            (to, fr)
            for fr, tos in g.items()
            for to in tos
        ]
        return to_from_edges
    ## reverse the graph from u -> v hash to v <- u has
    reversed_graph = reverse(graph)
    unvisited, in_order = set().union(graph), []
    while reversed_graph:
        reversed_graph_vertices = map(lambda (to,fr): to, reversed_graph)
        free_vertices = [
            v
            for v in unvisited
            if v not in reversed_graph_vertices
        ]
        reversed_graph = [
            (to, fr)
            for (to, fr) in reversed_graph
            if fr not in free_vertices
        ]
        in_order += free_vertices
        unvisited -= set(free_vertices)
    in_order += unvisited
    return in_order

## tests
if __name__ == '__main__':
    ## g1 undirected graph
    g1 = {
        'A': ('B', 'C', 'H'),
        'B': ('A', 'D', 'E'),
        'C': ('A', 'F', 'G'),
        'D': ('B',),
        'E': ('B',),
        'F': ('C',),
        'G': ('C', 'H'),
        'H': ('A', 'G')
    }
    ## g2 is g1 without H, g2 is a full binary tree rooted at 'A'
    g2 = {
        'A': ('B', 'C'),
        'B': ('A', 'D', 'E'),
        'C': ('A', 'F', 'G'),
        'D': ('B',),
        'E': ('B',),
        'F': ('C',),
        'G': ('C',),
    }
    ## g3 is an undirected triangle
    g3 = {
        'A': ('B', 'C'),
        'B': ('A', 'C'),
        'C': ('A', 'B')
    }
    ## g4 is a square
    g4 = {
        'a': ('b', 'c'),
        'b': ('a', 'd'),
        'c': ('a', 'd'),
        'd': ('b', 'c')
    }
    ## g5 is g4 with a diagonal b-c
    g5 = {
        'a': ('b', 'c'),
        'b': ('a', 'd'),
        'c': ('a', 'd'),
        'd': ('b', 'c'),
        'b': ('c',),
        'c': ('b',)
    }
    ## dag for topological sorting
    ## valid sortings include
    ## (7, 5, 3, 11, 8, 2, 9, 10), (3, 5, 7, 8, 11, 2, 9, 10),
    ## (3, 7, 8, 5, 11, 10, 2, 9), (5, 7, 3, 8, 11, 10, 9, 2),
    ## (7, 5, 11, 3, 10, 8, 9, 2), (7, 5, 11, 2, 3, 8, 9, 10)
    g6 = {
        2: tuple(),
        3: (8, 10),
        5: (11,),
        7: (8, 11),
        8: (9,),
        9: tuple(),
        10: tuple(),
        11: (2, 9, 10)
    }
    ## linear dag
    g7 = {
        5: (6, ),
        2: (3, ),
        3: (4, ),
        4: (5, ),
        1: (2, ),
        6: tuple()
    }
    ## test breath_first_search
    assert breath_first_search(g1, 'A') == collections.OrderedDict([
        ('A', ['A']), ('B', ['A', 'B']), ('C', ['A', 'C']), ('H', ['A', 'H']), 
        ('D', ['A', 'B', 'D']), ('E', ['A', 'B', 'E']), ('F', ['A', 'C', 'F']), 
        ('G', ['A', 'H', 'G'])])
    assert breath_first_search(g2, 'A') == collections.OrderedDict([
        ('A', ['A']), 
        ('B', ['A', 'B']), ('C', ['A', 'C']), 
        ('D', ['A', 'B', 'D']), ('E', ['A', 'B', 'E']), 
        ('F', ['A', 'C', 'F']), ('G', ['A', 'C', 'G'])])
        
    ## test depth_first_search
    assert depth_first_search(g1, 'A') == [
        ('A', ['A']), ('H', ['A', 'H']), ('G', ['A', 'H', 'G']), 
        ('C', ['A', 'H', 'G', 'C']), ('F', ['A', 'H', 'G', 'C', 'F']), 
        ('B', ['A', 'B']), ('E', ['A', 'B', 'E']), ('D', ['A', 'B', 'D'])]
    assert depth_first_search(g2, 'A') == [
        ('A', ['A']), ('C', ['A', 'C']), ('G', ['A', 'C', 'G']),
         ('F', ['A', 'C', 'F']), ('B', ['A', 'B']), 
         ('E', ['A', 'B', 'E']), ('D', ['A', 'B', 'D'])]
         
    ## test is_bipartite
    assert is_bipartite(g1) == True
    assert is_bipartite(g3) == False
    assert is_bipartite(g4) == True
    assert is_bipartite(g5) == False
    
    ## test topological sort
    assert topological_sort(g6) == [3, 5, 7, 8, 11, 2, 9, 10]
    assert topological_sort(g7) == range(1, 7)
    
    print 'all tests pass'