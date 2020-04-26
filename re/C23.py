#数量词
# * 匹配0次或者无限多次
# +匹配1次或者无限多次
# ? 匹配0次或者一次
import re
a = 'pytho0python1pythonn2'
r=re.findall('python?',a) #默认贪婪
# r=re.findall('[a-z]{3,6}?',a)# 非贪婪
# 贪婪与非贪婪 ,python默认倾向与贪婪. 
print(r)