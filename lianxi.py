#练习1-100的所有数的和
# a=1
# while a < = 100:
#     print("a的和",a)
#     a + = (a + 1)

#返回1-10之间的所有偶数
# lst1 = [1,2,3,4,5,6,7,8,9,10]
# print(lst1)
#
# for x in [1,2,3,4,5,6,7,8,9,10]:
#     print("打印1-10的x",x)
# print("==============")
# for x in [1,2,3,4,5,6,7,8,9,10]:
#     if x % 2 != 0:
#         print("打印1-10的所有偶数",x)
#
#
# lst1 = [1,3,5,,7,9]
# lst1.append(8)
# print(lst1)
print("==================")

dict1 = {'a':1,'b':2,'c':3,'d':'abcd'}
dict2 = {'e':10,'f':11}

print(dict1['a'])
# print(dict1['g'])

dict1['a'] = 11
print(dict1)


print("==================")

print("获取字典中c的值",dict1.get('c'))
print(dict1.get('g'))

print("获取字典中的键名",dict1.keys())
for x in dict1.keys():
    print("循环字典dict1",x)

print('获取字典中的值',dict1.values())
for y in dict1.values():
    print(y)

print("获取键值对",dict1.items())
for z,n in dict1.items():
    print(z,'============',n)

dict1.update(dict2)
print(dict1)

print('f' in dict1)
print('g' in dict1)
print("==================")
astr = "*"
bstr = astr.join("world")
print(bstr)

cstr = bstr.split("*")
print(cstr)
# 序列的通用操作

# 1. 索引: seq[index] ,index 代表的下标，默认从0开始 ; 索引支持：列表，元祖 ，字符串
lst = ['red','hello',2,3.5]
print(lst[1])          # 列表里的第二个值
print(lst[-1])

tp = ('red','hello',2,3.5)
print(tp[1])
print(tp[-1])

my_str = "redhello2"
print(my_str[1])
print(my_str[-1])


lst11 = [1,2,3,4,5,6,7,8,9,10]
print(lst11[0])
print(lst11[::2])


# 2. 序列的切片: seq[start:end:step] ,start代表位置，默认是从0开始，
# end是代表结束位置，如果不填写，代表列表的长度 ，step代表的是步长，默认是1
lst5 = ['red','green','blue','black','gold','orange']
print(lst5[1:5:1])      #获取第2个-5个元素
print(lst5[1:6:2])      #获取的偶数的值

print(lst5[::2])           # 省略了start和end
print(lst5[0:6:2])


print(lst5[2:])             # 省略了end和step
print(lst5[2:6:1])
print(lst5[2::])


print(lst5[1::2])           # 省略的是end

print(lst5[:3:])            # 省略的是start和step

print(lst5[::])
# print(lst5[])
print('===================================================')
logger.info("lst11{},请输入{}",12,"hello")






