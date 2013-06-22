#/usr/bin/env python
import sys, re
from util import *

print '<html><head><title>Hello</title><body>'
title = True

for block in blocks(sys.stdin):
    print block
    '''
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block);
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'
        
print '</body></html>'
'''

