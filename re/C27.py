import re
a='A8C3721D86'
def convert(value):
    matched = value.group()
    if int(matched)>6:
        return '9'
    else:
        return '0'



r = re.sub('\d', convert,a) # 替换字符
# language = language.replace('c#', 'Go')
print(r)



