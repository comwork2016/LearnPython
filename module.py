#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

print '模块：-------------'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello World!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments'

if __name__ == '__main__':
    test()


# 别名:
# 这样就可以优先导入cStringIO。如果有些平台不提供cStringIO，还可以降级使用StringIO。
# 导入cStringIO时，用import ... as ...指定了别名StringIO，因此，后续代码引用StringIO即可正常工作。
try:
    import cStringIO as StringIO
except ImportError:
    import IOString

print '模块搜索路径：-------------'
print sys.path

print '添加模块路径：--------------'
sys.path.append('E:\\workspace')
print sys.path