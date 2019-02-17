# -*- coding: utf-8 -*-
# @Time    : 2019/2/17 16:32
# @Author  : Wang
# @FileName: insert_sort.py
# @Software: PyCharm

def insert_sort(num_list):
    l = len(num_list)
    for i in range(1, l):
        current_num = num_list[i]
        for j in range(i):
            if num_list[i - j - 1] > current_num:
                num_list[i - j] = num_list[i - j - 1]
                num_list[i - j - 1] = current_num
            else:
                num_list[i - j] = current_num
                break
    return num_list


a = [3, 6, 12, 7, 1, 7, 4, 8]
print(insert_sort(a))
