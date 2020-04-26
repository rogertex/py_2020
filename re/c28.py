import re
s = 'A9733333eess777'
r=re.match('\d',s) #从首字母开始匹配,不匹配直接返回None
print(r)
r1 =re.search('\d',s) #serach 搜索整个字符串, 找到第一个为止
print(r1.group())
