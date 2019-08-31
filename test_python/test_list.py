# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 11:19
# @Author  : Wang
# @FileName: test_list.py
# @Software: PyCharm

a = [1, 2, 3, 4]
print(a[:2])
print(a[::1])
print(a[::-1])

print('------------------------------')
b = a
c = a.copy()

del(a[0])
print(a)
print(b)
print(c)
print('------------------------------')

a = [1, 2, 3, 4]
b = a
c = a.copy()
a[0] = 10
print(a)
print(b)
print(c)
print('--------------------------')

a = [1, 2, 33]
b = [1, 2, 33]
print(a==b)

# print(a-b)
print(a[1:10])

a_1 = ["a1b2","a1b2","a1B2","A1B2","A1b2","A1B2"]
print(set(a_1))
print('a1b2' in a_1)
#
# a_1 = a_1+"fdsf"
# print(a_1)

a = ['asc', 'fsd']
for i in a:
    i = i[::-1]
print(a)

print(a[-3:])
a.remove('asc')
print(a)
# print(a.index('asc'))
print(a)

letters = [1, 4, 5, 3, 2, 7]
target = 7
l = [x > target for x in letters]
print(l)
print(max(l))
# letters[l.index(max(l))]

a = [0] * 4
print(a)
b = a
b[0] = 1
print(a)
print(b)

c = [a] * 4
print(c)
c[0][0] = 2
print(c)

c = [[0 for i in range(3)] for j in range(3)]
print(c)
c[0][0] = 1
print(c)

a = [1, 3, 4]
a.reverse()
print(a)

a = [1, 3, 4]
b = [1, 3, 4]
print(a==b)

a = 'cba'
a = list(a)
a.sort()
print(a)

a = ['cba', 'era']
for i in a:
    b = list(i).sort()
print(a)

a = [
    [4, 5],
    [1, 5],
    [6, 2]
]

a.sort()
print(a)

