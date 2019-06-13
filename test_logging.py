# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:53
# @Author  : Wang
# @FileName: test_logging.py
# @Software: PyCharm


import logging

# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')