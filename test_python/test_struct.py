# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 10:25
# @Author  : Wang
# @FileName: test_struct.py
# @Software: PyCharm

import struct

a = 10240099
b = struct.pack('>I', a)
print(b)

b1 = (a & 0xff000000) >> 24
print(b1)
b2 = (a & 0xff0000) >> 16
print(b2)
b3 = (a & 0xff00) >> 8
print(b3)
b4 = (a & 0xff)
print(b4)
print(bytes([b1, b2, b3, b4]))
print(bytes([b1]))
print(bytes([b2]))
print(bytes([b3]))
print(bytes([b4]))
