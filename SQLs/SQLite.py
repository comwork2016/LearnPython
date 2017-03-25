#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('test.db') # 连接到SQLite数据库，如果文件不存在，会自动在当前目录创建:
cursor = conn.cursor() # 创建一个Cursor:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))') # 创建user表
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print cursor.rowcount # # 通过rowcount获得插入的行数:
cursor.close()
conn.commit() # 提交事务:
conn.close() # 关闭Connection:



# 查询记录：

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall() # 获得查询结果集:
print values
cursor.close()
conn.close()