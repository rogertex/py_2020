# def funcname(parameter_list):
#     pass
# 1. 参数列表可以没有
# 2. return value none
import sys
# sys.setrecursionlimit(10000) #限制递归的次数


def add(x, y):
    reuslt = x+y
    return reuslt


def print_code(code):
    print(code)


a = add(2, 3)
b = print_code('Python')
print(a, b)
