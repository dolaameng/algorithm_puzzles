"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from simple_profile import timed_call
from math import ceil

## AHA: backtracking - building solution from partial solutions
## but to avoid redudance, specify the order of abc as increasing numbers

def product(iterable):
    return reduce(lambda x,y: x*y, iterable)

## backtracking
def solution1():
    N = 1000
    def is_complete(solution):
        return len(solution) == 3 and solution[0]**2 + solution[1]**2 == solution[2]**2
    def next(solution):
        L = len(solution)
        if L == 3:
            return []
        elif L == 2:
            return [solution + [N-sum(solution)]] if N-sum(solution) >= solution[1] else []
        else:
            return [solution + [n] for n in range(solution[0], (N-solution[0])/2 + 1)]
    
    frontier = [[n] for n in range(1, N-1)] ## partial/complete solutions
    
    while frontier:
        solution = frontier.pop()
        if is_complete(solution):
            yield solution
        else:
            frontier += next(solution)
            
## simplication of backtracking sine the number of parts in solution is fixed
def solution2():
    N = 1000
    for a in range(1, int(ceil(N/3))+1):
        for b in range(a, int(ceil((N-a)/2))+1):
            c = N - a - b
            if a**2 + b**2 == c**2:
                yield (a, b, c)
            
## tests
if __name__ == '__main__':
    print timed_call(lambda: product(next(solution1()))) ## 0.05
    print timed_call(lambda: product(next(solution2()))) ## 