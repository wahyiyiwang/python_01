#类的多肽
# （1）必须有父类和子类，至少2个类
# （2）在子类中可以直接调用父类中的方法（功能）或属性（数据）
#继承与多肽的区别：子类引用父类的方法就是继承，子类的方法覆盖父类就是多肽
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