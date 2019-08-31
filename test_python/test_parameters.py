# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 14:34
# @Author  : Wang
# @FileName: test_parameters.py
# @Software: PyCharm

a = 1
b = 1
print(id(a))
print(id(b)) # 发现a和b的内存地址一样

print('---------------------------------')
a = 2
print(id(a))
print(id(b))  # 发现a和b的内存地址不一样
print('---------------------------------')

def test(c):
    print('test before')
    print(id(c))
    c += 2
    print('test after')
    print(id(c))
    return c

a = 2
print('before invoke test')
print(id(a))
n = test(a)
print('after invoke test')
print(id(a))
print('----------------------------------')

class Student:
    def __init__(self, age):
        self.age = age

s = Student(10)

def modify_age(p):
    p.age = 20
    return p

p = modify_age(s)
print(s.age)
print(p.age)
print('---------------------------------------')

def test_list(l):
    l.append('sss')
    return l

l = [1, 2]
after = test_list(l)
print(l)
print(after)
