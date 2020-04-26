def f1():
    a=10
    def f2():
        # a=20#此时将被python 认为是一个局部变量, 局部变量不会影响外部变量. 引用了局部变量就不是闭包了.
        print(a)
    print(a)
    f2()
    return f2
f=f1()        
print(f.__closure__)