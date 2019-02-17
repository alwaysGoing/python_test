# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 16:24
# @Author  : Wang
# @FileName: bubble_sort.py
# @Software: PyCharm

def bubble_sort(num_list):
    l = len(num_list)

    for i in range(l - 1):
        end = l - 1 - i
        for j in range(end):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


a = [3, 6, 12, 7, 1, 7, 4, 8]
print(bubble_sort(a))
