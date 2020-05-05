'''
@Author: Roger
@Date: 2020-04-26 17:08:55
@LastEditors: Roger
@LastEditTime: 2020-05-05 19:13:05
@Email: qunlin.gu@163.com
@Version: 
@Description: 
'''


a=[1,2,3,4,5,6,7,8]

for x in range(0,len(a),2):
    print(a[x],end='|')

b=a[0:len(a):2]
print(b)

l=a[0:7]
print(l)