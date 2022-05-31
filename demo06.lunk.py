#函数
def add(x,y):
    return x +y
print(add('3','hello'))

def student_lesson(grade,subject):
    z = '{}年级上{}课'.format(grade,subject)
    return z
print(student_lesson(grade=2,subject="语文"))
print(student_lesson(3,"语文"))

#默认参数
def study_language(name,language='python'):
    m = "{}要学习{}语言".format(name,language)
    return m
print(study_language('张三','java'))
print(study_language("李思"))

#需求：可以输入任何个数进行相加
#可变化参数：参数个数是可运行变化的，他有两种形式，分别是列表形式和字典形式
#1.定义列表形式
def add(x,y,*args):
    z = x + y + sum(args)
    return z
print(add(3,4))
print(add(3,4,5))
print(add(3,4,5,6,7,8))    #传递多个数

#使用列表方式调用
print(add(3,4,*[5,6,7,8]))      #传递列表

#2.可变化参数-字典形式的参数
def show_info(**kwargs):
    return kwargs

dt_date = {'x':1,'y':2,'z':3}

print(show_info(a='hello',b='world',c=123))
print(show_info(**dt_date))
print('================')
#面向对象
#1.定义一个电梯的类   class 类名（）：
class Elevator():
    #2.在类里申明属性（数据）和方法（函数）
    button = '开/关'
    floor = 15
    peple_nums = 13


    def open(self):
        print("面向对象-打开电梯") #打开电梯

    def close(self):
        print("面向对象-关闭电梯") #关闭电梯

    def run(self):
        print("面向对象-电梯运行") #运行电梯

#3.定义一个具体的对象，叫初始化对象，对象是一个实实在在的对象，---初始化对象：对象名 = 类名（）
e = Elevator()
#4.使用对象调用方法和属性     对项名.属性 ||  对象名.方法
e.open()
print(e.open())











