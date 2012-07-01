## http://www.pythonchallenge.com/pc/return/bull.html
## a = [1, 11, 21, 1211, 111221, 
## len(a[30]) = ?

def next_a(seq):
    seq = seq + '|'
    count_seq = []
    count = 1
    for i in range(len(seq)-1):
        if seq[i] != seq[i+1]:
            count_seq.append((count, seq[i]))
            count = 1
        else:
            count += 1
    return ''.join([str(count) + n
        for (count, n) in count_seq])

def a():
    current = '1'
    while True:
        yield int(current)
        current = next_a(current)
        
## tests
if __name__ == '__main__':
    ## test next
    assert next_a('1') == '11'
    assert next_a('11') == '21'
    assert next_a('1211') == '111221'
    ## test a generator
    generated_a = (1, 11, 21, 1211, 111221)
    for i, n in enumerate(a()):
        assert n == generated_a[i]
        if i > 3:
            break
    ## results
    ga = a()
    a_30 = [next(ga) for _ in range(31)][30]
    print a_30, len(str(a_30))