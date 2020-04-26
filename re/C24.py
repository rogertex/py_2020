#边界匹配
import re
qq='100000000001'
#4~8
r= re.findall('^\d{4,8}$',qq)
print(r)