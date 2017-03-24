#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '高阶函数：--------------'
def add(x,y,f):
    return f(x) + f(y)

print add(4,-6,abs)

print 'map/reduce:----------------'
# map/reduce
def f(x):
    return x*x

# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
L = map(f,[x for x in range(10)])
print L

# reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fn(x,y):
    return 10*x+y
L = reduce(fn,[x for x in range(10) if x % 2 == 1])
print L

# map / reduce example
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn,map(char2num,'13579'))

# filter
print 'filter:-----------------'
def is_odd(n):
    return n % 2 == 1
print filter(is_odd,[x for x in range(10)])

# sorted
print 'sorted:-----------------'
def reversed_cmp(x,y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21])
print sorted([36, 5, 12, 9, 21],reversed_cmp)

def ignore_case_cmp(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'], ignore_case_cmp)

# 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
print '函数作为返回值：---------------'
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,3,5,7,9)
print f
print f()

print '闭包：---------------'
# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(),f2(),f3()

def count1():
    fs = []
    for i in range(1,4):
        def fg(j):
            def g():
                return j*j
            return g
        fs.append(fg(i))
    return fs
f11, f21, f31 = count1()
print f11(),f21(),f31()

# 匿名函数有个限制，就是只能有一个表达式
print '匿名函数：--------------'
f = lambda x : x * x
print f(5)
print map(lambda x:x*x,[x for x in range(1,10)])

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数。
print '装饰器：------------'
import datetime

def log(func):
    def wrapper(*args,**kw):
        print 'call %s()'%func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now():
    print datetime.datetime.now()
now()
print now.__name__

import functools
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():'%(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log2('execute')
def now2():
    print datetime.datetime.now()

now2()
print now2.__name__

print '偏函数：-------------'
import functools
int2 = functools.partial(int,base=2)
print int2('1000000')
