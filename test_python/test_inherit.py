# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 11:01
# @Author  : Wang
# @FileName: test_inherit.py
# @Software: PyCharm

class Animal:
    def __init__(self, num):
        self.num = num

    def run(self):
        print('animal running!!!')
    def animal_run(self):
        print('I am your father!!!')
    def get_num(self):
        print('animal'+self.num)

class Dog(Animal):
    def __init__(self, a):
        self.a = a
    def run(self):
        print('dog running!!!')

d = Dog(111)
d.run()
d.animal_run()
print(d.a)
# 继承不会继承父类的属性
# print(d.num)

class Cat(Animal):
    def __init__(self, b):
        self.b = b
        super(Cat, self).__init__(44)
    def run(self):
        print('cat running!!!')

c = Cat('66')
c.run()
print(c.b)
print(c.num)

# 如果在子类中需要父类的构造方法就需要显式地调用父类的构造方法，或者不重写父类的构造方法。子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。
class Bird(Animal):
    def run(self):
        print('bird running!!!')
    def get_num(self):
        print('bird '+self.num)

b = Bird('aaa')
b.get_num()


# class Father(object):
#     def __init__(self, name):
#         self.name = name
#         print("name: %s" % (self.name))
#
#     def getName(self):
#         return 'Father ' + self.name
#
#
# class Son(Father):
#     def getName(self):
#         return 'Son ' + self.name
#
#
# if __name__ == '__main__':
#     son = Son('runoob')
#     print(son.getName())