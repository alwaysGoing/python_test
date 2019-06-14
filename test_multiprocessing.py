# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 16:37
# @Author  : Wang
# @FileName: test_multiprocessing.py
# @Software: PyCharm
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % (os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')

