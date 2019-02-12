# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 13:37
# @Author  : Wang
# @FileName: test_ravel.py
# @Software: PyCharm

import numpy as np

# ravel后得到的，改变会对原数据产生影响；而flatten不会

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
b = a.ravel()
print(b)

b[0] = 10

print(a)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

b = a.flatten()
print(b)

b[0] = 10
print(a)

c = a == a
print(c)
print(np.mean(c))