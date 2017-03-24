#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '迭代：------------'
for i,value in enumerate(['a','b','c']):
    print i,value

print '列表生成式：------------'
L = [x*x for x in range(1,11)]
print L

L2 = [x*x for x in range(1,11) if x%2 == 0]
print L2

L3 = [m+n for m in 'ABC' for n in 'XYZ']
print L3

import os
L4 = [d for d in os.listdir('D:/')] # windows中的编码为gbk
for str in L4:
    print str.decode('gbk'),'\t',
print


d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.iteritems():
    print k,'=',v

# 在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print '生成器：---------------'
g = (x*x for x in range(10))
for x in g:
    print x,
print

# define generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1

gf = fib(6)
print gf
for num  in gf:
    print num,
print