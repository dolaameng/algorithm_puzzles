## Is it possible to transform table1 to table2 
## by exchanging its rows and cols?

###########################################
##       table1
"""
1  2  3  4 
5  6  7  8
9  10 11 12
13 14 15 16
"""
###########################################

###########################################
##       table2
"""
12 10 11 9  
16 14 5  13
8  6  7  15
4  2  3  1
"""
###########################################

## AHA: the invariance here is that:
## by only exchanging rows and cols, the elements in
## the same row/col remains in the same