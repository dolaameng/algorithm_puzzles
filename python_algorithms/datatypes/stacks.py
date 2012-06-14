## Stack: LIFO (last-in-first-out)
## Python List (with append and pop) is a natrual implementation of this
## In essence, stack specifies MATCHING INFORMATION in the sequence

## Language Recognition Problem
## the language model accepts the following sequneces:
## S -> empty
## S -> S S
## S -> [ S ]
## S -> ( S )
## It is context-free language but not a regular expression
## e.g., accepted sequences "()", "[[]]", "[()[]()] []"
## unaccepted sequences "]", ")(", "(]", "([)]"
## Inspiration: Think about the onion layer model as discussed 
## in ../sorting/sort_application.py
def language_accept(text):
    s = []
    text = text.replace(' ','')
    for c in text:
        if c in ('(', '['):
            s.append(c)
        elif c in (')', ']'):
            cc = s.pop() if s else ''
            if cc+c not in ('()', '[]'):
                return False
        else:
            return False
    return False if len(s) > 0 else True
    
## tests
if __name__ == '__main__':
    ## test language_accept
    for t in ["()", "[[]]", "[()[]()] []"]:
        assert language_accept(t)
    for t in ["]", ")(", "(]", "([)]"]:
        assert not language_accept(t)
    
    print 'all test pass'