# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 16:39
# @Author  : Wang
# @FileName: test_range.py
# @Software: PyCharm

nums = [3, 5, 2, 6]
print(len(nums) < 3)
print((2, 0)[len(nums) < 3])
print((2, 0)[True])
for _ in range((2, 0)[len(nums) < 3]):
    nums.remove(max(nums))

for i in range(-2):
    print(i)
print('-----------------------')
for i in range(1, 1):
    print(i)