#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print 'Process (%s) start ...' % os.getpid()

# unix like multiprocessing
# pid = os.fork()
# if pid == 0:
#     print 'this is a child process (%s) and parent process is (%s).' % (os.getpid(),os.getppid())
# else:
#     print 'i (%s) just create a child process (%s).' % (os.getpid(),pid)


# windows like
from multiprocessing import Process

def run_proc(name):
    print 'Run child process %s (%s)...' % (name,os.getpid())


if __name__ == '__main__':
    print 'Parent process is %s.' % os.getpid()
    p = Process(target=run_proc,args=('test',))
    print 'Process will start'
    p.start()
    p.join() # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print 'Process end.'

