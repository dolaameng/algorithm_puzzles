## pronounce it
## http://www.pythonchallenge.com/pc/def/peak.html

import pickle, os.path

banner_file = open(os.path.join(os.path.split(__file__)[0], 'banner.p'))
banner = pickle.load(banner_file)

ascii = '\n'.join([
    ''.join(map(lambda (c, times): c*times, line))
    for line in banner
])
open('result.txt', 'w').write(ascii)