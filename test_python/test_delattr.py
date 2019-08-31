# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 16:05
# @Author  : Wang
# @FileName: test_delattr.py
# @Software: PyCharm

class Coordinate:
    x = 10
    y = -5
    z = 0

point_1 = Coordinate()
print('x= ', point_1.x)
print('y= ', point_1.y)
print('z= ', point_1.z)

print('delete')

# delattr(Coordinate, 'z')
# print(point_1.z) ## error

# delattr(point_1, 'z')  # 报错，只能作用于类，不能作用于实例化对象


