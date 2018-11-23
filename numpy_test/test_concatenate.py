# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 10:09
# @Author  : Wang
# @FileName: test_concatenate.py
# @Software: PyCharm

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[5, 6], [7, 8]])
print(b)

# concatenate is to make two or more arrays to be one

# the first parameter is the arrays to be concatenated, the second parameter is the axis to follow.
c = np.concatenate((a, b), 0)
print(c)

c = np.concatenate((a, b), 1)
print(c)