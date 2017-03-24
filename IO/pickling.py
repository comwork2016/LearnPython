#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import cPickle as pickle
except ImportError:
    import pickle

print 'dump:---------------'
d = dict(name='Bob',age=20,score=88)
print pickle.dumps(d)

with open('dump.txt','wb') as f:
    pickle.dump(d,f)

print 'load:--------------'
with open('dump.txt','r') as f:
    dp = pickle.load(f)
    print dp

print 'json dumps:---------------'
import json
d = dict(name='Bob', age=20, score=88)
jd = json.dumps(d)
print jd
print 'json loads:----------------'
dp = json.loads(jd)
print dp

print 'class json dumps:---------------'
class Student(object):

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(stu):
    return {
        'name':stu.name,
        'age':stu.age,
        'score':stu.score
    }

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s = Student('Bob',20,88)

json_str = json.dumps(s,default=student2dict)
print json_str
print json.dumps(s,default=lambda obj:obj.__dict__)

print 'class json loads:------------'
print json.loads(json_str,object_hook=dict2student)

