#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

s = r'ABC\-001'

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
    print 'match ok'
else:
    print 'match failed'

print 'a b    c'.split(' ')
print re.split(r'\s+','a b   c')
print re.split(r'[\s,;]+','a,b;; c  d')

# 用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0),m.group(1),m.group(2) # group(0)永远是原始字符串