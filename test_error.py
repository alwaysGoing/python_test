# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:31
# @Author  : Wang
# @FileName: test_error.py
# @Software: PyCharm


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')