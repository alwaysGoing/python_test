# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 16:30
# @Author  : Wang
# @FileName: test_dict.py
# @Software: PyCharm

import operator

d = {'a': 1, 'b': 2, 'c': 3}

# print key
for i in d:
    print(i)

for key, value in d.items():
    print(key, value)

# test if an element is in dict key
print('a' in d)

d = d.items()
# print(d)
d = sorted(d, key=operator.itemgetter(1), reverse=True)
print(d)
print(d[0])

d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())
# print(d.keys()[0]) # 报错，'dict_keys' object does not support indexing
print(d.items())
# print(d.items()[0]) # 同样报错，'dict_items' object does not support indexing
print(str(d.keys())[0:10])
print(type(d.keys()))
print(list(d.keys()))

for value in d.values():
    print(value)