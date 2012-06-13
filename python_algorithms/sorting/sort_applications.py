## Without order, everything goes to chaos
## Some applicatons that can be made much easier by pre-sorting

## intervals problems
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

## Test
if __name__ == '__main__':
    ## test max_intervals
    assert max_intervals([(0, 1), (0.1, 0.7), (0.3, 0.5)]) == 3
    assert max_intervals([(0, 2), (1, 5), (3, 6), (4, 7)]) == 3
    print 'all tests pass'