## Knuth-Morris-Pratt Algorithm
## The algorithm takes a string as input and scans it from left to right.
## The output is the sequence of nonnegative integers such that the ith
## element is the length of speical string l(substr1..i). Where special
## string l is defined as the longest sub that is both a prefix and 
## suffix of a string.
## E.g., l(aba) = a, l(abab) = ab, l(ababa) = aba, l(abc) = ''

## Use KMP to check whether a given string A is a substring of string B.
## TODO