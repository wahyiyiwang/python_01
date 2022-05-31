class Student():
    __names = '788'
    def __init__(self,name,age,hight):
        self.names = name
        self.age = age
        self.hight = hight
    def study(self=None):
        print("{}今年{}岁，身高{}cm".format(self.name,self.age,self.hight))

# python的构造方法使用 __init__() 方法来表示，每次调用类的时候会自动被调用 ，主要用来初始化数
# 据。
d = Student("张一一",25,185)
# t = Student("刘一一",25)
# print(s.age)
# print(s.hight)

print(Student.names)





















