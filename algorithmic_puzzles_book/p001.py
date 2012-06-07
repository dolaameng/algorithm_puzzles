# farmer, wolf, goat and cabbage
# idea and representations: (set('f', 'w', 'g', 'c'), set())
# use backtracking

## Lesson learned: 
## (1) use iteration instead of recursion is quite general in search
## (2) in search, the path should be (state, action, state ...)
## (3) explore a little bit best representation by testing solution, testing validaty, and extension
## (4) make the representation of state as hashable as possible -> used for explored

def is_solution(s):
    L, R = s
    return len(L) == 0 and R == frozenset(['f','w','g','c'])

def is_valid(s):
    L, R = s
    return not (('f' in L and frozenset('wg') <= R) or
                 ('f' in R and frozenset('wg') <= L) or
                 ('f' in L and frozenset('gc') <= R) or
                 ('f' in R and frozenset('gc') <= L))
    
def extend(s): 
    L, R = s
    bank = L if 'f' in L else R
    other = R if bank == L else L
    items = [item for item in bank if item != 'f']
    step = 1 if bank == L else -1
    arrow = '->' if other == R else '<-'
    return [
        ('f'+item+arrow, (bank - frozenset([item, 'f']), other | frozenset([item, 'f']))[::step])
        for item in items+['f']
    ]
    
def solve(init):
    explored = set()
    frontier = [[init]]
    while frontier:
        node = frontier.pop()
        s = node[-1]
        if is_solution(s):
            return node
        if is_valid(s):
            explored.add(s)
            next_nodes = [node + [a, s] for a, s in extend(s) if s not in explored]
            frontier += next_nodes
    
def show_actions(s):
    return s[1::2]
    
## test
if __name__ == '__main__':
    # test is_solution
    assert is_solution((frozenset(), frozenset('fwgc')))
    assert not is_solution((frozenset('fw'), frozenset('gc')))
    # test is_valid
    assert is_valid((frozenset(), frozenset('fwgc')))
    assert is_valid((frozenset('cw'), frozenset('gf')))
    assert not is_valid((frozenset('wg'), frozenset('fc')))
    # test extend
    assert extend((frozenset('fwgc'), frozenset())) == [('fc->', (frozenset(['w', 'g']), frozenset(['c', 'f']))), 
        ('fg->', (frozenset(['c', 'w']), frozenset(['g', 'f']))), 
        ('fw->', (frozenset(['c', 'g']), frozenset(['w', 'f']))), 
        ('ff->', (frozenset(['c', 'w', 'g']), frozenset(['f'])))]
    ##assert solve((frozenset(), frozenset('fwgc'))) == [(frozenset([]), frozenset(['c', 'g', 'w', 'f']))]
    assert show_actions(solve((frozenset('fwgc'), frozenset()))) == ['fg->', 'ff<-', 'fw->', 'fg<-', 'fc->', 'ff<-', 'fg->']
    print 'all tests passed'
    