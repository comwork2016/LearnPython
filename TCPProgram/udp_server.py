#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import logging
logging.basicConfig(level=logging.DEBUG,format='%(levelname)s: %(asctime)s - %(filename)s:%(lineno)s - %(message)s')

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # SOCK_DGRAM指定了这个Socket的类型是UDP
s.bind(('127.0.0.1',9999))
# 不需要调用listen()方法
logging.debug('Bind UDP on 9999...')
while True:
    data,addr = s.recvfrom(1024) # recvfrom()方法返回数据和客户端的地址与端口
    print 'Received from %s:%s.' % addr
    s.sendto('Hello, %s'%data,addr)
