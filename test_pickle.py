# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 15:14
# @Author  : Wang
# @FileName: test_pickle.py
# @Software: PyCharm

import pickle

d = dict(name='yingxin', age=25, score=100)
f = open('a_test.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('a_test.txt', 'rb')
e = pickle.load(f)
f.close()
print(e)
