## Some simple examples
## I choose to use functions to implement state machines
## Use closure to create private variables for states
## Use member_variables of functions for public variables of states

import re

## Substring - Naive Implementation
## check if a string contains a substring
## IT FAILS ON EXAMPLES THAT NEED TO LOOK BACK THE PATTERN
## SEE THE TEST CASES BELOW
def substr_search(text, s):
    ## states out-sub, in-sub, and matched
    def out_sub_state(i, c):
        if c == s[0]:
            return in_sub_state(0)
        else:
            return out_sub_state
    def in_sub_state(isub):
        def _help(i, c):
            if isub == len(s) - 1:
                matched_state.start = i - len(s)
                matched_state.end = i
                return matched_state 
            elif c == s[isub+1]:
                return in_sub_state(isub+1)
            else:
                return out_sub_state
        return _help
    def matched_state(i, c): pass
    ## consume the string
    state = out_sub_state
    for (i, c) in enumerate(text):
        state = state(i, c)
        if state == matched_state:
            return state.start, state.end
    return None

## tests
if __name__ == '__main__':
    ## test substring match
    ## working example
    text, needle = 'bcdefgabcabc', 'abc'
    r = re.search(needle, text)
    assert substr_search(text, needle) == (r.start(), r.end())
    ## non-working example
    ## CANNOT RECOGNIZE ababc
    text, needle = 'xyzabababc', 'ababc'
    r = re.search(needle, text)
    assert substr_search(text, needle) != (r.start(), r.end())
    print 'cannot find %s in %s' % (needle, text)
    print 'see Knuth-Morris_Pratt algorithm for the right solution'
    
    print 'all tests pass'