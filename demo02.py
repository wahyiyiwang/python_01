#定义变量



if 1 == 1:
    print("@@@@@@")
elif 1==2:
    print("-----------------------")

a = 20
if a >20:
    print("a大于10")
else:
    print("a是个数字")
b = 15
if b > 20:
    print("正确")
else:
    print("错误")
print("=======================")
jixiao=70
if jixiao >= 80:
    print("500元")
elif 70 <= jixiao < 80:
    print("300元")
elif jixiao >= 60 and jixiao <70:
    print("200元")
else:
    print("无奖金")
print("=====================")
if 0:
    print("hi")
if 2:
    print("hello")
if "你好":
    print("hi1")
if "":
    print("hello2")

# for
for x in "12345":
    print(x)
# while
print ("==============")



print ("==============")
#打印1-10的数字
for N in range(1,10,1):
    print(N)

print ("==============")
for V in range(1,10,1):
    if V == 8:
        break
    print(V)
print("==============")
for V in range(1, 10, 1):
    print(V)
    if V == 8:
        break


print("=================")
lista =  []
listb = [1, 2 ,"abc",None]
print(lista)
print(listb)

# for x in range(1,11):
#     print(x)

for z in range(1,11,1):
    print(z)
    if z == 7:
        break
print("===========")
for y in range(1,11):
    if y == 7:
        continue
    print(y)








