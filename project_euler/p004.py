"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

## back-envelope estimation
## 900 * 900 ~ 10**6 (1 million) to try, not a big challenge for brute force

## divergence : close-form formula for palindromic numbers less than 10, 10**2
##, ..., the sequence formula is 
## 