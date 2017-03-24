#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'assert:------------'

def foo(s):
    n = int(s)
    assert n!=0,'n is zero!'
    return 10/n

    # foo('0')