## Graph Algorithm Exercise Part I: COMPUTATION OF SHORTEST PATHS
##################### SOME FAMOUS SHORTEST PATH ALGORITHMS #######
## 1. Dijkstra Algorithm: single-source, nonnegative shortest path
## 2. Bellman-Ford Algorithm: single-source, weights could be negative
## 3. A* search: single-pair, use heuristics to speed up the search
## 4. Floyd-Warshall Algorithm: all-pairs shortest paths
## 5. Johnson's Algorithm: all pairs shortest paths, may be faster
## than Floyd-Warshall on sparse graphs
## 6. Perturbation theory: finds (at worst) the locally shortest path
##################################################################

INF = float('inf')

## Dijkstra Algorithm
## Given a directed weighted graph, find the minimal travel cost from
## a certain node to all other nodes in time O(n**3)
## Dijkstra Algorithm essentially has a flavor of Dynamic Programming 
## AHA: ###################
## 1. DATA STRUCTURES: unvisted (vertex set), distances (hash), current (single vertex)
## 2. INITIALIZATION: unvisited = all vertices (including start), 
## distances (0 for start, INF for rest), current (start)
## 3. UPDATE: 
## (1) distances: update distances all unvisted neighbors of current node
## (2) unvisited: a vertex remains unvisited till all its neighbors have been checked
## (3) current: pick the vertex with minimal distance from unvisited
## 4. TERMINATION: if unvisited is empty OR all vertices in unvisted have dist of INF
## 5. BONUS: precedences (hash of vertex->vertex) can be used to track the path
## it is like the track of the reverse of the shortest path
def dijkstra_shortest_path(start, graph):
    unvisited = set(graph.keys())
    distances = dict([(v, 0 if v == start else INF) for v in graph.keys()])
    precedences = {start: None}
    while unvisited:
        current = min(unvisited, key = lambda v: distances[v])
        if distances[current] == INF:
            break
        for v, current_to_v in graph[current].items():
            if (v in unvisited and
                current_to_v+distances[current] < distances[v]):
                distances[v] = current_to_v+distances[current]
                precedences[v] = current
        unvisited.remove(current)
    def restore_paths():
        paths = dict((v, [v]) for (v, _v) in precedences.items() if _v is None)
        while len(paths) < len(precedences):
            paths.update(dict([
                (v, paths[u] + [v])
                for u in paths
                for (v, _v) in precedences.items()
                if _v == u
            ]))
        return paths
    shortest_paths = restore_paths()
    return distances, shortest_paths
    
## A* Search Algorithm
## heuristic function h must be admissible for Astar to be 
## adminissable (optimal). An admissable h means it never
## overestimates the actual minimal cost of reaching the goal
## IN GENERAL: Dijkstra algorithm can be viewed as a special case
## of A* where h(x) = C for all x. And General Depth-First Search
## can be implemented using A* by considering that there is a global
## counter C initialized with a very large value. Every time we process
## a node we asign C to all of its newly discovered neighbors, and decreasing
## Counter by 1 after assignment.
############ AHA:
## Same search framework as traversal, backtracking, and etc.
## Main difference is the frontier strucutre, here it is based on
## priority queue where priority is calcuated as "cost + heuristic"
def astar_shortest_path(start, end, graph, h = None):
    ## default heuristic function - essentially dijkstra search
    if not h:
        h = lambda v: 0  
    explored, frontier = set(), [start]
    precedences = {start: [start]}
    distances = {start: 0}
    while frontier:
        frontier = sorted(frontier, key = lambda v: distances[v] + h(v))
        current = frontier.pop(0)
        if current in explored:
            continue
        explored.add(current)
        if current == end:
            break
        for v, current2v in graph[current].items():
            frontier.append(v)
            if (v not in distances or
                current2v+distances[current] < distances[v]):
                distances[v] = current2v + distances[current]
                precedences[v] = precedences[current] + [v]
    return distances[end], ''.join(precedences[end])
    
