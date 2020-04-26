from c10 import Human
class Student (Human):  # 类名要大写, Student 类继承了Human类
      tst = 0
      def __init__(self, school,name,age): #构造函数
        # Human.__init__(self,name,age)
        super(Student,self).__init__(name,age)#调用父类的构造函数
        self.school=school
      def __marking(self, score): #改变类的成员变量修改赋值通过方法来实现;双下滑线表示这个方法使私有的,不能被外部访问
        if score<0:
          self.score=0
        else:
          self.score=score  
        print(self.name + '本次成绩'+str(self.score))

      @classmethod  # 类方法
      def plus_sum(cls):
        cls.tst += 1
        print(cls.tst)

      @staticmethod  # 原则上不推荐使用静态方法
      def add(x, y):
        print('this is static method')
        
      def test(self):
        self.__tst1=-1
      def do_homework(self):
        super(Student,self).do_homework() #之类调用父类的方法.
        print('english homework')

      


