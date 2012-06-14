## Without order, everything goes to chaos
## Some applicatons that can be made much easier by pre-sorting

import math

## INTERVALS PROBLEM
## Suppose that n closed intervals [a[i], b[i]] on the real line are given.
## Find the maximal k such that there exists a point covered by k intervals,
## i.e., the maximal number of layers. The complexity should be of nlogn
## e.g. for inputs [(0, 1), (0.1, 0.7), (0.3, 0.5)], k = 3
## Inspirations: Think of intervals as layers of an onion, 
## when you come across a starting point, you enter another new layer,
## when you come across a ending point, you leave one previous layer.
## The layers could have overlaps, overlaps happen when you come across
## another layer before leaving the current one
## SORT all starting/ending points together, come across them in the order
## and count the current layers during the process. The max counting is
## the max overlaps
def max_intervals(intervals):
    points = sum([ [(L, 'L'), (R, 'R')] for L, R in intervals], [])
    labels = [label for pt, label in sorted(points, key = lambda (pt, label): pt)]
    max_overlap = overlap = 0
    for label in labels:
        overlap += 1 if label == 'L' else -1
        if overlap > max_overlap:
            max_overlap = overlap
    return max_overlap

## POLYGONAL ARC PROBLEM
## Assume that n points in the plane are given. Find a polygonal arc 
## with n-1 sides whose vertices are the given points, and whose sides
## do not intersect. Adjacent sides may form a 180 degree angle. 
## The number of operations should be of order nlogn
## SOLUTION: sort all the points with respect to the x-coordinate; when
## x-coordinates are equal, take the y-coordinate into account, then 
## connect all vertices by line segments (essentially in the lexigraphic order)
## THE CONSTRAINT is: never go back along x axis
def arc(points):
    points = sorted(points)
    return points

