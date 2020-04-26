class Human():
    sum = 0  # 类变量

    def __init__(self, name, age):  # 实体方法/构造函数/实例变量
      self.name = name
      self.age = age
    def get_name(self):
      print(self.name)
    def do_homework(self):
      print('this is parent method')