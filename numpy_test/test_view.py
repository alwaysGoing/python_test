# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 21:06
# @Author  : Wang
# @FileName: test_view.py
# @Software: PyCharm

import numpy as np

a = np.array([1, 2])
print(a.shape)

a = a.reshape((-1, 1))
print(a.shape)