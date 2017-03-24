#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print 'Process (%s) start ...' % os.getpid()

pid = os.fork()

if pid == 0:
    print 'this is a child process (%s) and parent process is (%s).' % (os.getpid(),os.getppid())
else:
    print 'i (%s) just create a child process (%s).' % (os.getpid(),pid)