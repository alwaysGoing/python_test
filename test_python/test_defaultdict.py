# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 10:05
# @Author  : Wang
# @FileName: test_defaultdict.py
# @Software: PyCharm

from collections import defaultdict

s = 'missisnfjlf'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d)

# defaultdict里面的参数set指定的是value的数据类型
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
  d[k].add(v)

print(d)