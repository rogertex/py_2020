import re
a = 'c|C++|Java|C#|Python|Javascript'

r = re.findall('Python', a)
if len(r) > 0:
    print('Python is there')
else:
    print('no Python')
