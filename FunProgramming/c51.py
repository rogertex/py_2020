# 闭包=函数+环境变量(函数定义时候的变量)
# 闭包的作用, 保存了函数的现场保存了.

def curve_pre():
    a = 25 #环境变量

    def curve(x):
        
        return a*x*x
        # print('this is curve of function')
    return curve


f = curve_pre()
print(f(2))
