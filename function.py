#!/usr/bin/env python
# -*- coding: utf-8 -*-

# function:
print 'function:--------------'
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print my_abs(12)
print my_abs(-12)
# print my_abs('A')


print 'return tuple:----------------'
import math

# return a tuple value
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

r = move(100,100,60,math.pi/6)
print r

# error usage of default parameter
print 'error usage of default parameter:-----------'
def add_end(L=[]):
    L.append('END')
    return L

print add_end()
print add_end()
print add_end()
# 不是只有一个'END'！！！
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

print 'correct usage of default parameter:-------------'
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end2()
print add_end2()
print add_end2()


# 可变参数
print '可变参数：-----------'
def calc_sum(*nums):
    sum = 0
    for n in nums:
        sum = sum + n
    return sum

print calc_sum()
print calc_sum(1,2,3)
nums = [1,2,3,4]
print calc_sum(*nums)


# 关键字参数
print '关键字参数:--------------'
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack',24,**kw)



# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
print '参数定义顺序：-------------'
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2, 3, 'a', 'b', x=99)