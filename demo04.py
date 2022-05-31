#索引，索引具体的值
list = ['red','hello',2,3,5,'abc']
print(list[0])

tp =('red','hello',2,3,5,'abc')
print(list[5])

my_str = 'redhello2'
print(my_str[1])

#切片，获取序列多个值
lst5 = ['red','green','blue','black','gold','orange']
print(lst5[1:6:2]) #取偶数
print(lst5[0:6:1]) #取全部
print(lst5[2:5:1]) #取blue-gold
print(lst5[::3]) #取全部
print(tp[1:5:1]) #取tp的hello-5
print("取my_str的ello",my_str[4:8:1])
print("取第3个后的所有",lst5[2:])
print(lst5[2:10:1])
print(lst5[2::1])
print(lst5[2::])
print(lst5[::])
print(lst5[:3:])
lst1 = [1,2,3,4,5,6,7,8,9,10]
print("取基数",lst1[0:9:2])
print("===============")

#相加 乘
alst = [1,3]
blst = [2,4]
clst = alst + blst
print(clst)
dlst = clst * 3
print("clst的3遍",dlst)
print("=======================")
astr = 'abcd'
bstr = 'efgh'
cstr = astr + bstr
print("打印cstr的值",cstr)
dstr = astr * 3
print("打印dstr",dstr)
print("=======================")

#检查元素
lst8 = ['red', 'yellow', 'cream', 'blue', 'gunmetal']
print("索引list8中是否存在blue",'blue' not in lst8)
#序列中的方法
gstr = 'abcd'
elst = list(gstr)
print(elst)

#
lst8 = ['red', 'yellow', 'cream', 'blue', 'gunmetal']
for index,vls in enumerate(lst8):
    print(index,'======',vls)



