#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '面向对象：----------------'
class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print '%s: %s' % (self.__name,self.__score)

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()


print '继承多态：------------'

class Animal(object):
    def run(self):
        print 'Animal is running!'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

b = Animal()
c = Cat()
d = Dog()

print 'c(Cat) is Animal: ', isinstance(c,Animal)

print '__slots__:--------------'
# 给实例绑定一个属性：
class Stu(object):
    # __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称
    pass

s = Stu()
s.name = 'Michael'
print s.name

# 给实例绑定一个方法
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s,Stu)
s.set_age(25)
print s.age

# 给所有实例都绑定方法
def set_score(self,score):
    self.score = score

Stu.set_score = MethodType(set_score,None,Stu)
s.set_score(100)
print s.score

print '@property:-----------'
class Stu2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s2 = Stu2()
s2.score = 60 # s.set_score(60)
print s.score # s.get_score()
# s2.score = 9999 # ERROR score must between 0 ~ 100!

print '定制类：------------'
class Student(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    __repr__ = __str__


    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self, *args, **kwargs):
        print 'My name is %s.' % self.name

s = Student('Michael')
print s
s()


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    # 传入的参数可能是一个int，也可能是一个切片对象slice
    def __getitem__(self, item):
        if isinstance(item,int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item,slice):
            start = item.start
            stop = item.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print n,'\t',
print

f = Fib();
print f[0],f[1],f[2]
print f[3:6]