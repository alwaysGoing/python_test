# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 19:08
# @Author  : Wang
# @FileName: merge_sort.py
# @Software: PyCharm

def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    mid = len(num_list) // 2

    left = merge_sort(num_list[:mid])
    right = merge_sort(num_list[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    left_len = len(left)
    right_len = len(right)

    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

a = [3, 6, 12, 7, 1, 7, 4, 8]
print(merge_sort(a))