# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 9:11
# @Author  : Wang
# @FileName: test_encode.py
# @Software: PyCharm

a = '中文'
print('length of a: ', len(a))
print('encode utf-8 of a:', a.encode('utf-8'))
print('encode utf-8 of a length:', len(a.encode('utf-8')))
