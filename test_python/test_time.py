# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 9:18
# @Author  : Wang
# @FileName: test_time.py
# @Software: PyCharm

import time

print(time.localtime())
print(time.strftime("%a %b %d %H:%M:%S %Y"), time.localtime())
