'''
@Author: Roger
@Date: 2020-04-26 13:57:30
@LastEditors: Roger
@LastEditTime: 2020-05-05 18:53:56
@Email: qunlin.gu@163.com
@Version: 
@Description: 
'''

#主要用来遍历/循环 序列或者集合,字典
a=[['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
      print(y)
 
""" a = [1, 2, 3]
for x in a:
    if x == 2:
        continue #当前代码继续,但是不执行x==2的情况.
        #break #当前代码终止
    print(x)
 """