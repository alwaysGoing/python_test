# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 15:20
# @Author  : Wang
# @FileName: test_sum.py
# @Software: PyCharm


import numpy as np

a = np.array([1, 2, 3])
print(a.sum)
print(np.sum(a))
print(a.shape)
print(np.sum(a, 0))

# print(np.sum(a, 1))  #error, the shape of a is (3, ), not having 1st axis

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
print(np.sum(b))
print(np.sum(b, 0))
print(np.sum(b, 1))