## Floyd Warshall Algorithm
## Finding the transitive closure and shortest paths between
## all pairs in a weighted graph. The original algorithm assumes
## there is no negative cycles in the graph, and if they do exist,
## the Floyd-Warshall algorithm can be used to detect them.
## It is essentially an example of dynamic programming, running in O(n**3)
## THE KEY TO IMPLEMENT DYNAMIC PROGRAMMING IS TO ASK THE QUESTION:
## IF YOU ALREADY GOT THE CURRENT SOLUTION, WHAT'S THE IMMEDIATE
## NEXT THING TO CALCULATE?
## IN THIS CASE, WE KNOW THE SHORTEST DISTANCE FROM I TO J IF 
## WE ALREADY KNOW THE SHORTEST DISTANCE FROM I TO ALL THE NEIGHBORS
## J
###### AHA:
## the shortest path from i to j is the min of all paths i->k->j
## over all possible intermediate vertices k
## 1. DYNAMIC PROGRAMMING VERSION
############################################################
## CONSIDER THE SHORTEST_PATH TABLE INDEXED BY (I, J, K) THAT
## RETURNS THE SHORTEST POSSIBLE PATH FROM I TO J VIA INTERMEDIATE
## POINTS FROM (V1, V2, ..., VK). GIVEN THAT, THE NEXT IMMEDIATE
## RESULT WOULD BE (I, J, K+1), I.E., THROUGH VIA-POINTS (V1, V2, ..., VK+1)
## 
## CLEARLY, THERE ARE TWO CANDIDATES FOR THE PATHS: EITHER THE REAL
## SHORTEST PATH USES ONLY VERTICES IN SET {1,...,K} OR THERE
## EXISTS SOME PATH THAT GOES FROM I TO K+1, THEN FROM K+1 TO J.
## AND THE SECOND CANDIDATE CAN BE REPRESENTED AS:
## (SHORTEST FROM I TO K+1 THROUGH 1,...,K) + (SHORTEST FROM K+1 TO J THROUGH 1,...,K)
## THAT IS WHERE THE RECURSION REALLY LIES. I.E.,
## shortest(i, j, k+1) = min(shortest(i, j, k), 
##                           shortest(i, k+1, k) + shortest(k+1, j, k)) 
############################################################
def floyd_warshall_algorithm_dp(graph):
    distances = dict([
        ((u, v), 
        (0 if u is v
        else graph[u][v] if v in graph[u]
        else INF))
        for u in graph
        for v in graph
    ])
    ## THE ORDER OF THE LOOP IS BEAUTIFUL!
    for k in graph: # use intermediate vertices up to k
        for i in graph: # update shortest distance pair i -> j
            for j in graph:
                distances[(i, j)] = min(distances[(i, j)], 
                                distances[(i, k)] + distances[(k, j)])
    return distances
## 2. MEMOIZATION VERSION
############################################################
## A VERY GOOD EXAMPLE OF USING HISTORY PARAMETER
## TO AVOID CYCLE-RECURSION IN MEMOIZATION IMPLEMENTATION
############################################################
def floyd_warshall_algorithm_memo(graph): 
    def neighbors_to(v):
        return [u for u in graph if v in graph[u]]
    def shortest_dist(start, end, explored = None):
        if explored is None: explored = set()
        ## redefine distances every time for new u, v
        ## because the calculated distances for different u, v
        ## are not the same
        distances = dict([
            ((u, u), 0)
            for u in graph
        ])
        if (start, end) not in distances:
            candidates = [
                shortest_dist(start, via, explored | set([end])) + graph[via][end]
                for via in neighbors_to(end)
                if via not in explored
            ]
            distances[(start, end)] = min(candidates) if candidates else INF
        return distances[(start, end)]
    shortest_distances = dict([
        ((u, v), shortest_dist(u, v))
        for u in graph
        for v in graph
    ])
    return shortest_distances
                

    
