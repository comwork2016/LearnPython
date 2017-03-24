#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

# # 创建一个logger
# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
#
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('test.log')
# fh.setLevel(logging.ERROR)
#
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # 定义handler的输出格式
# formatter = logging.Formatter('%(levelname)s: %(asctime)s - %(filename)s:%(lineno)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # 给logger添加handler
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # 记录一条日志
# logger.debug('debug logger')
# logger.info('info logger')
# logger.warning('warning logger')
# logger.error('error logger')
# logger.critical('critical logger')

logging.basicConfig(level=logging.DEBUG,format='%(levelname)s: %(asctime)s - %(filename)s:%(lineno)s - %(message)s')
logging.info('info logging')