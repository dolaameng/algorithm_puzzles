## combinatorial generation can be sued to enumerate all element
## of some set X. The scheme for combinatorial generation is: 
## Impose a linear ordering on X (e.g., lexigraphic order) and 
## define an explict method to generate the next element of X

## Another general alternative of enumeration is by "backtracking"
## or so-called "tree traversal". 
## The essence is to enumerate all by developing partial solutions
## into complete solutions (using DFS or BFS)
## Sometime early-pruning can be used with backtracking.

###############################################################################################
###################### BACKTRACKING FRAMEWORK #################################################
## The iterative implementation is usally preferred than the recursion
## one because it is more general (BFS, DFS) and don't suffer from
## the recursion depth limit

## DATA STRUCTURES: 
## 1. frontier: stack (DFS), queue (BFS)
## 2. explored: not useful in TREE-EXPLORATION, but useful in GRAPH
## search, could be simply a set(), or a dict(parent->node), which 
## essentially represents the spanning tree of the graph
## 3. path (partial/complete solutions): could be simply a tuple of
## states, or a chain of state->action->state->action->...->finalstate

## FUNCTIONS:
## 1. is_complete: define the goal state
## 2. is_feasible: define if a solution if feasible (for early-prunning, or for finding next states),
## sometime it is also helpful to define it as is_feasible(solution, added)
## because it could be much cheaper to check if we already know solution is feasible
## in the first place. See nonattack_queens implementation as an example.
## But this calculation advantage is not always true, see sequences_with_sum example below
## 3. next_state: generate all possible (action, state) for the current state
## 4. heuristic: define the underestimate of the distance from current node to goal
## used when AStar search is exploited. 

## STRATEGY FOR DEVELOPING A PARTIAL SOLUTION:
## To avoid redundancy, some times imposing a certain order on the partial solution could 
## be helpful. See sequences_with_sum as an example.
## Extension of a partial solution could be independent of the current partial solution
## (e.g. extension with replacement) or the remaining resource could depend on the 
## current partial solutions

###########################################################################################

## Queens not attacking each other
## generate all the positions of n queens on an n x n chess board
## such that the queens are not attacking each other.
## Queen can move any number of squares vertically, horizontally or digonally
## e.g., n = 1: [(0, 0)]
## n = 2: []
## n = 3: [(0, 1), (1, 2), (2, 0), ...]
## INSPIRATION: since the queens cannot be on the same rows, 
## the search space can be reduced by exploring possible columns for each row
def nonattack_queens(n):
    def is_complete(solution):
        return len(solution) == n
    def feasible(solution, column):
        row = len(solution)
        for r, c in enumerate(solution):
            if abs(r-row) == abs(c-column):
                return False
        return True
    def next(solution):
        return [
            solution + (c, )
            for c in set(range(n)) - set(solution)
            if feasible(solution, c)
        ]
    frontier, explored = [], set()
    frontier.append(tuple())
    all_columns = []
    while frontier:
        solution = frontier.pop()
        ## not necessary here, because it is a tree, not a graph!
        if solution in explored:
            raise RuntimeError('should not happen, it is a TREE')
            continue
        explored.add(solution)
        if is_complete(solution):
            all_columns.append(solution)
        else:
            frontier += next(solution)
    return [
        zip(range(n), columns)
        for columns in all_columns
    ]

## An array of n positive integers a[1] .. a[n] and a positive integer S are given.
## Determine if S can be represented as a sum of some of the elements from array A
## Restriction: each element in the array can ONLY be used at most once.
## This is a special case of knapsack problem, it can also be solved by dynamic programming
## TO REDUCE REDUNDANCY OF EXPLORATION, MAINTAIN THE ORDER THE PARTIAL SOLUTION
## YOU CAN ALSO DO IT THROUGH SORTING SEQ BEFOREHAND
def sequences_with_sum(seq, s):
    N = len(seq)
    ## solution is represented as the sub-indices of seq
    def is_complete(solution):
        return s == sum(map(lambda i: seq[i], solution))
    def next(solution):
        maxi = max(solution) if solution else -1
        ## impose the lexigraphic order on partial solutions
        ## to avoid some redundancy
        return [
            solution + (added, )
            for added in set(range(maxi+1, N)).difference(solution)
            if is_feasible(solution, added)
        ]
    def is_feasible(solution, added):
        return s >= sum(map(lambda i: seq[i], solution)) + seq[added]
    frontier, explored = [], set()
    frontier.append(tuple())
    solutions = []
    while frontier:
        solution = frontier.pop()
        if solution in explored:
            ## should NOT happen, it is a TREE (only one path to a node)
            ## no path back, so it is a tree
            raise RuntimeError('should not happen')
            continue
        explored.add(solution)
        if is_complete(solution):
            solutions.append(solution)
        else:
            frontier += next(solution)
    return map(lambda solution: map(lambda i: seq[i], solution), solutions)
    
## Generate all sequences of n digits 0, 1 and 2 that do not contain a substring
## of type XX (repeated occurance of any patterns in a row). 
## E.g., for n = 6, the sequence 210102 is prohibited because it contains 1010
def sequences_without_xx(n):
    def is_complete(solution):
        return len(solution) == n
    def is_feasible(solution, added):
        for i, v in enumerate(solution):
            if v == added:
                X1 = solution[i+1:] + (added,)
                X2_start = max(i - len(X1) + 1, 0)
                X2 = solution[X2_start:i+1]
                if X1 == X2: return False
        return True
    def next(solution):
        return [
            solution + (added,)
            for added in (0, 1, 2)
            if is_feasible(solution, added)
        ]
    frontier, explored = [], set()
    frontier.append(tuple())
    solutions = []
    while frontier:
        solution = frontier.pop()
        if solution in explored:
            raise RuntimeError('should not happen')
        explored.add(solution)
        if is_complete(solution):
            solutions.append(solution)
        else:
            frontier += next(solution)
    return solutions
    
## tests
if __name__ == '__main__':
    ## test nonattack_queens
    assert nonattack_queens(1) == [[(0, 0)]]
    assert nonattack_queens(2) == []
    assert nonattack_queens(3) == []
    assert nonattack_queens(4) == [[(0, 2), (1, 0), (2, 3), (3, 1)], [(0, 1), (1, 3), (2, 0), (3, 2)]]
    ## test sequences_with_sum
    assert sequences_with_sum([1, 1, 2, 4, 8, 16], 10) == [[2, 8], [1, 1, 8]]
    assert sequences_with_sum([1, 2, 4, 8, 16, 32], 22) == [[2, 4, 16]]
    assert sequences_with_sum([1 for _ in range(10)], 1) == [[1] for _ in range(10)]
    ## test sequences_without_xx
    assert sequences_without_xx(1) == [(2,), (1,), (0,)]
    assert sequences_without_xx(3) == [
        (2, 1, 2), (2, 1, 0), (2, 0, 2), 
        (2, 0, 1), (1, 2, 1), (1, 2, 0), 
        (1, 0, 2), (1, 0, 1), (0, 2, 1), 
        (0, 2, 0), (0, 1, 2), (0, 1, 0)]
    assert (2, 1, 0, 1, 0, 2) not in sequences_without_xx(6)
    print 'all tests pass'