import time
import math
import random

def decorator(func):
    def wrapper(*args,**kw):   #*args 可变参数 **kw关键字参数
        print(str(random.random()))
        print(time.time())
        func(*args,**kw) #*args 可变参数
    return wrapper

@decorator    #语法糖@, 装饰器 
def f1(func_name):
    print('this is a big'+func_name)


@decorator
def f2(func_name1,func_name2):
    print('this two funciton'+func_name1+func_name2)


@decorator
def f3(func_name1,func_name2,**kw):
    print('this two funciton'+func_name1+func_name2)
    print(kw)

# f=decorator(f1)
# f()
f1('  test func')
f2(' func1',' func2')
f3(' func1',' func2',a=1,b=2,c='123')


