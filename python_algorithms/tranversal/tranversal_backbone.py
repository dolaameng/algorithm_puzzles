## backbone algorithms of 
## 1. tranversal (spanning tree) of connected graph
## 2. find all connected components of a graph, complexity of O(E + V)
## Duck type for graph: 1) iteratable for all nodes 2) given a node, find all neighbors (e.g. as a dict)

## G: Graph
## s: starting node
## S: set of forbidden nodes (for strongly connected graph walk)
## Return P: spanning tree as a dict of {node -> predecessor}
def walk(G, s, S = None):
    if not S: S = set()
    P, Q = {s: None}, [s] # P: predecessors Q: frontier queue
    while Q:
        u = Q.pop() # visiting order in queue matters in some cases
        for v in G[u].difference(P, S):
            P[v] = u # update the spanning tree, now we know where v is from
            Q.append(v)
    return P

## find all connected components by walking    
def components(G):
    seen = set()
    comps = []
    for u in G:
        if u not in seen:
            tree = walk(G, u)
            seen.update(tree)
            comps.append(tree)
    return comps

## test
if __name__ == '__main__':
    G = {
        'a': set('bcd'),
        'b': set('ad'),
        'c': set('ad'),
        'd': set('abc'),
        
        'e': set('gf'),
        'g': set('ef'),
        'f': set('eg'),
        
        'h': set('i'),
        'i': set('h')
    }
    assert walk(G, 'a') == {'a': None, 'c': 'a', 'b': 'a', 'd': 'a'}
    assert walk(G, 'b') == {'a': 'b', 'c': 'd', 'b': None, 'd': 'b'}
    assert walk(G, 'e') == {'e': None, 'g': 'e', 'f': 'e'}
    assert components(G) == [{'a': None, 'c': 'a', 'b': 'a', 'd': 'a'}, 
                            {'e': None, 'g': 'e', 'f': 'e'}, 
                            {'i': None, 'h': 'i'}]
    print 'all tests passed'