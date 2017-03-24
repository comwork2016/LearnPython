#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Sample:

    def __enter__(self):
        print 'In __enter__()'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'In __exit__()'
        print "type:", exc_type
        print "value:", exc_val
        print "trace:", exc_tb

    def do_something(self):
        bar = 1/0
        return bar + 10

with Sample() as sample:
    sample.do_something()
