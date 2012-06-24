## Predicting a Figure Count
## counting 1 to 1000 using one hand in the order
## thumb -> first -> middle -> ring -> little -> ring -> middle ...
## on which figure does the counting stop?

## Rule:
## thumb:   (1), 9, 17
## first:   (2, 8), 10, 16
## middle:  (3, 7), 11, 15
## ring:    (4, 6), 12, 14
## little:  (5), 13, 31
## The period is 8

## 1000 % 8 == 0
## so it ends at first figure

import itertools
counting = itertools.cycle(['thumb', 'first', 'middle', 'ring', 'little',
                            'ring', 'middle', 'first'])
i = 1
while i < 1000:
    next(counting)
    i += 1

print i, next(counting)