## tests
if __name__ == '__main__':
    ## some common test examples
    g1 = {
        'A': {'B': 5, 'C': 2},
        'B': {'E': 1},
        'C': {'B': 1, 'D': 1},
        'D': {'B': 2, 'F': 6},
        'E': {'A': 1}, 
        'F': dict()
    }
    
    ## test shortest_path from a certain start node
    shortest_distances, shortest_paths = dijkstra_shortest_path('A', g1)
    assert shortest_distances == {'A': 0, 'C': 2, 'B': 3, 'E': 4, 'D': 3, 'F': 9}
    assert shortest_paths == {
        'A': ['A'], 'C': ['A', 'C'], 'B': ['A', 'C', 'B'], 
        'E': ['A', 'C', 'B', 'E'], 'D': ['A', 'C', 'D'], 
        'F': ['A', 'C', 'D', 'F']}
        
    ## test astar_shortest_path
    ## with a very specific heuristic function
    shortest_distances, shortest_paths = astar_shortest_path('A', 'B', g1, 
                h = lambda v: 1 if 'B' in g1[v] else 2)
    assert shortest_distances == 3
    assert shortest_paths == 'ACB'
        
    ## test floyd_warshall_algorithm memoization version
    assert floyd_warshall_algorithm_memo(g1) == {
        ('F', 'B'): INF, ('E', 'F'): 10, ('D', 'D'): 0, 
        ('B', 'A'): 2, ('D', 'E'): 3, ('A', 'F'): 9, 
        ('B', 'F'): 11, ('C', 'D'): 1, ('A', 'B'): 3, 
        ('F', 'C'): INF, ('E', 'A'): 1, ('B', 'B'): 0, 
        ('E', 'E'): 0, ('D', 'A'): 4, ('C', 'C'): 0, 
        ('D', 'B'): 2, ('B', 'C'): 4, ('A', 'A'): 0, 
        ('E', 'D'): 4, ('A', 'E'): 4, ('F', 'F'): 0, 
        ('F', 'D'): INF, ('A', 'D'): 3, ('E', 'C'): 3, 
        ('B', 'D'): 5, ('C', 'F'): 7, ('F', 'A'): INF, 
        ('D', 'C'): 6, ('D', 'F'): 6, ('A', 'C'): 2, 
        ('F', 'E'): INF, ('C', 'A'): 3, ('E', 'B'): 4, 
        ('C', 'B'): 1, ('B', 'E'): 1, ('C', 'E'): 2}
    
    ## test floyd_warshall_algorithm dynamic programming version
    assert floyd_warshall_algorithm_dp(g1) == {
        ('F', 'B'): INF, ('E', 'F'): 10, ('D', 'D'): 0, 
        ('B', 'A'): 2, ('D', 'E'): 3, ('A', 'F'): 9, 
        ('B', 'F'): 11, ('C', 'D'): 1, ('A', 'B'): 3, 
        ('F', 'C'): INF, ('E', 'A'): 1, ('B', 'B'): 0, 
        ('E', 'E'): 0, ('D', 'A'): 4, ('C', 'C'): 0, 
        ('D', 'B'): 2, ('B', 'C'): 4, ('A', 'A'): 0, 
        ('E', 'D'): 4, ('A', 'E'): 4, ('F', 'F'): 0, 
        ('F', 'D'): INF, ('A', 'D'): 3, ('E', 'C'): 3, 
        ('B', 'D'): 5, ('C', 'F'): 7, ('F', 'A'): INF, 
        ('D', 'C'): 6, ('D', 'F'): 6, ('A', 'C'): 2, 
        ('F', 'E'): INF, ('C', 'A'): 3, ('E', 'B'): 4, 
        ('C', 'B'): 1, ('B', 'E'): 1, ('C', 'E'): 2}
    
    print 'all tests pass'