# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 15:22
# @Author  : Wang
# @FileName: test_json.py
# @Software: PyCharm

import json
d = dict(name='yingxin', age=25, score=100)
a = json.dumps(d)
print(a)

json_str = '{"name":"yingxin", "score":100, "age":25}'
b = json.loads(json_str)
print(b)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('yingxin', 25, 100)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))