## Some applicatoins that can be solved by using a set structure
## Python has built-in support for set

## Graph Walk Problem
## Find all the vertices of a DIRECTED graph that can be reached
## from a given vertex along the graph edges. The program should
## run in time Cm, where m is the total number of edges leaving
## the reachable vertices and C is a constant
## AHA: This a typical tree-walk (backtracking) algorithm, the
## output is a spanning tree rooted at the start node.
## A GRAPH is represented as a dict of node -> set(connected nodes...)
## Solution: change the structure of explored to perserve the spanning
## tree structure
def graph_walk(start, graph):
    explored, frontier = {start: None}, [start]
    while frontier:
        u = frontier.pop()
        for v in graph[u].difference(explored):
            explored[v] = u
            frontier.append(v)
    return explored


## Tests
if __name__ == '__main__':
    ## test graph_walk
    g1 = {
        'a': set(['b', 'd']),
        'b': set(['c']),
        'c': set(),
        'd': set(),
        'e': set(['d', 'f']),
        'f': set(),
    }
    assert graph_walk('a', g1) == {'a': None, 'c': 'b', 'b': 'a', 'd': 'a'}
    assert graph_walk('e', g1) == {'e': None, 'd': 'e', 'f': 'e'}
    
    print 'all tests pass'