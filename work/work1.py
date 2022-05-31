#input
#input("字符串“）
# s = input("请输入一个整数")
# print(s)

#将字符串转化为整数： int(str), 注：只能转化数字的字符串
# a = int('10')
# print(type(a))
# b = int('a')   #error

#1.输入a,b,c,d4个整数，计算a+b-c*d的结果
#方法一
# a = input("请输入一个整数")
# b = input("请输入一个整数")
# c = input("请输入一个整数")
# d = input("请输入一个整数")
# print(int(a)+int(b)-int(c)*int(d))

#方法二
# a = 5
# b = 15
# c = 26
# d = 8
# e = a + b - c * d


#2. 打印1~100内被3整除的所有数的和。
#方法一
# y = 0
# for x in range(1,101,1):
#     if x % 3 == 0:
#         y += x
# print(y)

#方法二
sum = 0
x = 1
# while x <= 100:
#     if x % 3 == 0:
#         sum += x
#
#     x += 1
# print(sum)
#todo print(g)


# # 3. 使用range() 输出1 ~10内的所有奇数
# for x in range(1,11,2):
#     print(x)
#
# # 4.打印1~100所有偶数的和减去所有奇数的和的值
# y = 0
# z = 0
# for x in range(1,101):
#     if x % 2 == 0:
#         y += x
#     else:
#         z += x
# print(y-z)

# 5. 求1+2+3+...+100的和
# k = 0
# for x in range(1,101,1):
#     k += x
#     print(x)
# print(k)
#
# # 6.判断一个数n能同时被3和5整除
# n = 16
# if n % 3 == 0 and n % 5 == 0:
#     print("正确")
# else:
#     print("错误")


# 7.定义一个整数变量，判断该变量值是否是1 - 100 内的某个数，如果是打印出来
#方法1
# m = 100
# if m in range(1,100):
#     print("ok")
# else:
#     print("false")
# 方法2
# #m = input('请输入一个整数')
# if int(m) in range(1,101):
#     print('正确')
# else:
#     print("not")
# 8.输入三个整数x, y, z，请把这三个数由小到大输出。备注：输入方法：input()
# lst = []
# f = input("请输入一个整数")
# z = input("请输入一个整数")
# s = input("请输入一个整数")
# lst.append(f)
# lst.append(z)
# lst.append(s)
# print(lst)
# lst.sort()
# print(lst)
#print todo


# for x in range(3):
#     for g in range(3):


# 9.利用条件运算符的嵌套来完成此题：学习成绩 >= 90分的同学用A表示，60 - 89分之间的用B表示， 60分以下的用C表示。备注：需要使用input()方法
# score = 55
# if score >= 90:
#     print('A')
# elif 60 <= score < 90:
#     print('B')
# else:
#     print('C')

#10.将一个列表的数据复制到另一个列表中。
# alst = [12,48,89,123]
# blst = ['def','a','126']
# alst.extend(blst)
# print(alst)

#11.输出9 * 9乘法口诀表。
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(x,' * ',y,'=',x * y,end = ' ')
#     print()

#12.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# space = " " * (x-n)
# star = "*" * (2 n-1)


num = 5  #总数
x = num -1 #循环的伦茨x
for n in range(1,num):  #n循环次数
    space = " " * ( x - n)
    star = "*" * (2*n - 1)
    print(space+star)


#13.求s = a + aa + aaa + aaaa + aa...a的值，其中a是一个数字。例如2 + 22 + 222 + 2222 + 22222(此时共有5个数相加)，几个数相加由键盘控制。

# 14.题目：打印出如下图案（菱形）:



















