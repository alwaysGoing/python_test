# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 9:45
# @Author  : Wang
# @FileName: test_dot.py
# @Software: PyCharm

import numpy as np

a = np.array([1, 2])
b = np.array([[[1, 2, 3], [4, 5, 6]], [[2, 3, 4], [5, 6, 7]], [[1, 3, 4], [2, 4, 5]], [[2, 5, 1], [3, 5, 1]]])
print(a.shape)
print(b.shape)
c = np.dot(a, b)
print(c.shape)
print(c)
d = np.sum(c, 1)
print(d)
print(b.transpose(0, 2, 1).shape)