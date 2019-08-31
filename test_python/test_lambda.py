# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:21
# @Author  : Wang
# @FileName: test_lambda.py
# @Software: PyCharm
from functools import reduce

n = 5
a = reduce(lambda x, y: x*y, range(1, 1+n))
print(a)

a = lambda: 'none'
print(a())

a = [4, 5, 1]
b = sorted(range(len(a)), key=lambda k: a[k], reverse=True)
print(b)