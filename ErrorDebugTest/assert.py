#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG,format='%(levelname)s: %(asctime)s - %(filename)s:%(lineno)s - %(message)s')

logging.info('assert:------------')

def foo(s):
    n = int(s)
    assert n!=0,'n is zero!'
    return 10/n

foo('0')