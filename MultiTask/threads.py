#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time,threading

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name,n)
        time.sleep(0.5)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name # MainThread
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print 'thread %s ended' % threading.current_thread().name

# 多个线程同时操作一个变量怎么把内容给改乱了
balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print 'not locked: balance =',balance

balance = 0
lock = threading.Lock()
def run_thread2(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread2,args=(5,))
t2 = threading.Thread(target=run_thread2,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print 'locked: balance =',balance

local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student,threading.current_thread().name)

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()