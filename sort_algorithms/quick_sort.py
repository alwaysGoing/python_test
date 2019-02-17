# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 16:48
# @Author  : Wang
# @FileName: quick_sort.py
# @Software: PyCharm

def quick_sort(num_list, start, end):
    if start >= end:
        return

    left = start
    right = end

    anchor = num_list[left]

    while start < end:
        while num_list[end] >= anchor and start < end:
            end -= 1
        num_list[start] = num_list[end]
        while num_list[start] < anchor and start < end:
            start += 1
        num_list[end] = num_list[start]
    num_list[end] = anchor

    quick_sort(num_list, left, start - 1)
    quick_sort(num_list, start + 1, right)
    return num_list

a = [3, 6, 12, 7, 1, 7, 4, 8]
print(quick_sort(a, 0, len(a)-1))






