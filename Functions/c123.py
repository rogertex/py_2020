a=1
b=2
c=3 

a,b,c=1,2,3 #上面的代码和下面的相同

d=1,2,3
print(type(d))
a,b,c =d  #序列解包
# a,b=d #不能用两个变量来解包3个变量的tuple
# a,b=[1,3,4]
print(d)
