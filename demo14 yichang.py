#异常与处理  try ... except语句
#语法格式：
# try:
#     被运行的代码块
# except Exception as e:
#     print(e)

#实例
def div(a,b):
    try:
        x = a / b
        return x
    except Exception as e:
        print(e)

print(div(3,4))
print(div(5,0))


#try...except...finally语句
try:
    f = open('a.txt','r')
    z = f.readline()
    for x in z:
        print(x)
except Exception as e:
    print(e)

finally:
    if f:
        f,close()





#main 方法