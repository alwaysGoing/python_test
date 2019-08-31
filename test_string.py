# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 19:31
# @Author  : Wang
# @FileName: test_string.py
# @Software: PyCharm

s = 'dfdsf'
print(len(s))
s += ' '
print(len(s))
for i in range(len(s)):
    print(i)
    if s[i] != ' ' and s[i+1] == ' ':
        print('yes')
s = '""'
print(s.split(' '))
print(len(s.split(' ')))


def countSegments(s):
    # 给末尾添加一个空格
    s += " "
    count = 0
    for i in range(len(s)):
        if s[i] != " " and s[i + 1] == " ":  # 只要前一个字符不是空格且后一个字符是空格就计数一个单词
            count += 1
    return count
print(countSegments(s))
