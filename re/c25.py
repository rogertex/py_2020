#
import re
language='PythonC#\nJavaPHP'

r= re.findall('c#.{1}',language,re.I|re.S) #re.I 或略大小写
print(r)