'''
@Author: Roger
@Date: 2020-04-23 20:28:58
@LastEditors: Roger
@LastEditTime: 2020-05-06 19:12:12
@Email: qunlin.gu@163.com
@Version: 
@Description: 
'''

class Human():
    name = 'peter'  # 类变量
    sum1 = 0  # 类变量
    def __init__(self, name, age):  # 实例方法/构造函数/实例变量
      self.name = name   #self.name = 实例变量
      self.age = age
      # name = name  # 这里的name 是类变量,不是实例变量, 实例变量要用self.name
      # age = age
      print(name) # 这里的name 读取的是形参的name
      print(self.name)
      print(self.age)
    def get_name(self):
      print(self.name)
    def do_homework(self):
      print('this is parent method')

student1 = Human('roger1',23)
# print(student1.name)
# print(Human.name)11
# print(student1.__dict__)