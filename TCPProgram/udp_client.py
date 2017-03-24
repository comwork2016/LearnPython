#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 不需要调用connect()，直接通过sendto()给服务器发数据
for data in ['Machael','Tracy','Sarah']:
    s.sendto(data,('127.0.0.1',9999))
    print s.recv(1024)
s.close()