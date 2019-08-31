# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 14:54
# @Author  : Wang
# @FileName: test_copy.py
# @Software: PyCharm
import copy

a = [1, 2, 3, 4]
b = a
c = a.copy()

# list里无复杂对象
# 改变a的值
print('改变a的值')
a[0] = 10
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
print('---------------')

print('改变c的值')
b[0] = 1
c[0] = 100
print(a)
print(b)
print(c)
print(id(a[0]))
print(id(b[0]))
print(id(c))
print('---------------')



# list里有复杂对象
a = [[1, 2, 3], 4, 5]
b = a
c = a.copy()

print('改变a的值')
a[0][0] = 10
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
print('------------')

print('改变c的值')
c[0][0] = 1
print(a)
print(b)
print(c)
print(id(a[0]))
print(id(b[0]))
print(id(c[0]))

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

b = copy.deepcopy(a)
print(a)
print(b)

a[0][0] = 10
print(a)
print(b)

b[0][0] = 20
print(a)
print(b)