## POLYGON PROBLEM (NOT NECESSARILY CONVEX)
## For a given set of points in the plane, find a polygon having these 
## points as vertices. 
## SOLUTION: Same as to the other similiar problems, FIND a specific order,
## and connect the points in that order
## For Polygon problem: take the leftmost point (with minimal x-coordinate),
## consider all the rays starting from this point and going through all other points.
## Sort these rays according to their (slopes, distances to initial point). 
## The polygon goes from the initial point along the ray with minimal slope,
## then visits all the points in the order chosen, returning via the ray
## with maximal slope (where points are visited in the reversed order).
## In other words, the polygon is formed in counter-clockwise order
def polygon(points):
    def slope(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return float(y2-y1) / (x2-x1) if x1 != x2 else float('inf')
    def dist(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    origin = min(points, key = lambda (x, y): x)
    points = sorted(points, key = lambda pt: (slope(origin, pt), dist(origin, pt)))
    return points

## CONVEX HULL PROBLEM
## Assume n points in the plane. Find their convex hull, i.e., the minimal convex
## polygon that contains all the points. e.g., A rubber band put on
## the nails is the convex hull of the nails inside it. The number of operations should
## be nlogn.
## A major difference between a convex hull of a set of points and a polygon of them is that
## for a convex hull, not all the points need to be the vertexes of the hull (they could be inside)
## HINT: Order all the points according to one of the orderings (i.e., (x,y) or (slope, distance))
## in the above two problems. Then construct the convex hull considering the points one by one
## To maintain information about the current convex hull, it is useful to use a deque. However,
## when the points are ordered according to their slopes, it is not necessary.
############################################################################################
####################################### Algorithms for Convex Hull #########################
## Several Convex Hull Algorithms from WIKI Page
## http://en.wikipedia.org/wiki/Convex_hull_algorithms
## 1. Akl-Toussaint heuristic (not the minimal convex hull):
## (1) find the convex quardrilateral by finding the 4 points with minx, maxx, miny, maxy
## that defines the boundary for other points except these four
## (2) The boundary can be defined as irregular shape by adding points with smallest and largest
## sums of x- and y- coordinates as well as smallest and largest differences of x- and y- coords
## the inside can be safely discarded
#############################################################################################
## Implementation of Andrew's monotone chain convex hull algorithm
## (1) sort points in lexicographic order according to x- and y- coords
## (2) construct upper and lower hulls of the points each in O(n) time in COUNTER-CLOCKWISE order
## The upper and lower hulls must be found separately because they are using different
## lexigraphic order of the points (lower uses the left->right order, and upper uses the right->left orders)
## even the convex hull boundary can be found in the same counter-clockwise order
def convex_hull(points):
    """
    Input: iterable seqence of (x, y) pairs representing 2D points
    Output: list of vertices of the convex hull in counter-clockwise order, 
    starting from the vertex with the lexicographically smallest coord.
    Implement Andrew's monotone chain algorithm in nlogn complexity
    """
    ## define 2D cross product of OA and OB vectors, i.e., the z-component
    ## of their 3d cross product. 
    ## Returns a POSITIVE value, if OAB makes a counter-clockwise turn, 
    ## NEGATIVE for clockwise turn, and zero if the points are COLLINEAR.
    ## (RIGHT HAND RULE)
    ## for 2D case, for vectors (x1, y1) and (x2, y2), 
    ## their cross product is defined as x1y2 - x2y1
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    ## remove duplicate points and sort them in lexigraph order
    points = sorted(set(points))
    ## trivial case
    if len(points) <= 1:
        return points
    ## build lower hull - MUST RESERVER counter-clockwise
    lower_hull = []
    for p in points:
        # check previous 2 points - NOT counter-clockwise, pop the middle one, otherwise added
        while len(lower_hull) >= 2 and cross(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)
    ## build upper hull (visit in reverse order) - MUST RESERVER counter-clockwise
    upper_hull = []
    for p in points[::-1]:
        while len(upper_hull) >= 2 and cross(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)
    ## concat lower and upper hulls
    ## last point of each list is omitted because it is repeated at the beginning of the other
    return lower_hull[:-1] + upper_hull[:-1]


## Test
if __name__ == '__main__':
    ## test max_intervals
    assert max_intervals([(0, 1), (0.1, 0.7), (0.3, 0.5)]) == 3
    assert max_intervals([(0, 2), (1, 5), (3, 6), (4, 7)]) == 3
    
    ## test arc
    line_points = [(0, 1), (0, 3), (0, 2)]
    circle_points = [(math.cos(i*math.pi/4), math.sin(i*math.pi/4)) for i in range(8)]
    circle_with_origin_points = circle_points + [(0, 0)]
    assert arc(line_points) == [(0, 1), (0, 2), (0, 3)]
    assert arc(circle_points) == sorted(circle_points)
    
    ## test polygon
    assert polygon(line_points) == [(0, 1), (0, 2), (0, 3)]
    #a whole pie
    assert polygon(circle_points) == [
        (-0.7071067811865477, -0.7071067811865475), 
        (-1.8369701987210297e-16, -1.0), 
        (0.7071067811865475, -0.7071067811865477), 
        (1.0, 0.0), 
        (0.7071067811865476, 0.7071067811865475), 
        (6.123233995736766e-17, 1.0), 
        (-0.7071067811865475, 0.7071067811865476), 
        (-1.0, 1.2246467991473532e-16)]
    #a bitten pie - one piece missing
    assert polygon(circle_with_origin_points) == [
        (-0.7071067811865477, -0.7071067811865475), 
        (-1.8369701987210297e-16, -1.0), 
        (0.7071067811865475, -0.7071067811865477), 
        (0, 0), 
        (1.0, 0.0), 
        (0.7071067811865476, 0.7071067811865475), 
        (6.123233995736766e-17, 1.0), 
        (-0.7071067811865475, 0.7071067811865476), 
        (-1.0, 1.2246467991473532e-16)]  
          
    ## test convex_hull
    assert convex_hull(line_points) == [(0, 1), (0, 3)]
    assert convex_hull(circle_points) == [
        (-1.0, 1.2246467991473532e-16), 
        (-0.7071067811865477, -0.7071067811865475), 
        (-1.8369701987210297e-16, -1.0), 
        (0.7071067811865475, -0.7071067811865477), 
        (1.0, 0.0), 
        (0.7071067811865476, 0.7071067811865475), 
        (6.123233995736766e-17, 1.0), 
        (-0.7071067811865475, 0.7071067811865476)]
    assert convex_hull(circle_with_origin_points) == [
        (-1.0, 1.2246467991473532e-16), 
        (-0.7071067811865477, -0.7071067811865475), 
        (-1.8369701987210297e-16, -1.0), 
        (0.7071067811865475, -0.7071067811865477), 
        (1.0, 0.0), 
        (0.7071067811865476, 0.7071067811865475), 
        (6.123233995736766e-17, 1.0), 
        (-0.7071067811865475, 0.7071067811865476)]
    
    print 'all tests pass'