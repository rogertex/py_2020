# 装饰器
# 特性 注解


import time 
def f1():
    
    print('this is a small rabinet')
def f2():
    
    print('this is a small big')
#unix 时间戳

f1()
#开闭原则: 对修改是封闭的,对扩展是开放的


def print_current_time(func): #把函数作为参数传递到prnt_curent_time 函数.
    print(time.time())
    func()
print_current_time(f1)
print_current_time(f2)