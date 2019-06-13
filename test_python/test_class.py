# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 17:06
# @Author  : Wang
# @FileName: test_class.py
# @Software: PyCharm

from types import MethodType

class My_class:
    def __init__(self, x):
        self.x = x


def set_y(self, y):
    self.y = y
a = My_class(1)
print(a.x)

a.set_y = MethodType(set_y, a)
a.set_y(1)
print(a.y)