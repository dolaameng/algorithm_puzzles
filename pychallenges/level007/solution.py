## http://www.pythonchallenge.com/pc/def/oxygen.html

import Image, os.path
fimage = os.path.join(os.path.split(__file__)[0], 'oxygen.png')
oxygen = Image.open(fimage)
XLEN, YLEN = oxygen.size

def all_equal(iterable):
    return len(set(iterable)) == 1

region = []

for y in range(YLEN):
    xend = next(x for x in range(XLEN) 
        if not all_equal(oxygen.getpixel((x, y))[:3]))
    if xend > XLEN / 2:
        region.append([oxygen.getpixel((x, y))[0] for x in range(xend)])
                        
ciphered = region[0]
ciphered_text =  ''.join(map(lambda p: chr(p), ciphered))
print ciphered_text
"""
text, i = [], 0
while i < len(ciphered_text):
    text.append(ciphered_text[i])
    while i < len(ciphered_text) and ciphered_text[i] == text[-1]:
        i += 1
"""
text = ''.join(ciphered_text[::7])
print text 
## smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
