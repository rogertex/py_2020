import re
a='c0c++java8C#cfc'
rs=re.findall('\d',a) #\d =抽象0-9数字
print(rs)
#正则表达式
#'Python' 普通字符 '\d' 元字符
#\D =非数字 ,\w =字符和数字
# \s 空白字符\S
# . 除了换行符以外的所有字符