#格式化字符串
my_str = "my name is %s" % ("张三")
print(my_str)

#格式化整数
my_str1 = "张三 今年 %d 岁" %(25.5)
print(my_str1)

#格式化浮点数
my_str2 = "一斤苹果%f元" %(5)
print(my_str2)

#格式化辅助指令1
my_str3 = "一斤苹果%8.3f元"%(5.8)
print(my_str3)

#格式化辅助指令2
my_str4 = "一斤苹果%-8.3f元"%(5.8)
print(my_str4)

#格式化辅助指令3
my_str5 = "一斤苹果%08.3f元"%(5.8)
print(my_str5)

#格式化format "{}{}".format("")
my_str6 = "张三 今年{} 岁,今天星期{}" .format(25,"二")
print(my_str6)

#格式化format位置参数 "{}{}{}".format(第一个数，第二个数，第三个数)
my_str7 = "张三 今年{1} 岁,今天星期{0}" .format("二",25)
print(my_str7)

#格式化format关键字 "{x}{y}".format(x="字段",y="字段")
my_str8 = "张三 今年{0} 岁,今天星期{y}" .format(25,y="二")
print(my_str8)

#连接字符串 jion
astr = "+"
bstr = astr.join("world")
print(bstr)

#分割字符串 split
cstr = "hello world php c++ python zentao"
dstr = cstr.rsplit(" ")
print(dstr)
print("============")
#查找字符
estr = "helloworld"
fstr = estr.find("l")
print(fstr)

#查找以xxx结尾/开头的字符串
gstr = "测试报告.doc"
if gstr.endswith('.doc'):
    print("是一个文档")


#替换字符串
hstr = "hello world"
istr = hstr.replace('hello','555')
print(istr)

#列表 字符串转化
print('========================')
str11  = 'hello'
lstb = list(str11 )
print(lstb)

lst2 = ['black',2,3,'hello','green','red']
str1 = str(lst2)
print(str1)

for x in str1:
    print(x,end=' ')

print('========================')

#循环序列并索引
lst1 = ['black',2,3,'hello','green','red']

for x in lst1:
    print(x,end=' ')

for index,ualue in enumerate(lst1):
    print(index,'=========',ualue)

print('========================')
# 列表推导式 ： [ 表达式2  循环体  表达式1 ],执行的顺序：先执行循环体 ，其次执行后面的表达式1 ，最后执行表达式2

# 需求 ： 生成一个1~10的列表
lst3 = []
for x in range(1,11):
    lst3.append(x)
print(lst3)

lst4 = [ x for x in range(1,11)]
print(lst4)

# 需求2 ： 生成一个1~10的列表 ，要求只打印奇数的数

print([ x for x in range(1,11) if x % 2 != 0])

# 需求3 ： 生成一个1~10的列表 ，要求只打印奇数的数且结果加10

print([ x + 10 for x in range(1,11) if x % 2 != 0])




