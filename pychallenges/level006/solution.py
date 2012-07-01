## http://www.pythonchallenge.com/pc/def/channel.html
## HINT: zip file
## TITLE:" now there are pairs"

## get channel.zip, unzip it and find readme.txt, it reads
## welcome to my zipped list.

## hint1: start from 90052
## hint2: answer is inside the zip

## in 90052.txt, it reads 
## Next nothing is 94191

import os.path, re
from zipfile import ZipFile 
current_path = os.path.split(__file__)[0]
z = ZipFile(os.path.join(current_path, 'channel.zip'))

def do_nothing(nothing):
    comments = []
    while True:
        content = z.open(nothing+'.txt').read()
        comment = z.getinfo(nothing+'.txt').comment
        comments.append(comment)
        print content
        result = re.search('nothing is (\d+)', content)
        if not result:
            print 'COMMENTS:'
            open('level006/comments.txt','w').write(''.join(comments))
            break
        else:
            nothing = result.group(1)
            
do_nothing('90052')