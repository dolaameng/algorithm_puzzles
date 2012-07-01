## http://www.pythonchallenge.com/pc/def/ocr.html

## find rare characters in the mess below:
## data.txt

import collections, string
import os.path
datafile = os.path.join(os.path.split(__file__)[0], 'data.txt')
text = ''.join([c for c in open(datafile).read() if c in string.letters])
print text
#dictionary = collections.Counter(text)
#print dictionary
print r'http://www.pythonchallenge.com/pc/def/%s.html' % (text,)