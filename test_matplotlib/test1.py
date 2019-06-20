# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 20:16
# @Author  : Wang
# @FileName: test1.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2999, 3000)
print(a)
b = np.linspace(2999, 5998, 3000)
print(b)
c = np.random.randint(-1000, 1000, [3000])
print(c)
print(c.shape)
b += c


plt.plot(range(3000), a)
plt.plot(range(2999, 5999), b)
plt.xticks([0, 1000, 2000, 3000, 4000, 5000, 5999], [r'$t0$', r'$t1$', r'$t2$', r'$t3$', r'$t4$', r'$t5$', r'$t6$'])
plt.show()
