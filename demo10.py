
#类的继承
# （1）必须有父类和子类，至少2个类
# （2）在子类中可以直接调用父类中的方法（功能）或属性（数据）

class People():
    age = 25
    def eat(self,people_type):
        print(people_type,"在吃饭")

class Students(People):

    pass

class Teacher(People):

    pass

s = Students()
s.eat("学生")
t = Teacher()
t.eat("老师")













