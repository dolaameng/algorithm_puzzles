## http://www.pythonchallenge.com/pc/def/linkedlist.php

## follow the chain
## hint: urllib may help. DON'T TRY ALL NOTHINGS, 
## since it will never end. 400 times is more than enough.
## starting url: 
## http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

import urllib2, re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'

def do_nothing(nothing):
    while True:
        content = urllib2.urlopen(url+nothing).read()
        print content
        r = re.search('nothing is (\d+)', content)
        if r is None:    
            break
        else:
            nothing = r.group(1)
# step 1: do_nothing('12345')
## and the next nothing is 16044
## Yes. Divide by two and keep going.
# step 2: do_nothing(str(16044/2))