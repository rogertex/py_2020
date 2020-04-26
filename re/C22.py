#数量词
import re
a = 'python 1111java678php'
r=re.findall('[a-z]{3,6}',a) #默认贪婪
# r=re.findall('[a-z]{3,6}?',a)# 非贪婪

# 贪婪与非贪婪 ,python默认倾向与贪婪. 

print(r)