## Gray Code -- order of generating objects such that the next object
## is only a small modification of the preceding one.
## e.g., Generate 2**n strings of length n containing 0s and 1s
## such that two neighboring strings differ only in one bit.
## In geometric terms, the problem states that we can traverse the n-dimensional
## Bollean cube visiting each vertex exactly once.
## Alogorithm: Use Recursion. 
## Suppose we have the strings x1, x2, ... xk, in such order for k = 2**n, then 
## for k = 2**(n+1), the following strings satisfy the same order:
## 0x1, 0x2, .....0xk, 1xk, 1xk-1, .... 1x1

## binary strings of length n in gray order
def gray_strings(n):
    if n == 1:
        return ['0', '1']
    else:
        str_n_1 = gray_strings(n-1)
        return map(lambda s: '0'+s, str_n_1) + \
                map(lambda s: '1'+s, str_n_1[::-1])
                
################ Some problems related to Gray Code #########
## Generate all sequences of length n composed of the numbers
## 1..k in such an order that neighboring sequences differ
## only in one place, and the numbers at this place differ by 1
def gray_sequences(n, k):
    raise RuntimeError('not implemented')
    
## Generate all permutations of the numbers 1..n in such a way
## that each permutation is obtained from the preceding oen by
## exchange of two adjacent numbers. e.g., for n = 3, one possible
## answer is: 3.21 -> 23.1 -> 2.13 -> 12.3 -> 1.32 -> 312
def gray_permutations(n):
    raise RuntimeError('not implemented')
    
## tests
if __name__ == '__main__':
    ## test gray_strings
    assert gray_strings(1) == ['0', '1']
    assert gray_strings(3) == ['000', '001', '011', '010', '110', '111', '101', '100']
    gray_20 = gray_strings(15)
    for i in range(1, 2**15):
        diff0 = abs(gray_20[i].count('0') - gray_20[i-1].count('0'))
        assert diff0 == 1
    print 'all tests passed'