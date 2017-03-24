#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'open file:-------------'
try:
    f = open('read(gbk).txt','r')
    print f.read()
finally:
    if f:
        f.close()

print 'with ... as ... clause:----------'
with open('read(gbk).txt','r') as f:
    print f.read().decode('gbk')

print 'readlines:------------'
import codecs
f = codecs.open('read(gbk).txt','r','gbk')
for line in f.readlines():
    print line


print 'write file:------------'

with open('write.txt','w') as f:
    f.write('test中文')

print 'directory:-------------'

import os
print os.path.abspath('.')
print os.path.join('/Users/michael', 'testdir')
os.mkdir('./mkdir')
raw_input('press enter to remove dir')
os.rmdir('./mkdir')
print os.path.split(os.path.abspath('./'))
print os.path.splitext(os.path.abspath('./io.py'))
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']