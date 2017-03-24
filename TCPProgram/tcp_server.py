#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG,format='%(levelname)s: %(asctime)s - %(filename)s:%(lineno)s - %(message)s')

def tcplink(sock,addr):
    logging.debug('Accept new connection from %s:%s...' % addr)
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(0.5)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s' % data)
    sock.close()
    logging.debug('Connection from %s:%s closed' % addr)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999)) # 绑定IP和port地址
s.listen(5) # max connections is 5
logging.debug('Waiting for connection...')
while True:
    sock,addr = s.accept() # accept a connection
    # 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
    print addr
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()



