# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 19:38
# @Author  : Wang
# @FileName: test_tuple.py
# @Software: PyCharm

import numpy as np

a = (1, 2, 3)
print(a[1])

b = np.array(a)
print(b.shape)

a = tuple({'a': 1, 'n': 2})
print(a)
print(a[1])
