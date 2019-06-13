# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 16:30
# @Author  : Wang
# @FileName: test_dict.py
# @Software: PyCharm

d = {'a': 1, 'b': 2, 'c': 3}

# print key
for i in d:
    print(i)

for key, value in d.items():
    print(key, value)

# test if an element is in dict key
print('a' in d)