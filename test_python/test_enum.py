# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:04
# @Author  : Wang
# @FileName: test_enum.py
# @Software: PyCharm

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)