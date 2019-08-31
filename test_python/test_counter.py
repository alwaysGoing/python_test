# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 15:51
# @Author  : Wang
# @FileName: test_counter.py
# @Software: PyCharm

from collections import Counter
a = [2, 3, 3, 5, 1, 2, 2]
N = Counter(a)
print(N)
for i in N:
    print(i)
print('----------------')
for i in list(N):
    print(i)
    print(N[i])