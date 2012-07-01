## http://www.pythonchallenge.com/pc/def/equality.html

## One small letter,
## surrounded by EXACTLY three big bodyguards on each of its sides.

import re, os.path
datapath = os.path.join(os.path.split(__file__)[0], 'data.txt')
r = re.findall('[a-z]+[A-Z]{3}([a-z])[A-Z]{3}[a-z]+', open(datapath).read())
print ''.join(r)