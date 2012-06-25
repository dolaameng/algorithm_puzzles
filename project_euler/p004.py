"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

## back-envelope estimation
## 900 * 900 ~ 10**6 (1 million) to try, not a big challenge for brute force

## divergence : close-form formula for 
## number of palindromic numbers less than 10, 10**2
##, ..., the sequence formula is 
## a(n) = 2(10**(n/2) - 1) for even n
## a(n) = 11*10**((n-1)/2) - 2 for odd n
def palindromic_nums(upto = None):
    n = 1
    while n <= upto or upto is None:
        yield (2 * (10**(n/2) - 1)
                if n % 2 == 0
                else 11 * 10 ** ((n-1)/2) - 2)
        n += 1

## linear algorithm        
def is_palindromic(n):
    s = str(n)
    start, end = 0, len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return False
        start, end = start+1, end-1
    return True
        
if __name__ == '__main__':
    ## print list(palindromic_nums(10))
    ## test is_palindromic
    assert is_palindromic(181) == True
    assert is_palindromic(1) == True
    assert is_palindromic(1211) == False
    print max(n1*n2 for n1 in range(999, 100, -1)
                    for n2 in range(999, 100, -1)
                    if is_palindromic(n1*n2))
    print 'all tests pass'