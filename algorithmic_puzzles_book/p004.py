## Ferry Soldiers
## 25 soldiers must cross a river without any bridge
## there are 2 boys playing in a rowboat.
## The boat can only fit 2 boys or 1 soldier.
## How can the soldiers get across the river and leave
## the boys in joint prossession of the boat? Assume
## the boat and boys and soldiers start being on the same side.

## AHA: since the boat can only fit ONE SOLDIER, And for one soldier
## the only way is: 2boys->, <-1boy, solider->, <-1boy, which goes
## back to the exact same initial state. So by solving by reduction,
## the subproblmes are independent of each other. It takes 100 trips
## in total.