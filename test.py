#!/usr/bin/env python
import re
src = "url is http://www.baidu.com"

def sub_url(match):
    return '<a href="%s">%s</a>' % (match.group(1), match.group(1))

def sub(name):
    method = getattr('sub_' + name);
    return method

ret = re.sub(r'(http://[\.a-zA-Z]+)', sub("url"), src);

print ret
