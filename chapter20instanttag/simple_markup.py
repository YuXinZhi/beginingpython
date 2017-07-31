import sys,re
from chapter20instanttag.util import *

print('<html><head><title></title></head><body>')
title = True
for block in blocks('C:\\Users\\Ben\\PycharmProjects\\beginingpython\\chapter20instanttag\\listing20-1.txt'):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')