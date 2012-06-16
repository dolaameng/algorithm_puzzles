## In a binary tree a vertex can have 2, 1 or 0 edges to another vertex
## One possible represenation of a binary tree is via (root, vertexs, lefts, rights)
## structure, here root variable indicates the root of the tree, vertexs are
## list of vertexs (integers from 0 .. N-1), lefts are list of left neighbors, such
## that lefts[i] is the left child of vertex i. Value -1 in lefts/rights indicates there is no
## left or right branches at the certain node.
## e.g., N = 6, root = 1
## i: 0    1   2   3  4  5
## L: -1  -1   0  -1  5 -1
## R: -1  -1   4   2  1 -1
## It corresponds to a tree like this:
##                       5            1
##                          |       |
##                    0         4
##                      |     |
##                         2
##                      |
##                   3

## height of the tree
## depth at root = 0, height is the max depth in the tree
def height(tree, root):
    L, R = tree
    is_leaf = lambda v: L[v] == R[v] == -1
    if is_leaf(root): 
        return 1
    else:
        return 1 + max(height(tree, L[root]), height(tree, R[root]))

## Tests    
if __name__ == '__main__':
    ## test height
    tree = ([-1, -1, 0, -1, 5, -1], [-1, -1, 4, 2, 1, -1])
    assert height(tree, 3) == 4
    
    print 'all tests pass'