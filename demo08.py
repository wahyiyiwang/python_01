

#实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况

class Student():

    name = ""
    grade = ""
    def study(self):
        print("{}年级学生{}正在学习".format(self.grade,self.name))

s1 = Student()
s1.name = "yiyi"
s1.grade = "3"
print(s1.study())

#使用构造方法实现以上内容
class Student():

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("{}年级学生{}正在学习".format(self.grade,self.name))
s2 =Student("张三",5)
s2.study()


















