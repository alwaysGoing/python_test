# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 14:52
# @Author  : Wang
# @FileName: test1.py
# @Software: PyCharm

import argparse

parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('--echo', '-e', help='an example')
parser.add_argument('echo_another')
parser.add_argument('--epochs', default=50, type=int, metavar='N', help='number of total epochs to run')

# 可以在命令行里传值，也可以在parse_args里用list的形式传入参数
args = parser.parse_args(['fdf', '--epochs', '90', '--echo', 'ddd'])
print(args)
print('echo_another: ', args.echo_another)
print('epochs: ', args.epochs)
print('echo: ', args.echo)

print('----------------------------------------------------------------')

parser = argparse.ArgumentParser(prog='myprogram')
parser.add_argument('--foo', nargs=3)
parser.add_argument('bar', nargs=1)
args = parser.parse_args('c --foo a b c'.split())
print(args)
print(parser.print_help())


